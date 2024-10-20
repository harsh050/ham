import face_recognition
import os,sys
import cv2
import numpy as np
import math



def face_confidance(face_distance,face_match_threshold=0.6):
    range=(1.0-face_match_threshold)
    linear_value=(1.0-face_distance)/(range*2.0)
    
    if face_distance > face_match_threshold:
        return str(round(linear_value*100,2))+'%'
    else:
        value=(linear_value+((1.0-linear_value)*math.pow((linear_value-0.5)*2,0.2)))*100
        return str(round(value,2))+'%'
    
    
    class FaceRecognition:
        face_location=[]
        face_encodings=[]
        face_names=[]
        known_face_encoding=[]
        known_face_names=[]
        process_current_frame=True
        
        def __init__(self):
            self.encode_faces()        
        
        
        def encode_faces(self):
            for image in os.listdir('photo'):
                face_image=face_recognition.load_image_file(f'photo/{image}')
                face_encoding=face_recognition.face_encodings(face_image)[0]
                
                
                self.known_faces_encoding.append(face_encoding)
                self.known_faces_names.append(image)
            
            print(self.known_face_names)
            
            
    if __name__=='__main__' :     
        fr = FaceRecogniton()
    
            
            
        
        
    
    