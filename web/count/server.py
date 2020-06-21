__author__ = 'rocky'
import csv
from flask import Flask, render_template, request
import sys
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addcount', methods=['POST'])
def addcount():
  localtime = time.asctime(time.localtime(time.time()))
  username = request.form["user"]
  password = request.form["password"]
  location = request.form['location']
  group = request.form['num']
  unlocksequence = str(username) + " " + str(password)
  with open('accounts.txt', 'r') as f:
    if unlocksequence in f.read():
      unlock = True
    else:
      unlock = False
  if not unlock:
    return "Your account does not exist."
    sys.exit()
  with open('uploadrecord.csv', 'a') as f:
    f.write("\n" + str(location) + ", " + str(username) + ", " + str(group))
    f.close()
  with open('timebaseddata.csv', 'a') as f:
    currenttime = str(localtime)
    hourtime = currenttime[11:13]
    f.write("\n" + location + ", " + str(hourtime) + ":00, " + str(group))
    f.close()
  return 'You are going to %s with a party of %s. Have fun! <br/> <a href="/">Back Home</a>' % (location, group)

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1')
