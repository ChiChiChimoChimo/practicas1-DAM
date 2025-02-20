# dictionary = a collection of {key:value} pairs
#              ordered and changeable. NO duplicates

capitals = {"USA":"Washington DC",
            "France":"Paris", 
            "UK":"London",
            "China":"Beijing"}

# print(dir(capitals))
# print(help(capitals))

capitals.update({"Germany":"Berlin"})
capitals["China"] = "Shanghai"
del capitals["France"]
capitals.clear()
keys = capitals.keys()
values = capitals.values()
items = capitals.items()