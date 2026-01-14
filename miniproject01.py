#builting a small school website for student details and student information all curriculum maintaince for any school,college or institution
#Welcome To XYZ School---
#1) To Get Student Details
#2) To Add New Student
#3) To Remove Student
#4) To Update Student Details
#5) To Update School Name
#6) To Get Number Of Students In School
#7) To Get All Student Details
#8) To Get Any Class Student Details

class student:
    School_Name = "XYZ SCHOOL"
    student_count = 0
    student_list = []
#initializing the student details
    def __init__(self):
        self.student_name = input("Enter Student Name:")
        self.Roll_no = int(input("Enter the Roll NUmber:"))
        self.class_name = input("Enter the class name:")
        self.phone_number = int(input("Enter the Phone Number:"))
        self.address = input("Enter the Address:")
#to get the student details with the help of roll number
    def get_student_details(self,roll_no):
     if self.Roll_no == roll_no:
       return (f"Student Name:{self.student_name},Student Roll No:{self.Roll_no},Student Class Name:{self.class_name},Student Phone Number:{self.phone_number},Student Address:{self.address}")
     else:
        return "Student Not Found"
#To add new student details
    def add_new_student(self):
        new_student = student()
        return new_student
#To remove student details with the help of roll number
    def remove_student(self,roll_no):
        if self.Roll_no == roll_no:
            del self
            return "student removed successfully"
        else:
            return "Student Not Found"
#To update student details with the help of roll number
    def update_student_details(self, roll_no):
        if self.Roll_no == roll_no:
            self.student_name = input("Enter the Student Name:")
            self.class_name = input("Enter the Class Name:")
            self.phone_number = int(input("Enter the phone Number:"))
            self.address = input("Enter the Address:")
            return "Student Details Updated Successfully"
        else:
            return "student Not Found"
#To update School Name
    @classmethod
    def update_school_name(cls,new_name):
        cls.School_name = new_name
        return "School Name Updated Successfully"
#To get number of students in school
    @classmethod
    def get_number_of_students(cls):
        return cls.student_count
#To get all students details
    @classmethod
    def get_all_students_details(cls):
        all_students = []
        for student in cls.student_list:
            all_students.append(student.get_student_details(student.Roll_no))
        return all_students
# To get any class student details
    @classmethod
    def get_class_student_details(cls,class_name):
        class_students =  []
        for student in cls.student_list:
            if student.class_name == class_name:
                class_students.append(student.get_student_details(student.Roll_no))
                return class_students
            return "No students found in this class"
#main function
def main():
    while True:
        print(f"Welcome To {student.School_Name}")
        print("1) To Get Student Details")
        print("2) To Add New Student")
        print("3) To Remove Student")
        print("4) To Update Student Details")
        print("5) To Update School Name")
        print("6) To Get Number Of Students In School")
        print("7) To Get All Student Details")
        print("8) To Get Any Class Student Details")
        print("9) To Exit")
        choice = int(input("Enter Your Choice:"))
        if choice == 1:
            roll_no = int(input("Enter the Roll Number:"))
            found = False
            for student in student.student_list:
                details = student.get_student_details(roll_no)
                if details != "Student Not Found":
                    print(details)
                    found = True
                    break
            if not found:
                print("Student Not Found")
        elif choice == 2:
            new_student = student().add_new_student()
            student.student_list.append(new_student)
            student.student_count += 1
            print("Student Added Successfully")
        elif choice == 3:
            roll_no = int(input("Enter the Roll Number:"))
            found = False
            for student in student.student_list:
                result = student.remove_student(roll_no)
                if result == "student removed successfully":
                    student.student_list.remove(student)
                    student.student_count -= 1
                    print(result)
                    found = True
                    break
            if not found:
                print("Student Not Found")
        elif choice == 4:
            roll_no = int(input("Enter the Roll Number:"))
            found = False
            for student in student.student_list:
                result = student.update_student_details(roll_no)
                if result != "student Not Found":
                    print(result)
                    found = True
                    break
            if not found:
                print("Student Not Found")
        elif choice == 5:
            new_name = input("Enter the New School Name:")
            result = student.update_school_name(new_name)
            print(result)
        elif choice == 6:
            count = student.get_number_of_students()
            print(f"Number of Students in School: {count}")
        elif choice == 7:
            all_students = student.get_all_students_details()
            for details in all_students:
                print(details)
        elif choice == 8:
            class_name = input("Enter the class name:")
            class_students= student.get_class_student_details(class_name)
            if class_students != "No students found in this class":
                for details in class_students:
                    print(details)
            else:
                print(class_students)
