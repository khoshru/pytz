from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


def get_tehran_time():
    tehran_tz = pytz.timezone('Asia/Tehran')
    return datetime.now(tehran_tz).strftime('%Y-%m-%d %H:%M:%S')

def get_paris_time():
    paris_tz = pytz.timezone('Europe/Paris')
    return datetime.now(paris_tz).strftime('%Y-%m-%d %H:%M:%S')

@app.route("/time")
def show_time():
    paris_dic = get_paris_time()
    tehran_dict = get_tehran_time()
    result = {"paris" :paris_dic} | {"tehran " :tehran_dict}
    return result

if __name__ == '__main__':
    app.run(debug=True )
