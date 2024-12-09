import psycopg

class Connect():
    def __init__(self):
        self.connection = psycopg.connect(
            dbname="CS457_FP",
            user="postgres",
            password="password",
            host="127.0.0.1",
            port="5432"
        )

    def get_connection(self):
        return self.connection
