from sanic import Sanic

from data import CONFIG


app = Sanic("twecle")


app.run(**CONFIG)
