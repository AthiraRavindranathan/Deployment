import pickle

#user_input = [5,4,3,6,7,8,9,5]

user_input = input("Please enter the comma seperated value:").split(',')
data = [int(i) for i in user_input]

#Load the model
model = pickle.load(open('diabetic_79.pkl','rb'))

pred = model.predict([data])
if pred[0] == 1:
    print('Diabetic')
else:
    print('Not a Diabetic')