from flask import Flask, session, redirect, render_template, request


app = Flask(__name__)
app.secret_key ='safekey'

@app.route('/')
def root_route():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template('index.html')


@app.route('/add2')
def plus_two():
    if "count" in session:
        session["count"] += 2
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)