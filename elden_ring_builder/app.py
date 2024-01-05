from flask import Flask

from elden_ring_builder.ext import configuration
#from elden_ring_builder.ext import database
#from elden_ring_builder.ext import admin

app = Flask(__name__)
configuration.init_app(app)
#database.init_app(app)
#admin.init_app(app)

@app.route("/")
def hello_world():
    return "Hello, universe!"

if __name__ == "__main__":
    app.run(debug=True)