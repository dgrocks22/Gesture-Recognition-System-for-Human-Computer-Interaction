import serial
import pandas as pd


# Collecting Sensor Inputs and Creating Dataset
arduino_port = 'COM10'  
baud_rate = 9600
num_instances = 50

ser = serial.Serial(arduino_port, baud_rate)

dataset = pd.DataFrame(columns=['Flex1', 'Flex2', 'Flex3', 'Flex4', 'Flex5', 'X', 'Y', 'Z', 'Gesture'])

# Collect sensor readings for each instance
for i in range(28):
    
    gesture = input("Enter the gesture: ")
    
    for j in range(num_instances):
        
        sensor_readings = ser.readline().decode().strip()
        flex_values = sensor_readings.split(',')
    
        # Create a new row for the instance with the sensor readings and gesture
        new_row = pd.DataFrame([flex_values + [gesture]], columns=['Flex1', 'Flex2', 'Flex3', 'Flex4', 'Flex5', 'X', 'Y', 'Z', 'Gesture'])
    
        # Append the new row to the dataset
        dataset = dataset.append(new_row, ignore_index=True)
        
dataset.to_csv(r'C:\Users\Dell\Desktop/new_flex_sensor_data2.csv', index=False)