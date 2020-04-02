import psycopg2

connection = psycopg2.connect(database="pc", user="user", password="pass", host="localhost", port="5432")

cursor = connection.cursor()


query = """INSERT INTO computers(hard_drive, processor, amount_of_ram, maximum_ram, hard_drive_capacity, form_factor)
            VALUES
            ('SATA','Celeron','4GB','8GB','220GB','Mini');

"""

cursor.execute(query)
connection.commit()