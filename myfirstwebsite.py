from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p> welcome to our homepage <p>"

@app.route("/about_us")
def about_us():
    return "<p> we are bla bla bla company </p>"

@app.route("/contact_us")
def contact_us():
    return "<b> we are located at nowhere </b>"

@app.route("/products")
def products():
    return "<p> We have no product </p>"

@app.route("/services")
def services():
    return ("<p> we can do any job you want </p>")
