import sqlite3 as sq
dbase = sq.connect('StudentDataBase.db')
dbase.execute('''CREATE TABLE IF NOT EXISTS student(
ROLL TEXT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SGPA TEXT NOT NULL
)''')
sql_insert_querry = """INSERT INTO student(ROLL,NAME,SGPA) VALUES (?,?,?)"""
sql_select_querry = """SELECT * FROM student"""
sql_update_querry = '''UPDATE student SET SGPA = ? WHERE ROLL = ?'''
class Student:
    def set_data(self):
        self.name = input("Enter Name : ")
        self.roll = input("Enter Roll Number : ")
        self.pointer = input("Enter FE SGPA : ")

    def print_data(self):
        print("Name : ",self.name)
        print("Roll : ",self.roll)
        print("SGPA : ",self.pointer)


print("\tPRACTICE DATASHEET")
choice = 0
while choice!=5:
    print("1] Enter New Record\t2] Print Records\t3] Search Records\t4] Update a Record\t5] EXIT")
    choice = int(input())
    if choice==1:
        s = Student()
        s.set_data()
        data = (s.roll,s.name,s.pointer)
        dbase.execute(sql_insert_querry,data)
        dbase.commit()
    elif choice==2:
        data = dbase.execute(sql_select_querry)
        for i in data:
            print(f'Roll Number : {i[0]}',end=' ')
            print(f'Name : {i[1]}',end=' ')
            print(f'FE SGPA : {i[2]}',end='\n\n')
    elif choice==3:
        data = dbase.execute(sql_select_querry)
        roll = input('Search Roll Number : ')
        for i in data:
            if roll==i[0]:
                print(f'Roll Number : {i[0]}', end=' ')
                print(f'Name : {i[1]}', end=' ')
                print(f'FE SGPA : {i[2]}', end='\n\n')
    elif choice==4:
        roll = input('Update Roll Number : ')
        marks = input('New SGPA : ')
        data = (marks,roll)
        dbase.execute(sql_update_querry,data)
        dbase.commit()