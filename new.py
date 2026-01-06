def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Positional args: {args}")
        print(f"Keyword args: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    else:
        return a - b

# Test:
result = calculate(10, 5, operation="subtract")
print(f"Result: {result}")
