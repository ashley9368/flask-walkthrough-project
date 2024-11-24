import os
from flask import Flask

app = Flask(**name**)

@app.route("/")
def index():
return "Hello, World"

if **name** == "**main**":
app.run(
host=os.environ.get("IP", "0.0.0.0"),
port=int(os.environ.get("PORT", "5000")),
debug=True)