import glob
import sys
import os
import threading, time
from generate_data import Generate_Data as gd
from grade_analyzer import GradeAnalyzer as ga
data=gd()
num_courses = int(input("\nEnter the number of course you want to generate: ")) 
courses_data = data.generate_courses(num_courses)
num_students = int(input("\nEnter the number of students to be generated: "))
students_data = data.generate_students(num_students)
grades_data = data.generate_grades(students_data, courses_data)
print("\nDatasets generated successfully.")
#Write data to CSV files
os.chdir(r"data")
#file directories
avg_report=r'course_average.csv'
top_report=r'top_students.csv'
report=r'report.csv'
courses_file=r'courses.csv'
students_file=r'students.csv'
grades_file=r'grades.csv'
#Loading files from csv
analysis=ga(grades_file, students_file, courses_file, num_courses, num_students)
students=analysis.load_student()
courses=analysis.load_courses()
grades=analysis.load_grades()

def write_to_csv():
    print("\nWait, Loading Dataset to CSV Files!")
    for file in glob.glob(r'student_performance\*'):
        os.remove(file)
    for file in glob.glob(r'top_student_data_per_course\*'):
        os.remove(file)
    data.write_to_csv(courses_data, courses_file)
    data.write_to_csv(students_data, students_file)
    data.write_to_csv(grades_data, grades_file)
    analysis.write_to_csv(analysis.class_average(), avg_report)
    analysis.write_to_csv(analysis.top_students(), top_report)
    analysis.write_to_csv(analysis.generate_report(), report)
    for i in students:
        for j in i:
            if(j=='student_id'):
                analysis.write_to_csv(analysis.student_report(i[j]), fr'student_performance\{i[j]}.csv')
    for i in courses:
        for j in i:
            if(j=='course_id'):
                analysis.write_to_csv(analysis.top_students_per_course(i[j]), fr'top_student_data_per_course\{i[j]}.csv')
write_to_csv()    

def display(list_dic):
    for i in list_dic:
        print()
        for j in i:
            print(j, i[j])
def report_func():
    os.system('cls')
    print('\n**************************************Performance Report*******************************************')
    print('\n---> 1. General Performance Result')
    print('\n---> 2. Student Performance Result')
    print('\n---> 3. Main Menu')
    print('\n---> 4. Exit Program')
    choice=str(input('\nEnter the Number for Each Operation e.g 1 to General Performance Result: '))
    while(True):
        if (choice not in ['1','2','3','4']):
            choice=str(input('\nWrong Entry\nEnter the Number for Each Operation e.g 1 to General Performance Result: '))
            continue
        else:
            break
    if choice=='1':
        os.system('cls')
        print("\nPlease wait...")
        display(analysis.generate_report())
        print('\n**************************************General Performance Menu*******************************************')
        print('\n---> 1. Student Performance Report')
        print('\n---> 2. Main Menu')
        print('\n---> 3. Exit Program')
        choice=str((input('\nEnter the Number for Each Operation e.g 1 to Main Menu: ')))
        while(True):
            if ( choice not in ['1','2','3']):
                choice=str((input('\nWrong Entry\nEnter the Number for Each Operation e.g 1 to Main Menu: ')))
                continue
            else:
                break
        if choice=='1':
            student_per_report()
        elif choice=='2':
            os.system('cls')
            main_menu()
        elif choice=='3':
            os.system('cls')
            sys.exit("Thanks For Using the Application")
    elif choice=='2':
        student_per_report()
    elif choice=='3':
        os.system('cls')
        main_menu()
    elif choice=='4':
        os.system('cls')
        sys.exit("Thanks For Using the Application")
def student_per_report():
    os.system('cls')
    student_id=str(input("\nEnter the student id: "))
    while(True):
        chk=0
        for i in students:
            for j in i:
                if(i[j]==student_id):
                    chk=1
        if(chk==0):
            student_id=str(input('\nWrong Entry\nEnter the correct student id: '))
            continue
        elif(chk==1):
            break
    display(analysis.student_report(student_id))
    filter=[x for x in analysis.generate_report() if x['student_id']==student_id]
    print(f'\nRank {filter[0]['rank']}/{num_students}')
    print('\n**************************************General Performance Menu*******************************************')
    print('\n---> 1. General Performance Result')
    print('\n---> 2. Main Menu')
    print('\n---> 3. Exit Program')
    choice=str((input('\nEnter the Number for Each Operation e.g 1 to Main Menu: ')))
    while(True):
        if ( choice not in ['1','2','3']):
            choice=str((input('\nWrong Entry\nEnter the Number for Each Operation e.g 1 to Main Menu: ')))
            continue
        else:
            break
    if choice=='1':
        os.system('cls')
        print("\nPlease wait...")
        display(analysis.generate_report())
    elif choice=='2':
        os.system('cls')
        main_menu()
    elif choice=='3':
        os.system('cls')
        sys.exit("Thanks For Using the Application")
