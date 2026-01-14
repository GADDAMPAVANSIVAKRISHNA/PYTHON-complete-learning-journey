"""class Student:
    School_Name = "XYZ SCHOOL"
    student_count = 0
    student_list = [] 

    # initializing the student details
    def __init__(self):
        self.student_name = input("Enter Student Name: ")
        self.Roll_no = int(input("Enter the Roll Number: "))
        self.class_name = input("Enter the class name: ")
        self.phone_number = int(input("Enter the Phone Number: "))
        self.address = input("Enter the Address: ")

    # to get the student details with the help of roll number
    def get_student_details(self, roll_no):
        if self.Roll_no == roll_no:
            return (f"Student Name: {self.student_name}, "
                    f"Student Roll No: {self.Roll_no}, "
                    f"Student Class Name: {self.class_name}, "
                    f"Student Phone Number: {self.phone_number}, "
                    f"Student Address: {self.address}")
        else:
            return "Student Not Found"

    # To add new student details
    @classmethod
    def add_new_student(cls):
        new_student = cls()
        cls.student_list.append(new_student)
        cls.student_count += 1
        return new_student

    # To remove student details with the help of roll number
    def remove_student(self, roll_no):
        if self.Roll_no == roll_no:
            return "student removed successfully"
        else:
            return "Student Not Found"

    # To update student details with the help of roll number
    def update_student_details(self, roll_no):
        if self.Roll_no == roll_no:
            self.student_name = input("Enter the Student Name: ")
            self.class_name = input("Enter the Class Name: ")
            self.phone_number = int(input("Enter the Phone Number: "))
            self.address = input("Enter the Address: ")
            return "Student Details Updated Successfully"
        else:
            return "student Not Found"

    # To update School Name
    @classmethod
    def update_school_name(cls, new_name):
        cls.School_Name = new_name
        return "School Name Updated Successfully"

    # To get number of students in school
    @classmethod
    def get_number_of_students(cls):
        return cls.student_count

    # To get all students details
    @classmethod
    def get_all_students_details(cls):
        all_students = []
        for stu in cls.student_list:
                all_students.append(stu.get_student_details(stu.Roll_no))
        return all_students

    # To get any class student details
    @classmethod
    def get_class_student_details(cls, class_name):
        class_students = []
        for stu in cls.student_list:
            if stu.class_name == class_name:
                class_students.append(stu.get_student_details(stu.Roll_no))
        if class_students:
            return class_students
        return "No students found in this class"


# main function
def main():
    while True:
        print(f"\nWelcome To {Student.School_Name}")
        print("1) To Get Student Details")
        print("2) To Add New Student")
        print("3) To Remove Student")
        print("4) To Update Student Details")
        print("5) To Update School Name")
        print("6) To Get Number Of Students In School")
        print("7) To Get All Student Details")
        print("8) To Get Any Class Student Details")
        print("9) To Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            roll_no = int(input("Enter the Roll Number: "))
            found = False
            for stu in Student.student_list:
                details = stu.get_student_details(roll_no)
                if details != "Student Not Found":
                    print(details)
                    found = True
                    break
            if not found:
                print("Student Not Found")

        elif choice == 2:
            Student.add_new_student()
            print("Student Added Successfully")

        elif choice == 3:
            roll_no = int(input("Enter the Roll Number: "))
            found = False
            for stu in Student.student_list:
                result = stu.remove_student(roll_no)
                if result == "student removed successfully":
                    Student.student_list.remove(stu)
                    Student.student_count -= 1
                    print(result)
                    found = True
                    break
            if not found:
                print("Student Not Found")

        elif choice == 4:
            roll_no = int(input("Enter the Roll Number: "))
            found = False
            for stu in Student.student_list:
                result = stu.update_student_details(roll_no)
                if result != "student Not Found":
                    print(result)
                    found = True
                    break
            if not found:
                print("Student Not Found")

        elif choice == 5:
            new_name = input("Enter the New School Name: ")
            result = Student.update_school_name(new_name)
            print(result)

        elif choice == 6:
            count = Student.get_number_of_students()
            print(f"Number of Students in School: {count}")

        elif choice == 7:
            all_students = Student.get_all_students_details()
            for details in all_students:
                print(details)

        elif choice == 8:
            class_name = input("Enter the class name: ")
            class_students = Student.get_class_student_details(class_name)
            if class_students != "No students found in this class":
                for details in class_students:
                    print(details)
            else:
                print(class_students)

        elif choice == 9:
            print("Exiting...")
            break

        else:
            print("Invalid Choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
"""


