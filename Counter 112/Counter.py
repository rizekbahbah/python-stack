from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def count():
    if "Counter1" not in session:
        session["Counter1"] = 0

    
    if "Counter2" not in session:
        session["Counter2"] = 0

    return render_template("index.html",CounterTwo=session['Counter2'],CounterOne=session['Counter1'])


@app.route('/addToOne')
def addToOne():
    session['Counter1']=session['Counter1']+ 1
    return redirect("/") 

@app.route('/destroyOne')
def Destroy():
    session['Counter1']=0
    return redirect("/") 

@app.route('/addToTwo')
def AddToTwo():
    session['Counter2'] +=1
    return redirect ('/')


@app.route('/destroy2')
def destroy2():
    session['Counter2'] =0
    return redirect ('/')


if __name__=="__main__":
    app.run(debug=True)   

