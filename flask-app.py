from flask import Flask, request
from db_application import *

app = Flask(__name__)
  
@app.route('/select')
def select_api():
    start = request.args.get('start', 0)
    end = request.args.get('end', -1)
    return db_select(start, end)
  
@app.route('/insert')
def insert_api():
    line = request.args.get('line', None)
    return "Success" if db_insert(line) else "Error"

@app.route('/delete')
def delete_api():
    num_lines = request.args.get('num', 1)
    return "Success" if db_delete(num_lines) else "Error"

if __name__ == '__main__':
    app.run()