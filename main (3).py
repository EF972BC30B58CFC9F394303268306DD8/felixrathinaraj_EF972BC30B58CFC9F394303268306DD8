class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the list of students in descending order based on CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Test the function with sample student objects
if __name__ == "__main__":
  # Create a list of student objects
  students = [
      Student("Alice", "001", 3.8),
      Student("Bob", "002", 3.6),
      Student("Charlie", "003", 3.9),
      Student("David", "004", 3.7),
  ]

  # Sort the students by CGPA
  sorted_students = sort_students(students)

  # Print the sorted list
  for student in sorted_students:
      print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
