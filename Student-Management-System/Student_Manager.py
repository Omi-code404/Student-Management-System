from typing import List
from Student import Student 


class StudentManager:
    """Student management system"""
    
    def __init__(self):
        """Constructor : initialize the students list"""
        self.student: List[Student] = []
    
    def add_student(self, **details) -> str:
        """
        Add a new student
        
        Args:
            **details: student information
        
        Returns:
            Success message
        
        Raises:
            ValueError: if roll number is duplicate
        """
        try:
            roll = details.get("roll")
            
            if roll is None:
                raise ValueError("Roll number is required!")
            
            # Check if the roll already exists
            for student in self.student:
                if student.roll == roll:
                    raise ValueError(f"Roll {roll} already exists!")
            
            # Create new student
            student = Student(**details)
            self.student.append(student)
            
            return f"Student added successfully: {student.name} (Roll: {roll})"
        
        except ValueError as e:
            return f"Error: {e}"
    
    def remove_student(self, roll: int) -> str:
        """Remove a student by roll number"""
        try:
            for i, student in enumerate(self.students):
                if student.roll == roll:
                    removed_name = student.name
                    self.student.pop(i)
                    return f"Student removed successfully: {removed_name}"
            
            return f"Error: Roll {roll} not found!"
        
        except Exception: 
            return f"Error: Roll not found!"
    
    def update_student(self, roll: int, **details) -> str:
        """Update a student's information by roll number"""
        try:
            for student in self.student:
                if student.roll == roll:
                    student.update(**details)
                    return f"Student updated successfully: {student.name}"
            
            return f"Error: Roll {roll} not found!"
        
        except Exception as e:
            return f"Error: {e}"
    
    def search_student(self, roll: int) -> str:
        """Search for a student by roll number"""
        try:
            for student in self.student:
                if student.roll == roll:
                    avg_marks = student.average_marks()
                    return (
                        f"Student found:\n"
                        f"  {student.get_info()}\n"
                        f"  Average Marks: {avg_marks:.2f}\n"
                        f"  Grade: {student.get_grade()}"
                    )
            
            return f"Error: Roll {roll} not found!"
        
        except Exception as e:
            return f"Error: {e}"
    
    def search_by_name(self, name: str) -> str:
        """Search for students by full name (case-insensitive)"""
        try:
            found = []
            for student in self.students:
                if student.name.lower() == name.lower():
                    found.append(student)
            
            if found:
                result = f"Search results for '{name}':\n"
                for student in found:
                    result += f"{student.get_info()}\n"
                return result
            
            return f"Error: Name '{name}' not found!"
        
        except Exception as e:
            return f"Error: {e}"
    
    def get_all_students(self) -> str:
        """Display information of all students"""
        if not self.student:
            return "No students found!"
        
        result = "\nAll Students:\n"
        for student in self.student:
            result += f"  {student.get_info()} | Average: {student.average_marks():.2f} | Grade: {student.get_grade()}\n"
        
        return result
    
    def get_statistics(self) -> str:
        """Calculate average marks across all students and total student count"""
        if not self.student:
            return "No students found!"
        
        total_avg_marks = sum(student.average_marks() for student in self.student)
        average_marks = total_avg_marks / len(self.student)
        
        result = f"\nAverage Marks of Class: {average_marks:.2f}\n"
        result += f"{Student.get_info()} | Average: {Student.average_marks():.2f} | Grade: {Student.get_grade()}\n"
        
        return result
