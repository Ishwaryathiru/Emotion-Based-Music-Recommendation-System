import tensorflow as tf
import keras
import os
import cv2
import random
from tensorflow import keras
from keras import layers
import numpy as np
import matplotlib.pyplot as plt

path = "haarcascade_frontalface_default.xml"
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

rectangle_bgr = (255, 255, 255)

img = np.zeros((500, 500))

text = "Some text in a box!"

(text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]

text_offset_x = 10
text_offset_y = img.shape[0] - 25

box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height - 2))
cv2.rectangle(img, box_coords[0], box_coords [1], rectangle_bgr, cv2. FILLED)
cv2. putText(img, text, (text_offset_x, text_offset_y), font, fontScale=font_scale, color=(0, 0, 0), thickness=1)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import webbrowser
import time

def camera_module():
    hap = sad = sur = dis = ang = neut = 0
    cap = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    flag=0
    emote="neutral"
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        face_roi = None

        for x, y, w, h in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            facess = faceCascade.detectMultiScale(roi_gray)

            for (ex, ey, ew, eh) in facess:
                face_roi = roi_color[ey: ey+eh, ex:ex + ew]

        if face_roi is not None:
            final_image = cv2.resize(face_roi, (224, 224))
            final_image = np.expand_dims(final_image, axis=0)
            final_image = final_image / 255.0

            new_model = tf.keras.models.load_model('final_model_ishu1.h5')

            prediction = new_model.predict(final_image)

            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1.5

            if np.argmax(prediction) == 3:
                status = "happy"
                hap += 1
            elif np.argmax(prediction) == 5:
                status = "sad"
                sad += 1
            elif np.argmax(prediction) == 6:
                status = "surprise"
                sur += 1
            elif np.argmax(prediction) == 1:
                status = "disgust"
                dis += 1
            elif np.argmax(prediction) == 0:
                status = "angry"
                ang += 1
            else:
                status = "neutral"
                neut += 1
            print(status)

            if(hap>5 or sad>5 or sur>5 or dis>5 or ang>5 or neut>5):
                # flag=1
                emote=status
                cv2.putText(frame, emote, (100, 150), font, 3, (0, 0, 255), 2, cv2.LINE_4)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

                if(emote=="angry"):
                    lz_uri = 'spotify:artist:6AiX12wXdXFoGJ2vk8zBjy' #yuvan

                    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='5a58176dab9b49c9a1467f0e4a92763f',client_secret='666f8bedbdfe4c7f8400dda9b78ed039'))
                    results = spotify.artist_top_tracks(lz_uri)

                    aud=[]
                    for track in results['tracks'][:2]:
                        aud.append(track['preview_url'])

                    random.shuffle(aud)

                    for i in aud:
                        webbrowser.open(i)
                        print(i)
                        time.sleep(30)
                elif(emote=="happy" or emote=="surprise"):
                    lz_uri = 'spotify:artist:3m49WVMU4zCkaVEKb8kFW7' #illaiyaraja

                    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='5a58176dab9b49c9a1467f0e4a92763f',client_secret='666f8bedbdfe4c7f8400dda9b78ed039'))
                    results = spotify.artist_top_tracks(lz_uri)

                    aud=[]
                    for track in results['tracks'][:2]:
                        aud.append(track['preview_url'])

                    random.shuffle(aud)

                    for i in aud:
                        webbrowser.open(i)
                        print(i)
                        time.sleep(30)
                elif(emote=="sad" or emote=="neutral"):
                 
                        lz_uri = 'spotify:artist:6HtEIJH43LAZGQx6iNCqhg' #ganabala

                        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='5a58176dab9b49c9a1467f0e4a92763f',client_secret='666f8bedbdfe4c7f8400dda9b78ed039'))
                        results = spotify.artist_top_tracks(lz_uri)
                        aud=[]
                        for track in results['tracks'][:2]:
                            aud.append(track['preview_url'])
                            random.shuffle(aud)
                        for i in aud:
                            webbrowser.open(i)
                            print(i)
                            time.sleep(30)
                hap = sad = sur = dis = ang = neut = 0
                    
        cv2.imshow("Face emotion", frame)
        k = cv2.waitKey(10)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

camera_module()

