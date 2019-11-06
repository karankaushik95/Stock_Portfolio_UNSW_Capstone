import sqlite3
#from flask_login import login_manager

class LoginService():

    @staticmethod
    def user_exists(email):
        connection = sqlite3.connect('db/users.db')
        cursor = connection.cursor()
        sql_command = """ SELECT email FROM users;"""
        cursor.execute(sql_command)
        existing_emails = cursor.fetchall()
        connection.close()
        for existing_email in existing_emails:
            if email == existing_email[0]:
                return True
        return False

    @staticmethod
    def check(email, password):

        connection = sqlite3.connect('db/users.db')
        cursor = connection.cursor()
        sql_command = """ SELECT email FROM users;"""
        cursor.execute(sql_command)
        emails = cursor.fetchall()

        sql_command = """ SELECT password FROM users;"""
        cursor.execute(sql_command)
        passwords = cursor.fetchall()

        connection.close()

        # Note the length of emails will be the same as passwords, ie: the number of users
        for i in range(len(emails)):
            print(emails[i][0])
            if email == emails[i][0]:
                if password == passwords[i][0]:
                    return True
        return False

    @staticmethod
    def new_user(name, email, password):
        connection = sqlite3.connect('db/users.db')
        cursor = connection.cursor()
        sql = """ INSERT INTO users VALUES ("{}", "{}", "{}");"""
        query = sql.format(name, email, password)
        cursor.execute(query)
        connection.commit()
        connection.close()
        
    @staticmethod
    def load_user(self, user_id):
        if (self.user_exists(user_id)):
            return User(user_id)
        else:
            return None
    
class User():
    
    def __init__(self, user_id):
        self.email = user_id
        
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return True
    
    def get_id(self):
        return self.email