def all_courses():
    os.system('cls')
    print("\nPlease Wait")
    print('\n**************************************Top Students For Courses*******************************************')
    print('\n---> 1. View For All Courses')
    print('\n---> 2. View Per Course')
    print('\n---> 3. Main Menu')
    print('\n---> 4. Exit Program')
    choice=str((input('\nEnter the Number for Each Operation e.g 1 to View For All Courses: ')))
    while(True):
        if (choice not in ['1','2','3','4']):
            choice=str(input('\nWrong Entry\nEnter the Number for Each Operation e.g 1 to View For All Courses: '))
            continue
        else:
            break
    if choice=='1':
        os.system('cls')
        display(analysis.top_students())
        print('\n\n**************************************Top Students For All Courses Menu*******************************************')
        print('\n---> 1. View per Course')
        print('\n---> 2. Main Menu')
        print('\n---> 3. Exit Program')
        choice=str((input('\nEnter the Number for Each Operation e.g 1 to go back: ')))
        while(True):
            if (choice not in ['1','2','3']):
                choice=str(input('\nWrong Entry\nEnter the Number for Each Operation e.g 1 to View For All Courses: '))
                continue
            else:
                break
        if choice=='1':
            per_course()
        elif choice=='2':
            os.system('cls')
            main_menu()
        elif choice=='3':
            os.system('cls')
            sys.exit("Thanks For Using the Application")
    elif choice=='2':
        per_course()
    elif choice=='3':
        os.system('cls')
        main_menu()
    elif choice=='4':
        os.system('cls')
        sys.exit("Thanks For Using the Application")
def per_course():
    os.system('cls')
    course_id=str(input("\nEnter the course id: "))
    while(True):
        chk=0
        for i in courses:
            for j in i:
                if(i[j]==course_id):
                    chk=1
        if(chk==0):
            course_id=str(input('\nWrong Entry\nEnter the correct course id: '))
            continue
        elif(chk==1):
            break
    display(analysis.top_students_per_course(course_id))
    print('\n\n**************************************Top Students Per Courses Menu*******************************************')
    print('\n---> 1. View For All Courses')
    print('\n---> 2. Main Menu')
    print('\n---> 3. Exit Program')
    choice=str((input('\nEnter the Number for Each Operation e.g 1 to go back: ')))
    while(True):
        if (choice not in ['1','2','3']):
            choice=str(input('\nWrong Entry\nEnter the Number for Each Operation e.g 1 to View For All Courses: '))
            continue
        else:
            break
    if choice=='1':
        os.system('cls')
        all_courses() 
    elif choice=='2':
        os.system('cls')
        main_menu()
    elif choice=='3':
        os.system('cls')
        sys.exit("Thanks For Using the Application")
def main_menu():
    print('\n\n\n\n****************************School Management Analyis System****************************')
    print('\n**************************************Main Menu*******************************************')
    print('\n---> 1. Load Data')
    print('\n---> 2. Class Average For Each Course')
    print('\n---> 3. Top Students For Courses')
    print('\n---> 4. Performance Result')
    print('\n---> 5. Exit Program')        
    choice=str((input('\nEnter the Number for Each Operation e.g 1 to load data: ')))
    while(True):
        if ( choice not in ['1','2','3','4','5']):
            choice=str((input('\nWrong Entry\nEnter the Number for Each Operation e.g 1 to load data: ')))
            continue
        else:

            break
    if choice=='1':
        analysis.load_student()
        analysis.load_courses()
        analysis.load_grades()
        os.system('cls')
        print('\nLoading Succssfull')
        os.system('cls')
        main_menu()
    elif choice=='2':
        os.system('cls')
        print('\n**************************************Class Average For Each Course*******************************************')
        display(analysis.class_average())
        print('\n**************************************Class Average Menu*******************************************')
        print('\n---> 1. Main Menu')
        print('\n---> 2. Exit Program')
        choice=str((input('\nEnter the Number for Each Operation e.g 1 to Main Menu: ')))
        while(True):
            if ( choice not in ['1','2']):
                choice=str((input('\nWrong Entry\nEnter the Number for Each Operation e.g 1 to Main Menu: ')))
                continue
            else:
                break
        if choice=='1':
            os.system('cls')
            main_menu()
        elif choice=='2':
            os.system('cls')
            sys.exit("Thanks For Using the Application")
    elif choice=='3':
        all_courses()
    elif choice=='4':
        report_func()
    elif choice==5:
        sys.exit("Thanks For Using the Application")
main_menu()