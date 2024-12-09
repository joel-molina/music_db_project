import db_connection
import cursor_results

class User:
    def __init__(self):
        self.email = None
        self.first_name = None
        self.last_name = None

        #initialize connection
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

    def set_email(self, new_or_existing):
        self.email = input("Enter your email: ")

        #check that email does not already exist.
        if(new_or_existing == 0): #0 meaning new
            cursor = self.connection.cursor()
            cursor.execute('''
                            SELECT "User".email
                            FROM "User"
                            WHERE "User".email = %s;
                            ''', (self.email,))
            result = cursor.fetchone()

            #cursor result to object
            cursorResult = cursor_results.Email()
            cursorResult.convert_email_result(result)

            cursor.close()
            self.connection.close()

            if cursorResult.email is None:
                return 1 #valid email.
            else:
                return 0 #invalid email.
        
        #existing user, return the email.
        return self.email
        

    def set_first_name(self):
        self.first_name = input("Enter your first name: ")


    def set_last_name(self):
        self.last_name = input("Enter your last name: ")