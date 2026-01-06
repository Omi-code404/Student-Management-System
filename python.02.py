a = 'Global'

def outer():
    a = 'Enclosing'
    
    def inner():
        a = 'Local'
        print(f"Problem 9 - Local: {a}")
    
    inner()
    print(f"Problem 9 - Enclosing: {a}")

outer()
print(f"Problem 9 - Global: {a}")