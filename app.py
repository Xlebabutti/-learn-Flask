from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

result = []
result1: object = {}

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        date_str = request.form['date']
        time_str = request.form['time']
        date_time = datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')
        print(result.append(date_time))
        return 'Data and Time!'
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)