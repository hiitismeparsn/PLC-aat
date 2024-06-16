import numpy as np
import generate_embeddings as gm
from imgbeddings import imgbeddings
from PIL import Image

def embeddings(file):
    emb = imgbeddings()  # Start the embeder
    img = Image.open(file)  # Open the file as numpy array
    vector_embeddings = emb.to_embeddings(img)
    return vector_embeddings

def euclidean_distance(embedding1, embedding2):
    # Compute Euclidean distance between embeddings
    distance = np.linalg.norm(embedding1 - embedding2)
    return distance

def match(face1, face2, threshold):
    # Get embeddings for the faces
    
    # Compute Euclidean distance between the embeddings
    distance = euclidean_distance(face1, face2)
    
    # Check if distance is below threshold
    if distance < threshold:
        return True
    else:
        return False

def to_array(embedding):
    flattened = []
    for i in range(len(embedding)):
        for j in range(len(embedding[i])):  
            flattened.append(float(embedding[i][j]))
    return(flattened)



