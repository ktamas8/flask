thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
thisdict.pop("model")

for x in thisdict.items():
  print(x)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(dict(myfamily))

for x in myfamily.items():
    print(x)

print(myfamily["child1"]["year"])
print(myfamily["child2"])

child1 = { "name" : "Emil", "year" : 2004 }
child2 = { "name" : "Tobias", "year" : 2007 }
child3 = { "name" : "Linus", "year" : 2011 }

myfamily = {1:child1,2:child2,3:child3}
print(myfamily)
for x in myfamily.items():
    print(x(name))

# https://www.w3schools.com/python/python_dictionaries.asp
# https://www.tutorialspoint.com/How-to-declare-a-multi-dimensional-dictionary-in-Python
