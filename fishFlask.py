# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:45:03 2021

@author: noopa
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("fish.pkl" ,"rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    result = ''
    if prediction[0] == 0:
        result = 'Bream'
    elif prediction[0] == 1:
        result = 'Parkki'
    elif prediction[0] == 2:
        result = 'Perch'
    elif prediction[0] == 3:
        result = 'Pike'
    elif prediction[0] == 4:
        result = 'Roach'
    elif prediction[0] == 5:
        result = 'Smelt'
    else:
        result = 'Whitefish'
    
    return render_template('index.html', prediction_text='The flower belong to species {}'.format(result))
    
    


if __name__=='__main__':
    app.run()
