import justpy as jp


def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a=web_page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=web_page, text="This graph represents course review analysis",)
    return web_page


jp.justpy(app)