# making the student information management site for college or institution or school using the OOPS concepts
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
    school_name = "School_of _MBU"
    student_count = 0
    student_list = []
    def __init__(self):
        self.name = input("Enter the student name:")
        self.Roll_no = int(input("enter the Roll no:"))
        self.class_name = int(input("enter the student class:"))
        self.section = int(input("Enter the section:"))
        self.mobile = int(input("enter the mobile number:"))
        self.address = input("Enter the student address:")
                          
    def add_new_student(self):
        new_student = student()
        return new_student
    
    def get_student_details(self,roll_no):
        if self.Roll_no == roll_no:
         return (f"student name:{self.name},Roll:{self.Roll_no},class:{self.class_name},section:{self.section},mobile{self.mobile},address:{self.address}")
        else:
            return "student not found"
        
    def remove_student(self,roll_no):
        if self.Roll_no == roll_no:
         del self
         return "student removed successfully"
        else:
            return "student not found"

    def update_student_details(self,roll_no):
        if self.Roll_no == roll_no:
            self.name = input("Enter the student name:")
            self.Roll_no = int(input("enter the Roll no:"))
            self.mobile = int(input("enter the mobile number:"))
            self.address = input("Enter the student address:")
            return "Student details updated successfully"
        else:
            return "student not found"

    @classmethod
    def update_school_name(cls,new_school):
      cls.school_name = new_school
      return "school name updated successfully"

    @classmethod
    def get_no_of_students(cls):
     return cls.student_count

    @classmethod
    def get_all_students_details(cls):
        all_students = []
        for student in cls.student_list:
            all_students.append(student.get_student_details(student.Roll_no))
        return all_students

    @classmethod
    def get_class_students_details(cls,class_name):
        class_students = []
        for student in cls.student_list:
            if student.class_name == class_name:
                class_students.append(student.get_student_details(student.Roll_no))
        return class_students
#main function
def main():
    while True:
        print(f"Welcome to {student.school_name}")
        print("1).To get student details")
        print("2).To add new student")
        print("3).To remove student")
        print("4).To update student details")
        print("5).To update school name")
        print("6).To get number of students in school")
        print("7).To get all student details")
        print("8).To get any class student details")
        print("9).To Exit")

        choice = int(input("Enter the choice (ex:1,2,3,4,5,6,7,8,9):"))

        if choice == 1:
            roll_no = int(input("ENTER THE ROLL_NO:"))
            found = False
            for stu in student.student_list:
                details = stu.get_student_details(roll_no)
                if details != "student not found":
                    print(details)
                    found = True
                    break
            if not found:
                print("student not found")

        elif choice == 2:
            new_student = student()
            student.student_list.append(new_student)
            student.student_count += 1
            print("student added successfully")

        elif choice == 3:
            roll_no = int(input("Enter the Roll Number: "))
            found = False
            for stu in student.student_list:
                result = stu.remove_student(roll_no)
                if result == "student removed successfully":
                    student.student_list.remove(stu)
                    student.student_count -= 1
                    print(result)
                    found = True
                    break
            if not found:
                print("student not found")

        elif choice == 4:
            roll_no = int(input("Enter the student Roll no:"))
            found = False
            for stu in student.student_list:
                result = stu.update_student_details(roll_no)
                if result != "student not found":
                    print(result)
                    found = True
                    break
            if not found:
                print("student not found")

        elif choice == 5:
            new_name = input("Enter the new school name: ")
            result = student.update_school_name(new_name)
            print(result)

        elif choice == 6:
            count = student.get_no_of_students()
            print(f"No of students in the school is: {count}")

        elif choice == 7:
            all_students = student.get_all_students_details()
            for details in all_students:
                print(details)

        elif choice == 8:
            class_name = int(input("Enter the class name:"))
            class_students = student.get_class_students_details(class_name)
            if class_students:
                for details in class_students:
                    print(details)
            else:
                print("No students found in this class")

        elif choice == 9:
            print("...Exiting...")
            break

        else:
            print("Invalid Choice. Try Again.")

if __name__ == "__main__":
    main()