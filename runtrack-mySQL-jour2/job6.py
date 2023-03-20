import mysql.connector

# Se connecter à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)

# Exécuter la requête SQL
cursor = db.cursor()
cursor.execute("SELECT SUM(capacite) AS total_superficie FROM salles;")
result = cursor.fetchone()

# Afficher le résultat
print(f"La capacite de tous les salles est de {result[0]} ")

# Fermer la connexion à la base de données
db.close()