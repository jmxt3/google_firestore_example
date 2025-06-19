import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import FieldFilter

# Use the application default credentials.
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred)
db = firestore.client(database_id="pixelwood")

def create_user(user_id, user_data):
    doc_ref = db.collection("users").document(user_id)
    doc_ref.set(user_data)
    print(f"Created user {user_id}")


def read_user(user_id):
    doc_ref = db.collection("users").document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        print(f"{doc.id} => {doc.to_dict()}")
        return doc.to_dict()
    else:
        print("No such document!")
        return None


def update_user(user_id, update_data):
    doc_ref = db.collection("users").document(user_id)
    doc_ref.update(update_data)
    print(f"Updated user {user_id}")


def delete_user(user_id):
    db.collection("users").document(user_id).delete()
    print(f"Deleted user {user_id}")


def list_users():
    users_ref = db.collection("users")
    docs = users_ref.stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")


def search_users_by_field(field, value):
    users_ref = db.collection("users")
    query = users_ref.where(filter=FieldFilter(field, "==", value))
    results = query.stream()
    found = False
    for doc in results:
        print(f"{doc.id} => {doc.to_dict()}")
        found = True
    if not found:
        print(f"No users found with {field} == {value}")

def delete_all_users():
    users_ref = db.collection("users")
    docs = users_ref.stream()
    count = 0
    for doc in docs:
        doc.reference.delete()
        count += 1
    print(f"Deleted {count} users.")

# Example usage:
delete_all_users()
create_user("ada", {"first": "Ada", "last": "Lovelace", "born": 1815})
create_user("babbage", {"first": "Charles", "last": "Babbage", "born": 1791})
create_user("turing", {"first": "Alan", "last": "Turing", "born": 1912})
create_user("hopper", {"first": "Grace", "last": "Hopper", "born": 1906})
create_user("eclarke", {"first": "Edith", "last": "Clarke", "born": 1883})
print("----------------------")
list_users()
print("----------------------")
read_user("eclarke")
update_user("eclarke", {"born": 1884})
list_users()
print("----------------------")
search_users_by_field("first", "Ada")
print("----------------------")
delete_user("ada")
list_users()