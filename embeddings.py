import numpy as np
from imgbeddings import imgbeddings
from PIL import Image

def embeddings(file: str):
    emb = imgbeddings()  # Start the embeder
    img = Image.open(file)  # Open the file as numpy array
    vector_embeddings = emb.to_embeddings(img)
    return vector_embeddings

def euclidean_distance(embedding1: list, embedding2: list):
    # Compute Euclidean distance between embeddings
    distance = np.linalg.norm(embedding1 - embedding2)
    return distance

def match(emb1: list, emb2: list, threshold: int):
    # Get embeddings for the faces
    
    # Compute Euclidean distance between the embeddings
    distance = euclidean_distance(emb1, emb2)
    print(f"Euclidian distance calculated was: {distance}")
    
    # Check if distance is below threshold
    if distance < threshold:
        return True
    else:
        return False

    

def to_array(embedding: list):
    flattened = []
    for i in range(len(embedding)):
        for j in range(len(embedding[i])):  
            flattened.append(float(embedding[i][j]))
    return(flattened)


