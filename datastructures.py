# Tuples
cars = ("Limo","Ranger",1200,"mazda",10.5)
print(cars[1])
print(cars[0:3])
for gari in cars:
    print(gari)

# List
students = ["Moses","June","Chris","Delphine"]
print(students[1])
print(students[0:4])
students[2] = "Christopher"
students.append("Francis")
for jina in students:
    print(jina)
# Dictionaries
pupils = {"STD1":"shemaiyah","STD2":"Sylvanus"}
print(pupils["STD2"])

for pupils in pupils.keys():
    print(pupils)

for pupils in pupils.values():
    print(pupils)