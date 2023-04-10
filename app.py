from flask import Flask,request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))


@app.route('/home', methods = ['GET','POST'])    #creating API
def welcome():
    data = request.form
    if request.method == 'POST':
        age = data['Age']    #request.form.get(variable name from html)
        sex = data['SEX']
        cp = data['cp']
        thalach = data['thalach']
        exang = data['exang']
        oldpeak = data['oldpeak']
        slope = data['slope']
        ca = data['ca']
        thal = data['thal']

    Result = model.predict([[age,sex,cp,thalach,exang,oldpeak,slope,ca,thal]])
    if Result[0] == 0:
        return 'Patient is not having heart disease'
    else:
        return 'Patient is having heart disease'

@app.route('/login')    #creating API
def login():
    return 'This is a login page'

@app.route('/feed')    #creating API
def feed():
    return 'Display feed'

if __name__ == '__main__':
    app.run(debug=True)