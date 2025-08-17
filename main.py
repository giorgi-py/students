from student_class import Student
import sys
from pyfiglet import figlet_format


def main():
    while True:
        try:
            print (figlet_format("Students"))
            print ("======= MAIN MENU ===   ====")
            menu = int(input("[1]. Display Students\n[2]. Add Student\n[3]. Quit\n>> "))
            if menu == 3:
                sys.exit(figlet_format('Goodbye!'))
            if menu == 2:
                while True:
                    print ("=============== ADD STUDENT ===============")
                    first, last, grade = input(">> Enter: [Name] [Lastname] [Grade(10-100)]: ").split(" ")
                    if first == '3':
                        break
                    add_student(first, last, int(grade))
                    continue
            if menu == 1:
                print (display_students())
                break
        except ValueError:
            print("\nIncorrect Information")
            continue

def add_student(first, last, grade):
    st1 = Student(first, last, grade)
    st1.add_student()
    print (f">> {first} {last} Added!")

def display_students():
    return Student.full_info()

def add_grade():
    ...


if __name__ == '__main__':
    main()