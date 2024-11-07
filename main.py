# Function to print full pyramid pattern
from flask import Flask
app = Flask(__name__)

@app.route("/")
def full_pyramid(n):
   return 'Hello World'

