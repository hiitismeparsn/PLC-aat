import firebase_admin
from firebase_admin import credentials, firestore
import numpy as np
import embeddings as emb
# Function to add a user with input from the user
def add_user_with_input(name: str, fac_emb: list):
    # Reference to the 'users' collection and the document
    doc_ref = db.collection('Facial Embeddings').document()

    # Set data for the document using user input
    doc_ref.set({
        'name': name,
        'Facial Embedding': fac_emb
    })
    print("User added")

# Read data 
def read_users():
    doc_list = []
    users_ref = db.collection('Facial Embeddings')
    docs = users_ref.stream()
    for doc in docs:
        doc.to_dict()
        data = {}
        data['id'] = doc.id
        data['data'] = doc._data
        doc_list.append(data)
        #print(f"\n\n\n {doc.id} \n \n  {doc._data} \n\n\n")

    return doc_list


def get_facial_embeddings():
    users_ref = db.collection("Facial Embeddings")
    docs = users_ref.stream()
    allEmbed = []
    for doc in docs:
        val = doc.to_dict()
        allEmbed.append(val['Facial Embedding'])
    return allEmbed







# Function to print all attendance records
def print_attendance_records():
    attendance_ref = db.collection('Attendance')
    docs = attendance_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

# Function to convert string representation of embedding to list of floats



# Function to mark attendance
def mark_attendance(input_embedding: list, date: str):
    embeddings = read_users()
    attendance_ref = db.collection('Attendance')

    input_embedding_np = np.array(input_embedding, dtype=np.float32)  # Convert input embedding to numpy array

    for item in embeddings:
        student_id = item['id']
        data = item['data']

        stored_embedding_str = data['Facial Embedding']


        # Convert stored embedding to list of floats
        stored_embedding_np = np.array(stored_embedding_str)  # Convert to numpy array

         # Check if embedding is present in the DB

        if emb.match(stored_embedding_np, input_embedding_np, 12):
            attendance_ref.document(student_id).set({
                'name': data['name'],
                'status': 'present',
                'date': date
                    
            })
            print(f"Match found to: {data['name']}")
    #print(f"Marked attendance for: {data['name']}, for {date}")
 





# Use the service account key file
cred = credentials.Certificate('privateKey.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()


# Initialize Firestore
db = firestore.client()
print("Firestore has been initialized.")


# Check if the Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase with the service account key file
    firebase_admin.initialize_app(cred)
    print("Firebase Admin SDK has been initialized.")
else:
    print("Firebase Admin SDK is already initialized.")


