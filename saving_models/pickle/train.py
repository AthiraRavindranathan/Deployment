import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']

df = pd.read_csv(url,names = names)
print(df)

array = df.values

X = array[:,0:8]
y = array[:,8]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)

# Loading of the model
model = LogisticRegression()
model.fit(X_train,y_train)

# Accuracy
result = model.score(X_test,y_test)
print(result)

# Prediction- Batch Prediction
pred = model.predict(X_test)
print(pred)

# Single Prediction
pred = model.predict([[10,20,54,67,23,14,56,56]])
if pred[0] == 1:
    print('Diabetic')
else:
    print('Not a Diabetic')
print(pred)

# Saving model
#pickle.dump(model,open('diabetic_79.pkl','wb'))  #pkl or sav
file_name = open('diabetic_79.pkl','wb')
pickle.dump(model,file_name) 