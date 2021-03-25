from portal.student import Student
from hydra.schema import Schema
from portal.degree_plan import DegreePlan
from portal.course import Course
from portal.advisor import Advisor


if __name__ == '__main__':
    db = Schema()
    course = Course(db)
    degree_plan = DegreePlan('ITCS', 2021, db, course)
    advisor = Advisor('Jim', 'Moriarty', 'jim@gmial.com')
    student = Student(degree_plan, course, advisor, db)

    student.name = 'R'
    student.lastname = 'A'
    student.major = degree_plan.name

    print(student)
    print(student.course)
