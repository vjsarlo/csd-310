from pymongo import MongoClient

url = "mongodb+srv://admin:admin@sarlo-assignment4-2.5vuly.mongodb.net/pytech"

client = MongoClient(url, ssl=True,ssl_cert_reqs='CERT_NONE')

db = client.pytech

student_collection = db.students


print("\n- - INSERT STATEMENTS - -")

def insert_student(student):
    student_doc_id = student_collection.insert_one(student).inserted_id
    student_name = f'{student["first_name"]} {student["last_name"]}'
    print(f"Inserted student record {student_name} into the student's collection with document_id {student_doc_id}")


student_1007 = {
    "student_id": "1007",
    "first_name": "Thor",
    "last_name": "Odinson",
    "enrollment": [],
    "courses": []
}
insert_student(student_1007)

student_1008 = {
    "student_id": "1008",
    "first_name": "Steve",
    "last_name": "Rodgers",
    "enrollment": [],
    "courses": []
}
insert_student(student_1008)

student_1009 = {
    "student_id": "1009",
    "first_name": "Tony",
    "last_name": "Stark",
    "enrollment": [],
    "courses": []
}
insert_student(student_1009)

print("\n\nEnd of program, press any key to exit . . .\n")