people = [
    {"name" : "John", "house" : "Gryffindor"},
    {"name" : "Jane", "house" : "Ravenclaw"},
    {"name" : "Jack", "house" : "Gryffindor"},
    {"name" : "Tim", "house" : "Slytherin"}
]

#def f(person):
#    return person["name"]
#people.sort(key=f)

people.sort(key=lambda person:person["name"])

print(people)
