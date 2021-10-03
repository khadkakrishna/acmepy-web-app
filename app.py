from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def home(): 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)