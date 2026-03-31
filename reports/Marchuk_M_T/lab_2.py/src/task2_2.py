"""
Модуль для моделирования системы 'Факультатив'.
Включает Студентов, Преподавателей, Курсы и Архив оценок.
"""

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def __str__(self):
        return f"Курс: {self.title} (Записано студентов: {len(self.students)})"

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Студент: {self.name}"

class Teacher:
    def __init__(self, name):
        self.name = name

    def announce_course(self, title):
        print("[Преподаватель {self.name}]: Открыта запись на курс '{title}'")
        return Course(title)

def set_grade(self, student, course, value, archive_obj):
    print(f"[Преподаватель {self.name}]: Выставлена оценка {value} студенту {student.name}")
    archive_obj.save_record(student.name, course.title, value)

class Archive:
    def __init__(self):
        self.records = []

    def save_record(self, student_name, course_title, grade):
        self.records.append({
            "student": student_name,
            "course": course_title,
            "grade": grade
        })

    def show_all(self):
        print("\n--- АРХИВ ОЦЕНОК ---")
        if not self.records:
            print("Записей нет.")
        for r in self.records:
            print("Студент: {r['student']} | Курс: {r['course']} | Оценка: {r['grade']}")

# Демонстрация
print("--- Система Факультатив ---")
archive = Archive()
teacher = Teacher("Иванов И.И.")
student1 = Student("Алексей Крощенко")
student2 = Student("Мария Петрова")

# Логика работы
course_python = teacher.announce_course("Программирование на Python")

while True:
    print("\nМеню системы:")
    print("1. Записать студента 1 на курс")
    print("2. Записать студента 2 на курс")
    print("3. Выставить оценку студенту 1")
    print("4. Выставить оценку студенту 2")
    print("5. Посмотреть архив")
    print("0. Выход")

    choice = input("Действие: ")

    if choice == "1":
        course_python.students.append(student1)
        print("{student1.name} записан.")
    elif choice == "2":
        course_python.students.append(student2)
        print("{student2.name} записан.")
    elif choice == "3":
        val = input("Введите оценку для Алексея: ")
        teacher.set_grade(student1, course_python, val, archive)
    elif choice == "4":
        val = input("Введите оценку для Марии: ")
        teacher.set_grade(student2, course_python, val, archive)
    elif choice == "5":
        archive.show_all()
    elif choice == "0":
        break
