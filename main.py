import pymongo

# Connect to MongoDB (replace "localhost" and "27017" if using a different host or port)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the database (will be created if it doesn't exist)
database = client["neurolabDB"]

# Access the collection (will be created if it doesn't exist)
collection = database["Products"]

# Document to insert
document = {
    'companyName': 'iNeuron',
    'product': 'Affordable AI',
    'courseOffered': 'Machine Learning'
}

# Insert the document into the collection
result = collection.insert_one(document)
print(f"Inserted document ID: {result.inserted_id}")

# Retrieve and display all documents in the collection
all_records = collection.find()

print("All records in the collection:")
for idx, record in enumerate(all_records):
    print(f"{idx} : {record}")