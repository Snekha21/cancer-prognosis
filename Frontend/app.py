'''
Created on 
Course work: Cancer Prognosis
@author: Snekha
Source:
    
'''
# Import necessary modules


from flask import Flask, redirect, request, url_for, render_template
import os


# PORT = os.environ["PY_PORT"]


app = Flask(__name__)

#constants



@app.route("/",methods=["POST", "GET"])
def start():
    
    if request.method == "POST":
        return redirect(url_for("accounts"))
    return render_template("frontpage.html")

@app.route("/account",methods=["POST","GET"])
def accounts():

    if request.method == "POST":
        return redirect(url_for("round_1"))
    return render_template("login.html")

yes=lyes=syes=byes=llyes=pyes=lyes3=syes3=byes3=llyes3=pyes3=0

@app.route('/round1',methods=["GET","POST"])
def round_1():
    global yes
    yes=0
    if request.method == "POST":
        for i in range(11):
            if(request.form["choice-radio%d"%(i)] == "yes"):
                yes += 1
        return redirect(url_for("round_2"))
    return render_template('index.html')

@app.route('/round2', methods=["GET","POST"])
def round_2():
    
    if request.method == "POST":
        global lyes
        lyes=0
        for i in range(4):
            if(request.form["lchoice-radio%d"%(i)] == "yes"):
                lyes += 1
        global pyes
        pyes=0
        for i in range(3):
            if(request.form["pchoice-radio%d"%(i)] == "yes"):
                pyes += 1
        global byes
        byes=0
        for i in range(3):
            if(request.form["bchoice-radio%d"%(i)] == "yes"):
                byes += 1
        global syes
        syes=0

        for i in range(4):
            if(request.form["schoice-radio%d"%(i)] == "yes"):
                syes += 1
        global llyes
        llyes=0
        for i in range(3):
            if(request.form["llchoice-radio%d"%(i)] == "yes"):
                llyes += 1
        
        return redirect(url_for("round_3"))

    return render_template("round2.html")

@app.route("/round3", methods=["GET","POST"])
def round_3():
    if(request.method=="POST"):
        global lyes3
        lyes3=0
        for i in range(10):
            if(request.form["lchoice-radio%d"%(i)] == "yes"):
                lyes3 += 1
        global pyes3
        pyes3=0
        for i in range(10):
            if(request.form["pchoice-radio%d"%(i)] == "yes"):
                pyes3 += 1
        global byes3
        byes3=0
        for i in range(10):
            if(request.form["bchoice-radio%d"%(i)] == "yes"):
                byes3 += 1
        global syes3
        syes3=0
        for i in range(10):
            if(request.form["schoice-radio%d"%(i)] == "yes"):
                syes3 += 1
        global llyes3
        llyes3=0
        for i in range(10):
            if(request.form["llchoice-radio%d"%(i)] == "yes"):
                llyes3 += 1
        
        return redirect(url_for("result"))
    return render_template("round3.html")

@app.route("/result", methods=["GET","POST"])
def result():
    yesper = (yes/4)*10
    lyesper = round((((lyes+lyes3)/14)*90),2)
    byesper = round((((byes3+byes)/13)*90),2)
    syesper = round((((syes3+syes)/13)*90),2)
    pyesper = round((((pyes3+pyes)/14)*90),2)
    llyesper = round((((llyes3+llyes)/13)*90),2)
    return render_template("result.html",yes=yesper,lyes=lyesper,byes=byesper,syes=syesper,pyes=pyesper,llyes=llyesper)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port =8000,debug=True)