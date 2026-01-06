def greet_person(name):
    def greet():
        print(f"hallo ich bin , {name}!")
    return greet
greet_Arif = greet_person("Arif")
greet_Fatima = greet_person("Fatima")
greet_Arif()
greet_Fatima()

