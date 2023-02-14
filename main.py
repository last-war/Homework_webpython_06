from datetime import datetime
import faker
from faker.providers import DynamicProvider
import sqlite3
from random import randint, choice


NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUP = 3
NUMBER_SUBJECT = randint(5, 8)
NUMBER_TEACHERS = randint(3, 5)


def create_db():
    """just create empty tables"""
    with open('create_db.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('course.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


def fill_db(study_groups, students, teachers, subjects, marks):
    """insert to database"""
    with sqlite3.connect('course.db') as con:
        cur = con.cursor()
        sql_to_study_groups = """INSERT INTO study_groups(gr_name)
                                       VALUES (?)"""
        cur.executemany(sql_to_study_groups, study_groups)

        sql_to_students = """INSERT INTO students(full_name, group_id)
                                       VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(full_name)
                                       VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(sub_name, teacher_id)
                                       VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_marks = """INSERT INTO journal(mark, subject_id, student_id)
                                       VALUES (?, ?, ?)"""
        cur.executemany(sql_to_marks, marks)

        con.commit()


def generate_fake_data() -> dict:
    """generate some fake lists"""

    fake_data = faker.Faker()
    rez = {'students': [], 'study_groups': [], 'teachers': [], 'subjects': []}
    for _ in range(NUMBER_STUDENTS):
        rez['students'].append(fake_data.name())
    for _ in range(NUMBER_TEACHERS):
        rez['teachers'].append(fake_data.name())

    for _ in range(NUMBER_GROUP):
        rez['study_groups'].append(fake_data.msisdn())

    subject_provider = DynamicProvider(
        provider_name="subject",
        elements=["Computer Science", "Computing", "IT", "Multimedia", "Software", "Architecture", "Built Environment",
                  "Construction", "Maintenance Services", "Planning", "Property Management", "Surveying"],
    )
    fake_data.add_provider(subject_provider)
    for _ in range(NUMBER_SUBJECT):
        rez['subjects'].append(fake_data.unique.subject())

    return rez


def prepare_data(raw: dict) -> tuple:
    """convert dict of data to tuple"""
    study_groups = []
    for group in raw['study_groups']:
        study_groups.append((group, ))

    students = []
    for stud in raw['students']:
        students.append((stud, randint(1, NUMBER_GROUP)))

    teachers = []
    for teacher in raw['teachers']:
        teachers.append((teacher, ))

    subjects = []
    for subject in raw['subjects']:
        subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    marks = []
    for _ in range(1, NUMBER_STUDENTS*20):
        marks.append((randint(1, 10), randint(1, NUMBER_SUBJECT), randint(1, NUMBER_STUDENTS)))

    return study_groups, students, teachers, subjects, marks


def execute_query():
    with sqlite3.connect('course.db') as con:
        cur = con.cursor()
        for itr in range(1, 13):
            with open('query_'+str(itr)+'.sql', 'r') as f:
                sql = f.read()

            cur.execute(sql)
            print(cur.fetchall())


if __name__ == "__main__":
    create_db()
    fake_db = generate_fake_data()
    normal_fake_db = prepare_data(fake_db)
    fill_db(*normal_fake_db)
    execute_query()

