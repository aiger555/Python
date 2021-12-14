# import psycopg2
# import config
# import base64

# from pprint import pprint
# from datetime import datetime

# def manager(method):
#     def wrapper(*args, **kwargs):
#         args[0].cursor = args[0].connection.cursor()
#         method(*args, **kwargs)
#         args[0].cursor.close()
#     return wrapper

# def fetcher(method):
#     def wrapper(*args, **kwargs):
#         args[0].cursor = args[0].connection.cursor()
#         response = method(*args, **kwargs)
#         args[0].cursor.close()
#         return response
#     return wrapper

# class Coder:
#     #Do not use this for real application! Here I just pretend to encode password safely.
#     def encode(key, clear):
#         enc = []
#         for i in range(len(clear)):
#             key_c = key[i % len(key)]
#             enc_c = (ord(clear[i]) + ord(key_c)) % 256
#             enc.append(enc_c)
#         return base64.urlsafe_b64encode(bytes(enc))

# class DBConnection:
#     def __init__(self):
#         try:
#             self.connection = psycopg2.connect(dbname=config.DBNAME, user=config.USER, password=config.PASSWORD, port=config.PORT)
#             self.connection.autocommit = True
#         except:
#             pprint("Connect to database ==> Failure")

#     # @manager
#     # def createTable(self):
#     #     cmd = "CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY, name varchar(100) NOT NULL, surname varchar(100), email varchar(100) UNIQUE NOT NULL, password varchar(255) NOT NULL, date_of_birth date, date_of_creation date) "
#     #     self.cursor.execute(cmd)

#     @manager
#     def perform(self, command, values):
#         self.cursor.execute(command, values)

#     @fetcher
#     def fetchOne(self, command, values):
#         self.cursor.execute(command, values)
#         data = self.cursor.fetchall()
#         return data

# class User:
#     def __init__(self, name = None, surname = None, email = None, date_of_birth = None):
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.date_of_birth = date_of_birth

#     def __str__(self):
#         return f'''Account info:\n\tUser: {self.email}\n\tName: {self.name}\n\tSurname: {self.surname}\n\tBirth day: {self.date_of_birth}'''

#     @classmethod
#     def register(cls, dbconnection):
#         #Assuming we already have table for users.
#         #pass the DB connection when executing this function.
#         name = None
#         email = None
#         password = None
#         print("Registration process. Please fill in your information")
#         while True:
#             name = input("Name (Required field): ")
#             if len(name) > 0:
#                 break
#         surname = input("Last name: ")
#         while True:
#             email = input("Email (Required field): ")
#             if len(email) > 0:
#                 email = email.lower()
#                 break
#         while True:
#             password = input("Password (Required field): ")
#             if len(password) > 0:
#                 password = Coder.encode(config.PASSWORD_ENCRYPTION_KEY, password).decode('ascii')
#                 break        
#         bd = input("Birth day in 'dd.mm.yyyy' format: ")
#         date_of_creation = datetime.now()

#         executable_command = """INSERT INTO users(name, surname, email, password, date_of_birth, date_of_creation) VALUES (%s, %s, %s, %s, %s, %s)"""
#         values = (name, surname, email, password, bd, date_of_creation)
        
#         try:
#             dbconnection.perform(executable_command, values)
#         except psycopg2.errors.UniqueViolation as e:
#             print("Operation Failure!\nUser with this email already exist.")
#             return None
#         except psycopg2.errors.DatetimeFieldOverflow as e:
#             print("Operation Failure!\nUser's birth day is out of real range.")
#             return None
#         except psycopg2.errors.NotNullViolation as e:
#             print("Operation Failure!\nSome of the required fields are NULL.")
#             return None
#         except Exception as e:
#             print("Operation Failure!\nUnknown Error.")
#             return None

#         print("Successfully registered.")
#         return User(name, surname, email, bd)

