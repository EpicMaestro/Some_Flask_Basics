from flask import Flask , redirect ,url_for


import time  

app=Flask(__name__)

@app.route("/")
def Home():
    return f"<h1>Welcome to your result</h1>"


@app.route("/passed/<sname>/<int:smark>")
def passed(sname,smark):
    return f"<h1>Party Time !! Party Dehi {sname.title()} for securing {smark}</h1>"

@app.route("/failed/<sname>/<int:smark>")
def failed(sname,smark):
    return f"<h1>Khatam Tata GoodBye GAYA.{smark} mein kucch nahi ho sakta {sname.title()} </h1>"

@app.route("/score/<name>/<int:marks>")
def Score(name,marks):
    if marks<30:
        time.sleep(2)
        return redirect(url_for("failed",sname=name ,smark=marks))
# url_for : Generate a URL to the given endpoint with the "given values".
    else:
        time.sleep(0.5)
        return redirect(url_for("passed",sname=name ,smark=marks))


if __name__=="__main__":
    app.run(debug=True)