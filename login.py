import db_connection
import user


class Login:
    def __init__(self):
        self.choice = None
        self.user = user.User()

        #initialize connection
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

    
    def display_login_choices(self):
        self.choice = int(input("If you are an existing user enter [0] | If you would like to create an account enter [1]:\n"))

    def create_account(self):
        account_created = 0

        while (account_created != 1):
            self.user.set_first_name()
            self.user.set_last_name()

            valid_email = self.user.set_email(0) #0 indicates check for email already in-use.

            if(valid_email == 1):
                #add account to DB
                cursor = self.connection.cursor()
                cursor.execute('''
                                INSERT INTO "User" (email, first_name, last_name)
                                VALUES (%s, %s, %s);
                                ''', (self.user.email, self.user.first_name, self.user.last_name))
                print("Account created!")
                account_created = 1
                cursor.close()
            else:
                print("Email already exists, please try again.")

    def login_account(self):
        logged_in = 0

        while(logged_in != 1):
            email = self.user.set_email(1) #1 indicates don't check for email already in-use.
            #check email exists & get user's first and last name.
            cursor = self.connection.cursor()
            cursor.execute('''
                            SELECT first_name, last_name
                            FROM "User"
                            where "User".email = %s;
                            ''', (email,))
            result = cursor.fetchone()
            cursor.close()

            if result is None:
                print("Invalid email, please try again.")
            else:
                first_name = result[0]
                last_name = result[1]
                print ("welcome back ", first_name, last_name, "!")
                logged_in = 1

    def login_flow(self):
        self.display_login_choices()

        if(self.choice == 0): #existing user
            self.login_account()
            self.connection.close()

        elif(self.choice == 1):  #new user
            self.create_account()
            self.connection.commit()
            self.connection.close()

        else:
            print("Enter a valid choice")
    