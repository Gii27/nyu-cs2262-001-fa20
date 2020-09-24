from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def time():
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f UTC")
    return time_str

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
