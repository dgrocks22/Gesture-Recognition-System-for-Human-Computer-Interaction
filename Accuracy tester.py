import serial
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier

# Collecting Sensor Inputs and Creating Dataset
#arduino_port = 'COM10'  
#baud_rate = 9600

#ser = serial.Serial(arduino_port, baud_rate)

dataset = pd.read_csv(r'C:\Users\Dell\Desktop/new_flex_sensor_data1.csv')

X = dataset.iloc[:, :-1]  
y = dataset['Gesture']    

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#scaler = MinMaxScaler()
#X_train_scaled = scaler.fit_transform(X_train)
#X_test_scaled = scaler.transform(X_test)

# Create an SVM classifier
model = SVC()
model.fit(X_train, y_train)

classifier_predictions = model.predict(X_test)
print(accuracy_score(y_test, classifier_predictions)*100)
