from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__) # 앱 이름을 flaskapp으로
model = pickle.load(open('model/energy_model.pkl','rb'))

## 메인 페이지 라우팅
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def board():
    return render_template('board.html')

## 데이터 예측 처리
@app.route('/prediction', methods=['GET','POST'])
def prediction():
    data1= request.form['연료원']
    data2= request.form['Month']
    data3= request.form['Day']
    arr=np.array([[data1,data2,data3]])
    pred = model.predict(arr)
    return render_template('return.html',data=pred)

@app.route('/intro')
def intro():
    return render_template('intro.html')     


# 앱 실행
if __name__=="__main__": 
    app.run(host='0.0.0.0',port=5000) 

#host: 모든 점속을 허용한다, 외부 사용시 포트 5000번 지정 실행
# 해당 사이트 접속 시 가장 기본 페이지('/')에서 index 함수가 실행될 것