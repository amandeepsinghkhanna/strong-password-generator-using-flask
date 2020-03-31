"""
    @script-author: Amandeep Singh Khanna
    @script-description: Password genertor.
"""

# importing the standard python modules:
import os # for interfacing with the operating system.
import random # for random number generation.

# importing the external python modules:
from flask import Flask, request, render_template

# user-defined function to generate a strong password:
def generate_password(pass_len):
    choices = {
        "digits": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        "low_chars": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                  'w', 'x', 'y', 'z'],
        "up_chars":['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 
                'W', 'X', 'Y', 'Z'] ,
        "symbols": ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')'] 
    }
    password = "".join([random.choice(choices[random.choice(list(choices.keys()))]) for i in range(pass_len)])
    return password
    
# flask application:
app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def index():
    password = generate_password(16)
    return render_template("index.html", password = password)
    
if __name__ == "__main__":
    app.run(debug = True)




