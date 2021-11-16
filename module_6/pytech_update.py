from pymongo import MongoClient

url = "mongodb+srv://admin:admin@sarlo-assignment4-2.5vuly.mongodb.net/pytech"

client = MongoClient(url, ssl=True,ssl_cert_reqs='CERT_NONE')

db = client.pytech

print(db.list_collection_names())

# find() method 
docs = db.students.find({})

print(f'-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

for doc in docs:
   print(f'Student ID: {doc["student_id"]}')
   print(f'First Name: {doc["first_name"]}')
   print(f'Last Name: {doc["last_name"]}\n')

#update_one() method
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Odinson II"}})


#print find_one() method

doc = db.students.find_one({"student_id": "1007"})

print(f'-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')
print(f'Student ID: {doc["student_id"]}')
print(f'First Name: {doc["first_name"]}')
print(f'Last Name: {doc["last_name"]}\n')

print(f'\nEnd of program, press any key to continue . . . \n')