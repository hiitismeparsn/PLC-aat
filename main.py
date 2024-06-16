import recognise_face
import generate_embeddings as ge
import DBMS as db
import os
import embeddings 
import numpy as np

"""
Flow of program.

1. Recognice faces and create subpicures
2. Create embeddings for those faces
3. Upload into the database and create a document for each known face
4. Recieve a new face and repeat the process till creating embeddings. 
5. Compair the input vector embeddings to known using euclidian distance 
6. Increment the attendence for that student in the attendence collection. 
"""


fileToMark = input("Enter the file you want to mark attendence for: ")
date = input("Enter date of attendence: ")

recognise_face.recognise(fileToMark, 'fdir')

db.add_user_with_input("Halie",embeddings.to_array(ge.embeddings('fdir/face1.jpg')))
db.add_user_with_input("Claire",embeddings.to_array(ge.embeddings('fdir/face2.jpg')))
db.add_user_with_input("Alex",embeddings.to_array(ge.embeddings('fdir/face3.jpg')))
db.add_user_with_input("Luke",embeddings.to_array(ge.embeddings('fdir/face4.jpg')))
db.add_user_with_input("Phill",embeddings.to_array(ge.embeddings('fdir/face5.jpg')))



recognise_face.recognise(fileToMark, 'test')
db.mark_attendance(ge.embeddings(fileToMark), date)