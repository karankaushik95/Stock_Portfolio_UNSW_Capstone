import sqlite3
from flask_login import LoginManager, UserMixin


class LoginService():

    def __init__(self):
        self.session_users = []

    def user_exists(self, email):
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

    def login_session_user(self, user):
        self.session_users.append(user)
        
    def logout_session_user(self, user):
        self.session_users.remove(user)

    def check(self, email, password):

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
            print(emails[i][0], passwords[i][0])
            if email == emails[i][0]:
                if password == passwords[i][0]:
                    return True
        return False

    def new_user(self, name, email, password):
        print("Creating new user: ", email, password)
        connection = sqlite3.connect('db/users.db')
        cursor = connection.cursor()
        sql = """ INSERT INTO users VALUES ("{}", "{}", "{}");"""
        query = sql.format(name, email, password)
        cursor.execute(query)
        connection.commit()
        connection.close()

    def get_user(self, email):
        for user in self.session_users:
            if (user.email == email):
                return user
        return None


class User(UserMixin):

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
