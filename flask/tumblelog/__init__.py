from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "SUPER_SECRET"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')