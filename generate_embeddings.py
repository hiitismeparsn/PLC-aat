from imgbeddings import imgbeddings
from PIL import Image

def embeddings(file):
    emb = imgbeddings()  # Start the embeder
    img = Image.open(file)  # Open the file as numpy array
    vector_embeddings = emb.to_embeddings(img)
    return vector_embeddings

def to_array(embedding):
    flattened = []
    for i in range(len(embedding)):
        for j in range(len(embedding[i])):  
            flattened.append(float(embedding[i][j]))
    return(flattened)