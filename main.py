import recognise_face
import generate_embeddings as ge
import DBMS
import os

#recognise_face.recognise('fdir\kkjx4jc9.bmp', 'fdir')
#print(ge.embeddings('fdir/face1.jpg'))


DBMS.mark_attendance(ge.embeddings('fdir/face1.jpg'), '07/19/2024')
