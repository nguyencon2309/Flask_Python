
from pymongo import MongoClient 

# root route 


# Set up MongoDB connection and collection 
client = MongoClient('mongodb://localhost:27017/') 

# Create database named demo if they don't exist already 
db = client['db_flask'] 

# Create collection named data if it doesn't exist already 
collection = db['test'] 

col_employee = db['employee']
col_dep = db['department']
# for i in rs:
# 	print(i["text"])
