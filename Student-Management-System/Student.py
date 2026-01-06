from typing import Optional, List

class Student:
    """Student class: stores and manages student information"""

    def __init__(self, **details):
        """
        Constructor: initializes student information

        Args:
            **details: student details (roll, name, marks, department)
                      - marks should be a list of 5 subject marks
        """
        self.roll: Optional[int] = details.get("roll", None)
        self.name: str = details.get("name", "Unknown")
        self.marks: List[float] = details.get("marks", [0.0, 0.0, 0.0, 0.0, 0.0])
        self.department: str = details.get("department", "General")

    def average_marks(self) -> float:
        """Calculate and return the average of all subjects"""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def get_grade(self) -> str:
        """
        Determine grade based on average marks

        Returns:
            Grade as a string (A+, A, A-, B, C, D, F)
        """
        avg = self.average_marks()
        if avg >= 80:
            return "A+"
        elif avg >= 70:
            return "A"
        elif avg >= 60:
            return "A-"
        elif avg >= 50:
            return "B"
        elif avg >= 45:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def get_info(self) -> str:
        """Return complete student information including average and grade"""
        return (
            f"Roll: {self.roll}, "
            f"Name: {self.name}, "
            f"Marks: {self.marks},"
            f"Department: {self.department}, "
        )

    def update(self, **details) -> None:
        """
        Update student information

        Args:
            **details: fields to update (name, marks, department)
                      - marks should be a list of 5 subject marks if provided
        """
        if "roll" in details:
            self.roll = details["roll"]
        if "name" in details:
            self.name = details["name"]
        if "marks" in details:
            self.marks = self._to_float(details["marks"])
        if "department" in details:
            self.department = details["department"]
