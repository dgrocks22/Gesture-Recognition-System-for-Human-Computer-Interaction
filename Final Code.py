import serial
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


# Step 1: Collecting Sensor Inputs
arduino_port = 'COM10'  
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)

dataset = pd.read_csv(r'C:\Users\Dell\Desktop/new_flex_sensor_data2.csv')

# Step 2: Split the dataset into input features (X) and target variable (y)
X = dataset.iloc[:, :-1]  
y = dataset['Gesture']    

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the ML Model
model = SVC()
model.fit(X_train, y_train)

l = []
c = 0

# Step 4: Real-time Gesture Prediction
while c < 1:
    # Read a line of sensor readings from Arduino
    sensor_readings = ser.readline().decode().strip()

    flex_values = sensor_readings.split(',')

    # Create a new row for the instance with the sensor readings
    new_row = pd.DataFrame([flex_values], columns=['Flex1', 'Flex2', 'Flex3', 'Flex4', 'Flex5', 'X', 'Y', 'Z'])
    
    predicted_gesture = model.predict(new_row)
    
    l.append(predicted_gesture)
    
    print("Predicted Gesture:", l[c])
    
    c = c + 1
    
while c >= 1:
    
    sensor_readings = ser.readline().decode().strip()
    
    flex_values = sensor_readings.split(',')

    new_row = pd.DataFrame([flex_values], columns=['Flex1', 'Flex2', 'Flex3', 'Flex4', 'Flex5', 'X', 'Y', 'Z'])
    
    predicted_gesture = model.predict(new_row)
    
    l.append(predicted_gesture)
    
    if l[c] != l[c-1]:

        print("Predicted Gesture:", l[c])
    
    c = c + 1
    
