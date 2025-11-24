import psycopg2

def  table():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="admin",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''create table emmployees(Name Text, ID Int, Age Int);''')
    print('Table Created Successfully')

    conn.commit()
    conn.close()

def  data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="admin",host="localhost",port="5432")

    cursor = conn.cursor()

    name = input("Enter the name of the employee: ")
    id = input("Enter ID number of the employee:: ")
    age = input("Enter age of the employee: ")

    query = '''insert into emmployees(Name, ID, Age) values(%s,%s,%s);'''

    cursor.execute(query, (name,id,age))
    print('Data Added Successfully')

    conn.commit()
    conn.close()

data()

"""def  extract():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="admin",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''select * from emmployees;''')
    show = cursor.fetchone()
    print(show[0])

    conn.commit()
    conn.close()"""