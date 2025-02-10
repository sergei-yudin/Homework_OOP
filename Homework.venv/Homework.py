class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            "Ошибка"

    def average_score(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return round(sum(all_grades) / len(all_grades), 2)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.average_score()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_score() < other.average_score()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_score() <= other.average_score()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_score() == other.average_score()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_score() > other.average_score()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_score() >= other.average_score()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_score() != other.average_score()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.grades = {}

    def average_score(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return round(sum(all_grades) / len(all_grades), 2)

    def rate_hw(self, student, course, grade):
        pass

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score() < other.average_score()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score() <= other.average_score()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score() == other.average_score()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score() > other.average_score()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score() >= other.average_score()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score() != other.average_score()
        return NotImplemented

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_score()}"


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

# Функции для подсчёта средних баллов
def average_homework(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return round(sum(total_grades) / len(total_grades), 2) if total_grades else 0

def average_lecture(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return round(sum(total_grades) / len(total_grades), 2) if total_grades else 0

# Вводные данные:
student1 = Student("Иван", "Иванов", "Мужской")
student2 = Student("Анна", "Ефимова", "Женский")

student1.courses_in_progress = ["Python", "Java"]
student2.courses_in_progress = ["JavaScript", "Python"]

lecturer1 = Lecturer("Петр", "Смирнов", ["Python", "Java"])
lecturer2 = Lecturer("Сергей", "Балашов", ["Python", "JavaScript"])

reviewer1 = Reviewer("Николай", "Петров", ["Python", "Java"])
reviewer2 = Reviewer("Елена", "Миронова", ["JavaScript", "Python"])

reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Python", 7)
reviewer1.rate_hw(student1, "Java", 9)

reviewer2.rate_hw(student2, "Python", 6)
reviewer2.rate_hw(student2, "Python", 5)
reviewer2.rate_hw(student2, "JavaScript", 7)

student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer1, "Java", 8)
student2.rate_lecturer(lecturer2, "Python", 7)
student2.rate_lecturer(lecturer2, "JavaScript", 6)

print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()
print(reviewer2)
print()

# Вызов функций после основного вывода
print(f"Средняя оценка за курс Python среди студентов: {average_homework([student1, student2], 'Python')}")
print(f"Средняя оценка за курс Python среди лекторов: {average_lecture([lecturer1, lecturer2], 'Python')}")
