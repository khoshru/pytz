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
    time_dict = {

     "paris" : get_paris_time(),
     " tehran":get_tehran_time()
    }
    return time_dict
show_time()  
    

if __name__ == '__main__':
    app.run(debug=True )
 