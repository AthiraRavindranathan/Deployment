import numbers
from xml.etree.ElementPath import prepare_self
from flask import Flask, render_template, request
import joblib

# initialize the app
app = Flask(__name__)    # main     #start

#load the model
model = joblib.load('models/diabetic_79.pkl')

#logic
# One decorator can associate with one function
@app.route('/')
def main():
    return render_template('main.html')


@app.route('/contact')
def contact():
    return render_template('main.html')


@app.route('/course')
def course():
    return render_template('main.html')

@app.route('/submit', methods=['post'])
def submit():
    # name = request.form.get("name")
    # number = request.form.get("number")
    # mail = request.form.get("email")
    # print(name)
    # print(number)
    # print(mail)
    preg = float(request.form.get("preg"))
    plas = float(request.form.get("plas"))
    pres = float(request.form.get("pres"))
    skin = float(request.form.get("skin"))
    test = float(request.form.get("test"))
    mass = float(request.form.get("mass"))
    pedi = float(request.form.get("pedi"))
    age =  float(request.form.get("age"))

    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    if output[0] == 1:
        data = 'diabetic'
    else:
        data = 'not diabetic'
    return data
    #return "Form submitted"
    
    
# run the app
app.run(debug=True)    #end  #->debug=True makes the change