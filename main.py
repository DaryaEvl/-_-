
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def course_grades (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 0< grade<= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_grades(self):
        all_grades = 0
        count_grades = 0
        for courses, grades in  self.grades.items():
            for grade in grades:
                all_grades += grade
                count_grades += 1
        average_grades = all_grades / count_grades
        return round(average_grades,2)
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за ДЗ  {self.average_grades()} ' \
               f'\nКурсы в процессе изучения {" ".join(self.courses_in_progress)} ' \
               f'\nЗавершенные курсы  {" ".join(self.finished_courses)}'
    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка! Студента нет в списке!"
        elif self.average_grades() < other.average_grades():
            return f'Средняя оценка выше у {other.name} {other.surname}'
        else:
            return f'Средняя оценка выше у {self.name} {self.surname}'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer (Mentor):
    def __init__(self,  name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_grades(self):
        all_grades = 0
        count_grades = 0
        for courses, grades in  self.grades.items():
            for grade in grades:
                all_grades += grade
                count_grades += 1
        average_grades = all_grades / count_grades
        return round(average_grades,2)
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции {self.average_grades()}'
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return"Ошибка! Лектора нет в списке преподавателей!"

        elif self.average_grades() < other.average_grades():
            return f'Средняя оценка за лекции выше у {other.name} {other.surname }'
        else:
            return f'Средняя оценка за лекции выше у {self.name} {self.surname}'
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 0< grade<= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


ivan_ivanov = Student('Ivan', 'Ivanov', 'man')
ivan_ivanov.finished_courses = ['Python']
ivan_ivanov.courses_in_progress = ['Git']
ivan_ivanov.grades = {"Python": [10, 8, 9, 9, 9, 10], "Git":[10, 6, 9]}

petr_petrov = Student('Petr', 'Petrov', 'man')
petr_petrov.finished_courses = ['Python', 'Git']
petr_petrov.courses_in_progress = []
petr_petrov.grades = {"Python": [10, 8, 9], "Git":[9, 7, 9]}

dmitrii_smirnov = Student('Dmitrii', 'Smirnov', 'man')
dmitrii_smirnov.finished_courses = []
dmitrii_smirnov.courses_in_progress = ['Python', 'Git']
dmitrii_smirnov.grades = {"Python": [9, 10], "Git":[10, 6, 9]}

elena_kalinina = Mentor('Elena', 'Kalinina')
elena_kalinina.courses_attached = ['Python']
alex_aleksandrov = Mentor('Alex', 'Aleksandrov')
alex_aleksandrov.courses_attached = ['Python', 'Git']

roman_romanov = Reviewer('Roman', 'Romanov')
maxim_smirnov = Reviewer('Maxim', 'Smirnov')
maxim_smirnov.courses_attached = ['Python', 'Git']
svetlana_svetlova = Lecturer('Svetlana', 'Svetlova')
svetlana_svetlova.courses_attached = ['Python', 'Git']
denis_popov = Lecturer('Denis', 'Popov')
denis_popov.courses_attached = ['Git']

print(ivan_ivanov)
print(petr_petrov)
print(roman_romanov)
print(maxim_smirnov)
ivan_ivanov.course_grades(svetlana_svetlova, 'Git', 10)
ivan_ivanov.course_grades(denis_popov, 'Git', 7)
print(svetlana_svetlova.grades)
print(svetlana_svetlova)
print(ivan_ivanov<petr_petrov)
print(svetlana_svetlova<denis_popov )
maxim_smirnov.rate_hw(ivan_ivanov, 'Git', 4)

student_list = [ivan_ivanov, petr_petrov, dmitrii_smirnov]

def ad_grade(student_list, course):
    all_grade = 0
    count_grade = 0
    for student in student_list:
        if course in student.courses_in_progress :
            for st_course, grade in student.grades.items():
                if st_course == course:
                    for st_grade in grade:
                        all_grade += int(st_grade )
                        count_grade +=1
            return f'Средняя оценка студентов за курс {course} - { all_grade/count_grade}'
        else:
            return f'Нет студентов изучающих курс {course}'

print(ad_grade(student_list, 'Git'))

lecturer_list = [svetlana_svetlova, denis_popov]

def ad_grade_lecturer(lecturer_list , course):
    all_grade_lecturer = 0
    count_grade = 0
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached:
            for lec_course, grade in lecturer.grades.items():
                if lec_course == course:
                    for lec_grade in grade:
                        all_grade_lecturer += int(lec_grade )
                        count_grade +=1
            return f'Средняя оценка лектора за курс {course} - { all_grade_lecturer/count_grade}'
        else:
            return f'Нет лекторов читающих курс {course}'

print(ad_grade_lecturer(lecturer_list, 'Git'))