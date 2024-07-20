import csv
from operator import itemgetter
class GradeAnalyzer:
    def __init__(self, grades_file, students_file, courses_file, num_courses, num_students) -> None:
        self.grades_file=grades_file
        self.students_file=students_file
        self.courses_file=courses_file
        self.num_students=num_students
        self.num_courses=num_courses
        self.students=[]
        self.courses=[]
        self.grades=[]
    #Function to load student CSV file
    def load_student(self):
        with open(self.students_file, 'r') as csvfile:
            for _ in csv.DictReader(csvfile):
                self.students.append(_)
        return self.students
    #Function to load courses CSV file
    def load_courses(self):
        with open(self.courses_file, 'r') as csvfile:
            for _ in csv.DictReader(csvfile):
                self.courses.append(_)
        return self.courses
    #Function to load grades CSV file
    def load_grades(self):
        with open(self.grades_file, 'r') as csvfile:
            for _ in csv.DictReader(csvfile):
                self.grades.append(_)
        return self.grades  
    #Function to rank according to a specific dictionary key e.g grades
    def rank(list_of_dic, dic_key):
        list_of_dic.sort(key=itemgetter(dic_key), reverse=True)
        count=0
        age=0.0
        for i in list_of_dic: 
            for j in list(i.keys()):
                if dic_key==j:
                    count=count+1
                    temp=age
                    age=i[j]
                    if(temp==i[j]):
                        count1=count-1
                        (i.update({"rank":count1}))
                    else:
                        (i.update({"rank":count}))
        return list_of_dic 
    #Function returns a ranked list of class average per course 
    def class_average(self):
        class_avg=[]
        for x in self.courses:
            for y in x:
                sum=0
                filter_grade=[]
                filter_grade = [i for i in self.grades if i['course_id'] == x[y]]
                for n in filter_grade:
                    for m in n:
                        if(m=='grade'):
                            sum=sum+int(n[m])
                if(y=='course_id'):
                    avg=sum/500
                    class_avg.append({'course_id': x['course_id'], 'course_name':x['name'], 'course_lecturer':x['lecturer'], 'course_credit':x['credits'], 'course_average': avg})
        return GradeAnalyzer.rank(class_avg, 'course_average')
    #Function returns a list of top students 
    def top_students(self):
        top_stud=[] 
        for x  in self.courses:
            for y in x:
                max=0
                filter_grade=[]
                filter_grade = [i for i in self.grades if i['course_id'] == x[y]]
                for n in filter_grade:
                    for m in n:
                            if(m=='grade' and int(n[m])>int(max)):
                                max=n[m]
                for i in self.students:
                    for j in i:
                        filter_grade1 = [_ for _ in filter_grade if  _['student_id']==i[j] and _['grade']==max and _['course_id'] == x[y] ]
                        for n in filter_grade1: 
                            for m in n:
                                if(y=='course_id' and x[y]==n[m]):
                                    top_stud.append({'course_id': x['course_id'], 'course_name':x['name'], 'course_lecturer':x['lecturer'], 'course_credit':x['credits'], 'student_id':n['student_id'], 'student_Name':i['name'], 'top mark': max})
        return top_stud
    #Function returns a filtered list of the top students per course
    def top_students_per_course(self, course_id):
        filter_course = [i for i in GradeAnalyzer.top_students(self) if i['course_id'] == course_id]
        return filter_course
    #Returns the average of each student and rank  
    def generate_report(self):
        report=[]
        for x  in self.students:
            for y in x:
                sum=0
                filter_grade = [i for i in self.grades if i['student_id'] == x[y]]
                for n in filter_grade:
                    for m in n:
                        if(m=='grade'):
                            sum=sum+int(n[m])
                if(y=='student_id'):
                    avg=sum/self.num_courses
                    if (avg>=85 and avg<=100): 
                        g='A'
                        r='Excellent' 
                    elif (avg>=70 and avg<=84.9): 
                        g='B'
                        r='Very Good'
                    elif (avg>=60 and avg<=69.9): 
                        g='C'
                        r='Good'
                    elif (avg>=50 and avg<=59.9): 
                        g='D'
                        r='Fairly Good'
                    elif (avg>=45 and avg<=49.9): 
                        g='E'
                        r='Average'
                    else: 
                        g='F'
                        r='fail'
                    report.append({'student_id': x['student_id'], 'student_name':x['name'], 'age':x['age'], 'student_average': avg, 'grade': g, 'remark': r}) 
        return GradeAnalyzer.rank(report, 'student_average')
    #Function returns the grades for each student
    def student_report(self, student_id):
        filter=[i for i in GradeAnalyzer.load_grades(self) if i['student_id']==student_id ]
        return filter
    #Function converts list of dictionaries to CSV file
    def write_to_csv(self, data, filename):
        keys=data[0].keys()
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, keys)
            writer.writeheader()
            writer.writerows(data)