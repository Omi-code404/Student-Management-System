def create_student(name):
    marks = 0
    print(f"ছাত্রের নাম: {name}")
    def add_mark(mark):
        nonlocal marks
        marks += mark
        return f" মোট মার্ক: {marks}"
    
    return add_mark

student1 = create_student("আরিফ")
print(student1(80))
print(student1(85))
print(student1(90))