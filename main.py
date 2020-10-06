from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index_page():
    print("index page route")
    return render_template('index.html', var_to_javascript=json.dumps('This will go to the html + javascript'))

if __name__ == "__main__":
    app.run()