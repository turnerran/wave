from h2o_wave import main, app, Q, ui, data


# Array buffer
a = data(fields='price low high', size=8, rows=[
        [4, 50, 100],
        [6, 100, 150],
        [8, 150, 200],
        [16, 350, 400],
        [18, 400, 450],
        [10, 200, 250],
        [12, 250, 300],
        [14, 300, 350],
    ],
    pack=True
    )

ac = data(fields='price low high', size=8, columns=[[4,6,8,16,18,10,12,14],[50,100,150,350,400,200,250,300],[100,150,200,400,450,250,300,350]],
    pack=True
    )

# Cyclic buffer
c = data(fields='price low high', size=-8, rows=[
        [4, 50, 100],
        [6, 100, 150],
        [8, 150, 200],
        [16, 350, 400],
        [18, 400, 450],
        [10, 200, 250],
        [12, 250, 300],
        [14, 300, 350],
    ])

# Map buffer
m = data(fields='price low high', rows=dict(
        fst=[4, 50, 100],
        snd=[6, 100, 150],
        trd=[8, 150, 200],
        fth=[16, 350, 400],
        fih=[18, 400, 450],
        sth=[10, 200, 250],
        seh=[12, 250, 300],
        nth=[14, 300, 350],
))

@app('/demo')
async def serve(q: Q):
        q.page['meta'] = ui.meta_card(box='')
        q.page['example'] = ui.plot_card(
            box='1 1 4 5',
            title='Histogram',
            data=ac,
            plot=ui.plot([ui.mark(type='interval', y='=price', x1='=low', x2='=high', y_min=0)]),
        )

        await q.page.save()
