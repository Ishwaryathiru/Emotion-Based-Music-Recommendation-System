**EMOTION BASED MUSIC RECOMMENDATION SYSTEM**

**ABOUT**

This project aims to recognize human emotions using facial expression analysis and provide real-time music recommendations based on the detected emotion. 
It utilizes a convolutional neural network (CNN) model trained to classify emotions such as happiness, sadness, surprise, disgust, anger, and neutrality. 
The facial expression recognition is performed using OpenCV and Haar cascades for face detection. 

**Features:**

Real-time Emotion Detection        : The application detects emotions in real-time through webcam feed.

Multi-class Emotion Classification : Emotions such as happiness, sadness, surprise, disgust, anger, and neutrality are classified using a pre-trained CNN model.

Dynamic Music Recommendations      : Based on the detected emotion, the system dynamically recommends playlists from Spotify corresponding to the user's emotional state.

Interactive Web Interface          : Users can interact with the system through a web interface to view recommended playlists.

**Technologies Used:**

Python : OpenCV, TensorFlow, Keras, Spotipy (Spotify API wrapper)

HTML, CSS, JavaScript : Front-end for web interface

PHP : Backend script for executing Python code

**EmotionalAi.ipynb**

DATA SET       : https://www.kaggle.com/datasets/msambare/fer2013

METHODOLOGY    : Transfer Learning

MODEL USED     : MobilenNtV2

EPOCHS         : 8

ACCURACY       : 72.95% (With increase in epochs you can achieve more than 90% of accuracy)

LIBRARIES USED : tensorflow, keras, os, cv2, random, from keras layers, numpy
              
You will be able to see the trained model in the below drive link

ACCURACY : 72%

https://drive.google.com/file/d/1b0LwjEisTNShn4kAbmUh3ehk7toHDShE/view?usp=drive_link 

ACCURACY : 82%

https://drive.google.com/file/d/1Sjc-S9NEDP9bYcXyCgq5xyeO4vDj5hOe/view?usp=sharing

If you are making use of this make a change in emotionrecoginzewithtime.py in the line 

new_model = tf.keras.models.load_model('final_model_ishu2.h5')

**emotionrecognisewithtime.py**

It initializes a video capture object using OpenCV to capture frames from the webcam.

It loads a pre-trained face detection model called 'haarcascade_frontalface_default.xml' using OpenCV's CascadeClassifier.

It continuously captures frames from the webcam, detects faces in each frame, and extracts the region of interest (ROI) containing the face.

It resizes the face ROI to 224x224 (required input size for the pre-trained model), preprocesses the image, and feeds it into a pre-trained emotion detection model ('final_model_ishu1.h5').

It interprets the model predictions to recognize the emotion (happy, sad, surprise, disgust, angry, or neutral) based on the highest predicted probability.

If a certain emotion is detected for more than 5 consecutive frames, it triggers actions accordingly:

If the emotion is 'angry', it retrieves and plays two preview tracks from the artist Yuvan Shankar Raja using the Spotify API.

If the emotion is 'happy' or 'surprise', it retrieves and plays two preview tracks from the artist Ilaiyaraaja.

If the emotion is 'sad' or 'neutral', it retrieves and plays two preview tracks from the artist Gaana Bala.

After triggering the action for an emotion, it resets the emotion counters to zero.

The function also displays the webcam feed with detected faces and emotion labels in real-time. Pressing 'q' will exit the loop and close the webcam feed.

**NOTE:**
1. Provide your Spotify API credentials (client ID and client secret) 
2. Run the emotionrecognisewithtime.py in your local host and copy paste the localhost link in the script part of home.html
3. Install the recommended libraries
