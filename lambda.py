people = [
    {"name" : "John", "house" : "Gryffindor"},
    {"name" : "Jane", "house" : "Ravenclaw"},
    {"name" : "Jack", "house" : "Gryffindor"},
    {"name" : "Tim", "house" : "Slytherin"}
]

#def f(dog):
#    return dog["name"]

people.sort(key=lambda person:person["name"])

print(people)