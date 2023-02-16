import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

from sklearn.preprocessing import MinMaxScaler,StandardScaler

## Splitting data

from sklearn.model_selection import train_test_split

X=df.drop(columns=['Price'],axis=1)
y =df['Price']

X_train_org, X_test_org, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state = 0)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train_org)
X_test = scaler.transform(X_test_org)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

## xgboost model

import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.metrics import classification_report,confusion_matrix

xg_reg = XGBRegressor()

xg_reg.fit(X_train,y_train)

xg_preds = xg_reg.predict(X_test)

print('Train score: {:.4f} %'.format(xg_reg.score(X_train, y_train)*100))
print('Test score: {:.4f} %'.format(xg_reg.score(X_test, y_test)*100))

print('RMSE: {:.4f}'.format(np.sqrt(mean_squared_error(y_test,xg_preds))))
print('r2_score :', xg_reg.score(X_test,y_test))


##

print("Price predction: ", xg_reg.predict([[133551, 2, 2, 1, 400, 37.58, 33, 1, 2, 0, 0]])*0.1)


######################
import pandas as pd
from sklearn.naive_bayes import GaussianNB


import joblib

joblib.dump(xg_reg, "xg_reg.pkl")

