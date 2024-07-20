import csv
import random
class Generate_Data:
    def __init__(self) -> None:
        # Set to store generated student IDs and course IDs
        self.generated_student_ids = set()
        self.generated_course_ids = set()
    def generate_student_id(self):
        student_id = 'EHIST' + str(random.randint(1000, 9999))
        while student_id in self.generated_student_ids:
            student_id = 'EHIST' + str(random.randint(1000, 9999))
        self.generated_student_ids.add(student_id)
        return student_id
    # Function to generate random course IDs
    def generate_course_id(self):
        course_id = 'EHIST' + str(random.randint(10, 99))
        while course_id in self.generated_course_ids:
            course_id = 'EHIST' + str(random.randint(10, 99))
        self.generated_course_ids.add(course_id)
        return course_id
    # Generate courses data
    def generate_courses(self, num_courses):
        courses = [["course_id", "name", 'lecturer', "credits"]]
        for _ in range(num_courses):
            course_id = self.generate_course_id()
            course_name = f"Course_{course_id}"
            course_lecturer = f"lecturer_{course_id}"
            credits = random.randint(1, 5)
            courses.append([course_id, course_name, course_lecturer, credits])
        return courses
    # Generate students data
    def generate_students(self, num_students):
        students = [["student_id", "name", "age"]]
        for _ in range(num_students):
            student_id = self.generate_student_id()
            student_name = f"Student_{student_id}"
            age = random.randint(18, 25)
            students.append([student_id, student_name, age])
        return students
    # Generate grades data
    def generate_grades(self, students, courses):
        grades = [["student_id", "course_id", "grade"]]
        for student in students[1:]: # Skip headers
            student_id = student[0]
            for course in courses[1:]: # Skip headers
                course_id = course[0]
                grade = random.randint(20, 100)
                grades.append([student_id, course_id, grade])
        return grades
    # Write data to CSV files
    def write_to_csv(self, data, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

        