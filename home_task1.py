

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_grade()}\n' 
            f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}')
    
    def __eq__(self, other):
        return self.__average_grade() == other.__average_grade()
    
    def __lt__(self, other):
        return self.__average_grade() < other.__average_grade()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __average_grade(self):
        grades_sum = 0
        grades_count = 0        
        for courses in self.grades:
            grades_list = self.grades[courses]
            for grades in grades_list:
                grades_sum += grades
                grades_count += 1
        return round(grades_sum / grades_count, 1) if grades_count != 0 else 'Нет оценок'
        

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []      
    
        
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}'
    
    def __eq__(self, other):
        return self.__average_grade() == other.__average_grade()
    
    def __lt__(self, other):
        return self.__average_grade() < other.__average_grade()
    
    def __average_grade(self):
        grades_sum = 0
        grades_count = 0        
        for courses in self.grades:
            grades_list = self.grades[courses]
            for grades in grades_list:
                grades_sum += grades
                grades_count += 1
        return round(grades_sum / grades_count, 1) if grades_count != 0 else 'Нет оценок'


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        

def average_hw_grade(students, course):
    grades_sum = 0
    grades_count = 0
    if type(students) is list:
        for student in students:
            if isinstance(student, Student) and course in student.grades:
                grades_list = student.grades[course]
                for grades in grades_list:
                    grades_sum += grades
                    grades_count += 1
            else:
                continue
    else:
        return 'Error of parameter'
    average_grade = round(grades_sum / grades_count, 1) if grades_count != 0 else 'Нет оценок'
    return f'Средняя оценка за домашние задания на курсе {course}: {average_grade}'

def average_lecturer_grade(lectures, course):
    grades_sum = 0
    grades_count = 0
    if type(lectures) is list:
        for lecturer in lectures:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
                grades_list = lecturer.grades[course]
                for grades in grades_list:
                    grades_sum += grades
                    grades_count += 1
            else:
                continue
    else:
        return 'Error of parameter'
    average_grade = round(grades_sum / grades_count, 1) if grades_count != 0 else 'Нет оценок'
    return f'Средняя оценка за лекции на курсе {course}: {average_grade}'


student_first = Student('Kirill', 'Korostylev', 'Male')
student_second = Student('Ivan', 'Ivanov', 'Male')
lecturer_first = Lecturer('Boris', 'Borisov')
lecturer_second = Lecturer('Petr', 'Petrov')
reviewer_first = Reviewer('Alexander', 'Alexandrov')
reviewer_second = Reviewer('Sidor', 'Sidorov')
student_first.courses_in_progress += ['Python', 'Android'] 
student_second.courses_in_progress += ['Python']
lecturer_first.courses_attached += ['Python']
lecturer_second.courses_attached += ['Python', 'Android'] 
reviewer_first.courses_attached += ['Python', 'Android'] 
reviewer_second.courses_attached += ['Python']
student_first.rate_lecturer(lecturer_first, 'Python', 5)
student_first.rate_lecturer(lecturer_second, 'Python', 3)
reviewer_second.rate_hw(student_first, 'Python', 5)
reviewer_second.rate_hw(student_second, 'Python', 4)
print(student_first)
print(student_second)
print(student_first > student_second)
print(lecturer_first)
print(lecturer_second)
print(reviewer_first)
print(reviewer_second)
print(average_hw_grade([student_first, student_second], 'Python'))
print(average_lecturer_grade([lecturer_first, lecturer_second], 'Python'))
help(Student)