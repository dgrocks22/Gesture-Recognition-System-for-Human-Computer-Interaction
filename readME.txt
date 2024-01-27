Dataset:

new_flex_sensor_data2 - This csv file contains the flex sensors and gyroscope values for each gesture. There are a total of 28 gestures in this csv file. They are: 26 letters of the English Alphabet, The gesture for "I Love You" and the gesture for "Eat".

--------------------------------------------------------------------------------------------------------------------------------------

Pictures:

Screenshot 2023-07-17 140610 - This PNG file has a basic block diagram of what the project looks like.
Screenshot 2023-07-17 143146 - This PNG file has a basic circuit diagram of the project.

--------------------------------------------------------------------------------------------------------------------------------------

Codes:

Arduino Code - The .txt file has a code that you can copy and paste into your Arduino IDE. The Arduino board used in this project was Arduino Nano. This code allows the Arduino Nano to read the values from the Flex Sensors and the Gyroscope.

Creating Dataset - This PY file contains the code for creating a dataset that contains the Flex Sensor and Gyroscope values to train the Machine Learning model. This code helps in reading the values from the Arduino board and it directly feeds it into a csv file to have the dataset ready in no time. 

Final Code - This PY file contains the final code of the project that we used to predict the gesture in real time. Once you settle your hand into your desired sign's position, the ML model reads the values from the Arduino and predicts the gesture. The model is pre-trained using Support Vector Machine algorithm over the created dataset to later predict the gesture in real time. 

Accuracy tester - This PY file contains the code for testing the accuracy of the Machine Learning model over the created dataset.

--------------------------------------------------------------------------------------------------------------------------------------

Equipment Used:

Five flex sensors, One Gyroscpe (MPU6050), Five 10K ohm Resistors, Arduino Nano board, A comfortable glove, Jumper wires, Breadboard.

--------------------------------------------------------------------------------------------------------------------------------------

Arrangement:  

The flex sensors and the gyroscope are mounted on top of the glove. They will have unique values for each gesture due to the change in orientation of the hand and the bending of the fingers. These are all connected to the Arduino Nano board through the breadboard as shown in the Circuit Diagram photo. The Arduino Nano board is connected to the laptop using a data transmission cable. 
