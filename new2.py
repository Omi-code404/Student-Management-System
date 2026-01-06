def show_name(func):
    def wrapper():
        print(f"ফাংশনের নাম: {func.__name__}")
        func()
    return wrapper

@show_name
def student_info():
    print("আমার নাম আরিফ")

student_info()