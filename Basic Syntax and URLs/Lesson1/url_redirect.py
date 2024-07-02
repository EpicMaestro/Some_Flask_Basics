#It is a process in which when users visit a particular URL , they are navigated / guided to a different URL .

#Usecases
# 1) If a page is deleted , users need to be redirected to a new URL
# 2) If maintenance of the webpage is going on , users can be directed
# 3) If a website is renamed , users can be redirected to appropriate URL


#Common Response Codes 
# 1) 301: Moved permanently
# 2) 308: Redirected Permanently
# 3) 307 : Temporary Redirect 

from flask import Flask , redirect ,url_for
#redirect for redirecting to the specific webpage corresponding to the URL given as input
# url_for for giving an endpoint name associated with a URL so that it can generate a URL , instead of explicitly giving one as input

import time  

app=Flask(__name__)

@app.route("/")
def Home():
    return f"<h1>Welcome to your result</h1>"

#we will need 2 more endpoints , those of redirected webpages
@app.route("/passed")
def passed():
    return f"<h1>Party Time !!</h1>"

@app.route("/failed")
def failed():
    return f"<h1>Khatam Tata GoodBye GAYA </h1>"

@app.route("/score/<name>/<int:marks>")
def Score(name,marks):
    if marks<30:
        time.sleep(2)
        return redirect(url_for("failed"))
    else:
        time.sleep(0.5)
        return redirect(url_for("passed"))


if __name__=="__main__":
    app.run(debug=True)
