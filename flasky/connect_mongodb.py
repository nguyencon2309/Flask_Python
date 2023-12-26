
from pymongo import MongoClient 

# root route 


# Set up MongoDB connection and collection 
client = MongoClient('mongodb://localhost:27017/') 

# Create database named demo if they don't exist already 
db = client['db_flask'] 

col_employee = db['employee']#get collection employee
col_dep = db['department']#get collection department
col_user = db['users']
