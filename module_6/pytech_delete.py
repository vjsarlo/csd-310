from pymongo import MongoClient

url = "mongodb+srv://admin:admin@sarlo-assignment4-2.5vuly.mongodb.net/pytech"

client = MongoClient(url, ssl=True,ssl_cert_reqs='CERT_NONE')

db = client.pytech


#Find() method 
docs = db.students.find({})

print(f'-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

for doc in docs:
   print(f'Student ID: {doc["student_id"]}')
   print(f'First Name: {doc["first_name"]}')
   print(f'Last Name: {doc["last_name"]}\n')

# Insert_one student_id 1010

print("\n-- INSERT STATEMENTS --")

def insert_student(student):
    student_doc_id = db.students.insert_one(student).inserted_id
    print(f"Inserted student record into the student's collection with document_id {student_doc_id}\n")

student_1010 = {
    "student_id": "1010",
    "first_name": "Black",
    "last_name": "Widow",
    "enrollment": [],
    "courses": []
}
 
insert_student(student_1010)

#Find_one() method new_student_id


doc = db.students.find_one({"student_id": "1010"})

print(f'-- DISPLAYING STUDENT TEST DOC --')
print(f'Student ID: {doc["student_id"]}')
print(f'First Name: {doc["first_name"]}')
print(f'Last Name: {doc["last_name"]}\n')

#Delete student_1010

result = db.students.delete_one({"student_id": "1010"})

#Find() method after delete
docs = db.students.find({})

print(f'-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

for doc in docs:
   print(f'Student ID: {doc["student_id"]}')
   print(f'First Name: {doc["first_name"]}')
   print(f'Last Name: {doc["last_name"]}\n')

print(f'\nEnd of program, press any key to continue . . . \n')
