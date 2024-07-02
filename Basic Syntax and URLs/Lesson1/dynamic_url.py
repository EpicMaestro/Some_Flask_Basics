from flask import Flask

app=Flask(__name__)

@app.route("/")
def Home():
    return"Welcome to Home page of ABC"

@app.route("/welcome/tony")
def Welcome_tony():
    return "Welcome to ABC , Tony Bhai!!"

@app.route("/welcome/steve")
def Welcome_steve():
    return "Kasha aahe steve Bhau ?"

@app.route("/welcome/jonny")
def wel_jonny():
    return "All-rounder"

# 10000 log hue to ? 10000 likhoge kya ye code . It violates DRY principle . Thoda sensible bane . 
# An idea is to use a path parameter .

@app.route("/welcome/<name>")
def welcome(name):
    return f"Welcome {name.title()} .ABC mein aapka swaagat hain"

if __name__=="__main__":
    app.run(debug=True)
