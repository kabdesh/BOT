students = [['Ильяс',5],
            ['Арыстан',4],
            ['Касым',5],
            ['Владисвлав',4],
            ['Искандер',4],
            ['Рахат',3],
            ['Виктор',5]]


def get_list_students():
    return students

def get_students_by_number(a):
    if a > len(students) or a < 1:
        return "Извините, такого студента нет!"
    else:
        return students[a-1]

def get_stud_aver_mark():
    aver = 0
    for student in students:
        aver += student[1]
    return aver/len(students)

print(get_stud_aver_mark())


