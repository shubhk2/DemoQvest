from pymongo import MongoClient

# Replace this with your actual MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://mongo:shubhk2004@cluster0.mj3tg8t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(MONGO_URI)
    db = client.get_database("QuanvestDB")  # Name of your database (it will be auto-created)
    print("Connected to MongoDB successfully!")

    # Create a collection (like a table in SQL)
    collection = db["companies"]

    # Insert a test document
    sample_data = {"company_name": "TCS", "sector": "IT", "market_cap": "₹13.5T"}
    collection.insert_one(sample_data)

    print("Inserted test data into MongoDB!")

except Exception as e:
    print(f"Error: {e}")
