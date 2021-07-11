# ex.1
# def func(lst):
#     data_type = list(map(type, lst))
#     result = {lst[i]: data_type[i] for i in range(len(lst))}
#     return result
  
  
# print(func([1, 4.7, 'hi', False, None]))

# # ex.2
# a=int(input('кол-во строк: ')) 
# b=int(input('кол-во звездочек на строке: ')) 
# print(a*'{}\n'.format(b*'*'))


# # ex3
# a = [1, 54, 3, 6, 8, 90, 4, 2]
# b = [2, 4, 3, 87, 6, 32, 56, 90]
# c = []
# for i in a: 
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)


# # ex4
# def counter(digit):
#     result = 0
#     while digit > 0 and digit != float:
#         result += digit % 10
#         digit //= 10
#     return result
 
# print(counter(67))

# # ex5
# import psycopg2
# class CSV:
#     conn = psycopg2.connect(dbname='Adb', user='Aig', password='post')
#     cur = conn.cursor()
#     cur.execute("""CREATE TABLE database(
#         id integer,
#         name varchar(50),
#         pol varchar(50),
#         age integer,
#     );
#     """)
#     with open(r'exam.csv', 'r') as f:
#         next(f)
#         cur.copy_from(f, 'database', sep='*********')

#     conn.commit()


#     def sorting(self):
#         self.cur.execute("SELECT name FROM database ORDER BY age ASC;")
#         row = self.cur.fetchall()
#         return row

#     def adding_row(self):
#         self.cur.execute("ALTER TABLE database ADD column surname VARCHAR(60);")
#         row = self.cur.fetchall()
#         return row

#     def updating_row(self):
#         self.cur.execute("UPDATE database SET name='Dante' WHERE id=2;")
#         updating = self.cur.fetchall()
#         return updating


#     def editing(self):
#         self.cur.execute("ALTER TABLE database ALTER COLUMN age SET NOT NULL;")
#         editted = self.cur.fetchall()
#         return editted
    
#     def find_name(self):
#         self.cur.execute("SELECT name FROM database WHERE pol = 'female';")
#         name = self.cur.fetchall()
#         return name