import mysql.connector

class Zoo:
    def __init__(self):
        # Connect to MySQL database
        self.cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='zoo')
        self.cursor = self.cnx.cursor()

    def __del__(self):
        # Close MySQL connection
        self.cursor.close()
        self.cnx.close()

    def add_animal(self, id_animal, name, breed, cage_id, birth_date, origin_country):
        # Insert new animal into database
        query = "INSERT INTO animal (id_animal, name, breed, cage_id, birth_date, origin_country) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (1, "gazelle", "carnivore", 1, "02-09-2000", "Tchad")
        self.cursor.execute(query, values)
        self.cnx.commit()

    def delete_animal(self, id_animal):
        # Delete animal from database
        query = "DELETE FROM animal WHERE id_animal = %s"
        values = (id_animal,)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def update_animal(self, id_animal, name=None, breed=None, cage_id=None, birth_date=None, origin_country=None):
        # Update animal information in database
        query = "UPDATE animal SET "
        values = []
        if name:
            query += "name = %s, "
            values.append(name)
        if breed:
            query += "breed = %s, "
            values.append(breed)
        if cage_id:
            query += "cage_id = %s, "
            values.append(cage_id)
        if birth_date:
            query += "birth_date = %s, "
            values.append(birth_date)
        if origin_country:
            query += "origin_country = %s, "
            values.append(origin_country)
        # Remove last comma and space from query
        query = query[:-2] + " WHERE id_animal = %s"
        values.append(id_animal)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def add_cage(self, id_cage, area, capacity):
        # Insert new cage into database
        query = "INSERT INTO cage (id_cage, area, capacity) " \
                "VALUES (%s, %s, %s)"
        values = (id_cage, area, capacity)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def delete_cage(self, id_cage):
        # Delete cage and animals inside from database
        query = "DELETE FROM animal WHERE cage_id = %s"
        values = (id_cage,)
        self.cursor.execute(query, values)
        query = "DELETE FROM cage WHERE id_cage = %s"
        values = (id_cage,)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def update_cage(self, id_cage, area=None, capacity=None):
        # Update cage information in database
        query = "UPDATE cage SET "
        values = []
        if area:
            query += "area = %s, "
            values.append(area)
        if capacity:
            query += "capacity = %s, "
            values.append(capacity)
        # Remove last comma and space from query
        query = query[:-2] + " WHERE id_cage = %s"
        values.append(id_cage)
        self.cursor.execute(query, values)
       
animal = Zoo()
animaux = Zoo()
animal.add_animal(1, "gazelle", "carnivore", 1, "02-09-2000", "Tchad")
animaux.add_animal(2, "lion", "carnivore", 1, "03-09-2000", "Tchad")
animal.delete_animal(1)
animal.update_animal(1, name="gazelle", breed="carnivore", cage_id=1, birth_date="02-09-2000", origin_country="Tchad")