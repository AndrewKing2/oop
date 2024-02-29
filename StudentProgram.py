import StudentClass as s

def main():
    from datetime import datetime
    student1 = s.Student(8915555,'John Smith','2/29/2000','Junior','','')

    student1.calc_current_age()
    student1.reg_time()

    print(f'The student is {student1.get_age()} years old and {student1.get_time()}')

main()