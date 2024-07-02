# Import the Flask class from the flask module.
from flask import Flask

# Create an instance of the Flask class for the application.
# The __name__ variable is a special Python variable that is set to the name of the module in which it is used.
# When the module is run directly, __name__ is set to "__main__".
app = Flask(__name__)

# Define a route for the root URL ("/").
# The @app.route("/") decorator binds the URL "/" to the home function.
@app.route("/")
@app.route("/Home")
def home():
    # The home function returns a simple string that will be displayed on the home page.
    return "<h1>Welcome to the Home Page</h1>"

@app.route("/About")
def About():
    return "<h2> Welcome to About Section of the Page</h2>"
#Adding a Path parameter to our webpage using <param_name>
@app.route("/Welcome/<name>")
def Welcome(name):
    return f"<h1> Hi {name.title()} , Iss Webpage par aapka Swaagat hain !</h1>"

# Specifying the type of parameters used . By default , it is a string 
@app.route("/Calc/<int:num>") # Bina space ke likhna int:num 
def Calc(num):
    return f" Calcualtion ke baad aapka result aayega {num+10}"

#Using multiple path parameters ( Calling function ka naam alag rakhna )
@app.route("/DO_param/<int:num1>/<int:num2>")
def Do_param(num1,num2):
    return f"<h1>Ek number hain {num1}, doosra hain {num2}; addition is {num1+num2}</h1>"

# Check if the script is run directly (not imported as a module).
if __name__ == "__main__":
    # Start the Flask development server with debug mode enabled.
    # Debug mode provides detailed error messages and auto-reloads the server on code changes.
    app.run(debug=True)
