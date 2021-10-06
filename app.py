from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def home(): 
    return render_template('index.html')

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/createCert")
def createCert():
    return render_template("create_cert.html")

demo_data= [{ 'name': "cert1", 'status': 'READY'}, { 'name': "cert2", 'status': 'FAILED'}]

@app.route("/viewCert")
def viewCert():
    return render_template("view_cert.html", certsList=demo_data)

@app.route("/manageCert")
def manageCert():
    return render_template("manage_cert.html", certsList=demo_data)

if __name__ == "__main__":
    app.run(debug=True)