# Dictionary
students = {"Alice": 23, "Bob": 25, "Clair": 25}
print(students.items())

# Dictionary in Dictionary
students_1 = {
            "Alice": {"id": "ID0001", "age": 26, "grade": "A"},
            "Bob": {"id": "ID0002", "age": 27, "grade": "B"},
            "Claire": {"id": "ID0003", "age": 17, "grade": "C"},
            "Dan": {"id": "ID0004", "age": 21, "grade": "D"},
            "Emma": {"id": "ID0005", "age": 22, "grade": "E"}
            }

print(students_1["Dan"]["age"])

print(students_1["Emma"]["id"], students_1["Emma"]["grade"])

# List in dictionary
students_2 = {
            "Alice": ["ID0001", 23, "A"],
            "Bob": ["ID0002", 33, "B"],
            "Claire": ["ID0003", 14, "C"],
            "Dan": ["ID0004", 15, "D"],
            "Emma": ["ID0005", 22, "E"]
            }

print(students_2["Dan"][0])

print(students_2["Alice"][1:])

