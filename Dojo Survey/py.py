from flask import Flask, render_template , request # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def Cites():
    return render_template('index.html')  # Return the string 'Hello World!' as a response
    
@app.route('/rizek',methods=["post"]) # The "@" decorator
def procces_info():
    return render_template ('index1.html', name_user = request.form['username'] , city = request.form['location'] , comments = request.form['comment'])

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

