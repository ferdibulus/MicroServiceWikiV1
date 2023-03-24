from flask import Flask
import json
#import event
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Start taking data from api in compile time
print("Initial Data process has been started. It'll take approximately 15 minutes")


# event.getDataFromApi()


@app.route("/api/getAllEvents")
def get():
    return json.dumps([obj.__dict__ for obj in event.returnData])


@app.route("/api/deneme")
def getaa():
    return "Hello Ferdi"


@app.route("/")
def hello():
    return "Hello1 World from Flask in a uWSGI Nginx Docker container with \
     Python 3.8 (from the example template)"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
