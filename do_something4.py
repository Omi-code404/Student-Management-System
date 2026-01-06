def student_info(name,roll,gpa):
    """
    Docstring for student_inf0
    
    :param name: Description
    :param roll: Description
    :param gpa: Description
    """
    return f"Name :{name},Roll:{roll},GPA:{gpa}"
print(student_info("Arif",101,4.50))
print(f"Docstring: {student_info.__doc__}")