#     @classmethod
#     def login(cls, dbconnection):
#         email = input("Email: ")
#         email = email.lower()
#         password = input("Password: ")
#         executable_command = '''select name, surname, email, date_of_birth from users as u WHERE u.email = %s and u.password = %s'''
#         values = (email, Coder.encode(config.PASSWORD_ENCRYPTION_KEY, password).decode('ascii'),)
#         try:
#             fetchedData = dbconnection.fetchOne(executable_command, values)
#             if len(fetchedData) != 0:
#                 (name, surname, email, bd) = fetchedData[0]
#                 assignUser = User(name, surname, email, bd)
#                 print("Successfully logged in.")
#                 return assignUser
#             else:
#                 print("No such record in database. Try again.")
#                 return None
#         except Exception as e:
#             print(e)

#     def update(self, dbconnection):
#         name = None
#         print("Update your information. Please fill in your information")
#         while True:
#             name = input(f"Previous[{self.name}]. Name (Required field): ")
#             if len(name) > 0:
#                 break
#         surname = input(f"Previous[{self.surname}]. Last name:  ")
#         bd = input(f"Previous[{self.date_of_birth}]. Birth day in 'dd.mm.yyyy' format: ")

#         executable_command = """UPDATE users
#         SET name = %s, surname = %s, date_of_birth = %s
#         WHERE email = %s 
#         RETURNING name, surname, date_of_birth"""
#         values = (name, surname, bd, self.email)

#         try:
#             fetchedData = dbconnection.fetchOne(executable_command, values)
#             if len(fetchedData) != 0:
#                 (name, surname, bd) = fetchedData[0]
#                 self.name = name
#                 self.surname = surname
#                 self.date_of_birth = bd
#                 print("Successfully updated user information.")
#             else:
#                 print("Some error. Try again.")
#         except Exception as e:
#             print(e)

#     def delete(self, dbconnection):
#         executable_command = '''DELETE FROM users WHERE email = %s'''
#         values = (self.email,)
#         try:
#             fetchedData = dbconnection.perform(executable_command, values)
#             print("Successfully deleted your account from database.")
#         except Exception as e:
#             print(e)

# class App:

#     def __init__(self, db):
#         self.DBEngine = db

#     def loggedIn(self, user):
#         while True:
#             choice = input("\n***********\nUpdate - 1\nInfo - 2\nLogout - 3\nDelete account - 4\n\nExit - 0\n***********\n")
#             if choice == "1":
#                 user.update(self.DBEngine)
#             elif choice == "2":
#                 print(user)
#             elif choice == "3":
#                 del(user)
#                 break
#             elif choice == "4":
#                 sure = input("\n***********\nAre you sure you want to delete your account?\nYes - Y\nNo - n\n***********\n")
#                 if sure == "Y":
#                     user.delete(self.DBEngine)
#                     del(user)
#                     break
#                 else:
#                     print("You cancelled account deletion.")
#             else:
#                 exit()

#     def start(self):
#         while True:
#             choice = input("\n***********\nRegister - 1\nLogin - 2\n\nExit - 0\n***********\n")
#             if choice == "1":
#                 #registration logic
#                 user = User.register(self.DBEngine)
#                 if user != None:
#                     self.loggedIn(user)
#             elif choice == "2":
#                 #login logic
#                 user = User.login(self.DBEngine)
#                 if user != None:
#                     self.loggedIn(user)
#             else:
#                 exit()

# def main():
#     db = DBConnection()
#     app = App(db)

#     app.start()

# if __name__ == '__main__':
#     main()

# import socket

# HOST, PORT = '', 8888

# listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# listen_socket.bind((HOST, PORT))
# listen_socket.listen(1)
# print(f'Serving HTTP on port {PORT} ...')
# while True:
#     client_connection, client_address = listen_socket.accept()
#     request_data = client_connection.recv(1024)
#     print(request_data.decode('utf-8'))
#     a = 'Aigerim'

#     http_response = b"""\
# HTTP/1.1 200 OK

# Hello, World! %s
# """ % a
#     client_connection.sendall(http_response)
#     client_connection.close()