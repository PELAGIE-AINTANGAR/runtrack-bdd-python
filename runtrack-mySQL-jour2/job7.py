# import mysql.connector

# class Salaries:

#     def __init__(self, host, user, password, database):
#         self.conn = mysql.connector.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=database
#         )
#         self.cursor = self.conn.cursor()

#     def create(self, nom, prenom, salaire, id_service):
#         query = "INSERT INTO salariee (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
#         values = (nom, prenom, salaire, id_service)
#         self.cursor.execute(query, values)
#         self.conn.commit()

#     def read(self, id):
#         query = "SELECT * FROM salariee WHERE id = %s"
#         values = (id,)
#         self.cursor.execute(query, values)
#         return self.cursor.fetchone()

#     def update(self, id, nom, prenom, salaire, id_service):
#         query = "UPDATE salariee SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
#         values = (nom, prenom, salaire, id_service, id)
#         self.cursor.execute(query, values)
#         self.conn.commit()

#     def delete(self, id):
#         query = "DELETE FROM salariee WHERE id = %s"
#         values = (id,)
#         self.cursor.execute(query, values)
#         self.conn.commit()

#     def get_all(self):
#         query = "SELECT * FROM salariee"
#         self.cursor.execute(query)
#         return self.cursor.fetchall()


# salaries = Salaries("localhost", "root", "root", "entreprise")

# # Ajouter un nouveau salarié
# salaries.create("Doe", "John", 3000.50, 1)

# # Récupérer les informations d'un salarié
# salarié = salaries.read(1)
# print(salarié)

# # Mettre à jour les informations d'un salarié
# salaries.update(1, "Doe", "John", 3500.00, 1)

# # Supprimer un salarié
# salaries.delete(1)

# # Récupérer tous les salariés
# tous_les_salaries = salaries.get_all()
# print(tous_les_salaries)



import mysql.connector

class Entreprise:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='entreprise')
        self.cursor = self.cnx.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Employé {nom} {prenom} ajouté avec succès !")

    def read_employes(self):
        query = "SELECT e.nom, e.prenom, e.salaire, s.nom FROM employes e JOIN services s ON e.id_service = s.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update_employe(self, id, nom, prenom, salaire, id_service):
        query = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (nom, prenom, salaire, id_service, id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Employé avec l'ID {id} modifié avec succès !")

    def delete_employe(self, id):
        query = "DELETE FROM employes WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Employé avec l'ID {id} supprimé avec succès !")

    def create_service(self, nom):
        query = "INSERT INTO services (nom) VALUES (%s)"
        values = (nom,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Service {nom} ajouté avec succès !")

    def read_services(self):
        query = "SELECT * FROM services"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update_service(self, id, nom):
        query = "UPDATE services SET nom = %s WHERE id = %s"
        values = (nom, id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Service avec l'ID {id} modifié avec succès !")

    # def delete_service(self, id):
    #     query = "DELETE FROM services WHERE id = %s"
    #     values = (id,)
    #     self.cursor.execute(query, values)
    #     self.conn.commit()
    #     print(f"Service avec l'ID {id} supprimé avec succès !")
        
    def delete_service(self, id_service):
    # Vérifier s'il y a des employés associés au service
        self.cursor.execute("SELECT COUNT(*) FROM employes WHERE id_service = %s", (id_service,))
        count = self.cursor.fetchone()[0]
        if count > 0:
        # S'il y a des employés, demander à l'utilisateur s'il veut les supprimer ou mettre à jour leurs id_service
            print("Il y a {} employé(s) associé(s) à ce service.".format(count))
            action = input("Voulez-vous supprimer ces employés (s) ou mettre à jour leurs ID de service (m) ? ")
            
            if action == "s":
            # Supprimer tous les employés associés au service
                self.cursor.execute("DELETE FROM employes WHERE id_service = %s", (id_service,))
            elif action == "m":
            # Mettre à jour les ID de service de tous les employés associés au service
                new_id = input("Entrez le nouvel ID de service: ")
                self.cursor.execute("UPDATE employes SET id_service = %s WHERE id_service = %s", (new_id, id_service))
                self.cnx.commit()
        else:
            print("Action invalide.")
            #return

    # Supprimer le service une fois tous les employés associés supprimés ou mis à jour
        self.cursor.execute("DELETE FROM services WHERE id = %s", (id_service,))
        self.cnx.commit()
        print("Service supprimé avec succès !")

        
entreprise = Entreprise("localhost", "root", "root", "entreprise")

# créer un employé
entreprise.create_employe("Doe", "John", 3000.50, 1)

# lire tous les employés avec leur service respectif
entreprise.read_employes()

# modifier un employé
entreprise.update_employe(1, "Doe", "Jane", 3500, 1)
entreprise.delete_employe(1)
entreprise.create_service("Comptabilité")
entreprise.read_services()
entreprise.update_service(1, "Comptabilité et Finance")
entreprise.delete_service(1)

