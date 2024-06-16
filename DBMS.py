import firebase_admin
from firebase_admin import credentials, firestore
import numpy as np
import embeddings as emb
# Function to add a user with input from the user
def add_user_with_input(name, fac_emb):

    # Reference to the 'users' collection and the document
    doc_ref = db.collection('Facial Embedddings').document()

    # Set data for the document using user input
    doc_ref.set({
        'name': name,
        'Facial Embedding': fac_emb
    })
    print("User added")

# Read data (Retrieve)
def read_users():
    users_ref = db.collection('Facial Embedddings')
    docs = users_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def get_facial_embeddings():
    facial_embeddings_ref = db.collection('Facial Embedddings')
    docs = facial_embeddings_ref.stream()
    embeddings = {doc.id: doc.to_dict() for doc in docs}
    return embeddings


# Function to print all attendance records
def print_attendance_records():
    attendance_ref = db.collection('Attendance')
    docs = attendance_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

# Function to convert string representation of embedding to list of floats
def convert_embedding(embedding_str):
    # Remove whitespace and brackets, then split by commas
    embedding_list = embedding_str.replace('[', '').replace(']', '').split(',')
    # Convert to list of floats
    list = []
    for num in embedding_list:
        list.append(num)

    return list



# Function to mark attendance
def mark_attendance(input_embedding, date):
    embeddings = get_facial_embeddings()
    attendance_ref = db.collection('Attendance')

    input_embedding_np = np.array(input_embedding, dtype=np.float32)  # Convert input embedding to numpy array

    
    for student_id, data in embeddings.items():
        print('hi')
        print(f"Student ID: {student_id}, Data: {data}")  # Debug print to check document structure
        if 'Facial Embedding' not in data:
            print(f"Warning: No 'Facial Embedding' key found in document for student ID {student_id}")
            continue

        stored_embedding_str = data['Facial Embedding']
        stored_embedding = convert_embedding(stored_embedding_str)
        print(stored_embedding)
        print(type(stored_embedding[0]))
          # Convert stored embedding to list of floats
        stored_embedding_np = np.array(stored_embedding)  # Convert to numpy array

        # Check if embedding is present in the DB

        if emb.match(stored_embedding_np, input_embedding_np, 12):
            attendance_ref.document(student_id).set({
                'name': data['name'],
                'status': 'present',
                'date': date
                
            })
            print('hi')
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


