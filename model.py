import pandas as pd
import numpy as np
from sklearn import preprocessing


df = pd.read_csv('energy.csv')
### print(df.head(1))
df=df[['연료원','Month','Day','전력거래량']]
### print(df.head(1))


from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import pickle
import requests
import json


#2nd trial modeling for lable
category_col = ['연료원','Month','Day']
labelEncoder = preprocessing.LabelEncoder()

mapping_dict ={}
for col in category_col:
    df[col] = labelEncoder.fit_transform(df[col])

    mapping_name = dict(zip(labelEncoder.classes_,
                    labelEncoder.transform(labelEncoder.classes_)))
    mapping_dict[col] = mapping_name
#print(mapping_dict)

train,test=train_test_split(df,test_size=0.2,random_state=8)
# print(train.shape,test.shape)

target='전력거래량'
features = df.columns.drop([target])
X_train = train[features]
X_test =test[features]
y_train = train[target]
y_test= test[target]

lr_energy_model = LinearRegression()
lr_energy_model.fit(X_train,y_train)
y_pred_lr = lr_energy_model.predict(X_test)

lm = lr_energy_model.fit(X_train,y_train)
#pickle.dump(pipe, open('model/energy_model.pkl','wb'))
pickle.dump(lm,open('model/energy_model.pkl','wb'))


'''#original trial
pipe = make_pipeline(
    OneHotEncoder(),
    LinearRegression()
)

pipe.fit(X_train,y_train)
#print('정확도:',pipe.score(X_test,y_test))
'''