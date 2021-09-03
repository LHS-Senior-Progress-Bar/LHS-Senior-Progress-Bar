from flask import Flask, render_template, Response
import time
from datetime import datetime
app = Flask('app')


@app.route('/')
def hello_world():
  # percent_display = 0
  return render_template("index.html")

@app.route('/progress')
def progress():
	return Response(generate(), mimetype= 'text/event-stream')

def generate():
  x=0
  start_date = datetime(year=2021, month=8, day=31, hour=8, minute=30)
  graduation_date = datetime(year=2022, month=6, day=5, hour=10)
  time_in_between = graduation_date - start_date
  time_in_seconds = time_in_between.total_seconds()

  while x <= 100:
    now_date = datetime.now()
    between_start_and_current = now_date - start_date
    between_start_current_seconds = between_start_and_current.total_seconds()
    percent = between_start_current_seconds / time_in_seconds
    x = percent * 100
    x = round(x, 4)
    yield "data:" + str(x) + "\n\n"
    time.sleep(0.5)

app.run(host='0.0.0.0', port=8080)