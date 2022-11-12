import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
app=Flask(__name__)

model=pickle.load(open('Logistic.pkl','rb'))
scalar=pickle.load(open('scalar.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)
    print(output)
    return render_template("home.html",prediction_text="The Result for parkinson's disease is {}".format(output))



@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=model.predict(data)
    
    return jsonify(float(output[0]))

if __name__=="__main__":
    app.run(debug=True)
    