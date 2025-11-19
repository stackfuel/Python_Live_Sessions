class Person:
    def __init__(self, name, alter, **kwargs):
        self.name = name
        self.alter = alter
        super().__init__(**kwargs)

    def __repr__(self):
        return f"Person(name={self.name}, alter={self.alter})"
    
    def is_adult(self):
        return self.alter >= 18
    
class Staff:
    def __init__(self, position, salary, **kwargs):
        self.position = position
        self.salary = salary
        super().__init__(**kwargs)

    def __repr__(self):
        return f"Staff(position={self.position}, salary={self.salary})"


class Professor(Person, Staff):
    def __init__(self, name, alter, fachgebiet, position, salary):
        super().__init__(name=name, alter=alter, position=position, salary=salary)
        self.fachgebiet = fachgebiet
        
    def __repr__(self):
        return f"Professor(name={self.name}, alter={self.alter}, fachgebiet={self.fachgebiet}, position={self.position}, salary={self.salary})"


class Course:
    def __init__(self, name, credits, professor: Professor = None):
        self.name = name
        self.credits = credits
        self.professor = professor

    def __repr__(self):
        return f"Course(name={self.name}, credits={self.credits}, professor={self.professor.name if self.professor else None})"


class Student(Person):
    def __init__(self, name, alter):
        super().__init__(name, alter)
        self.courses = []
        
    def __repr__(self):
        return f"Student(name={self.name}, alter={self.alter}, courses={len(self.courses)})"
    
    def enroll(self, course: Course):
        self.courses.append(course)
        print(f"{self.name} wurde in den Kurs '{course.name}' eingeschrieben.")

    def get_courses(self):
        return self.courses