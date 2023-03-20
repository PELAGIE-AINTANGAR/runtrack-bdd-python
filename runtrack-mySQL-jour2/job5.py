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
cursor.execute("SELECT SUM(superficie) AS total_superficie FROM etage;")
result = cursor.fetchone()

# Afficher le résultat
print(f"La superficie de La Plateforme est de {result[0]} m2")

# Fermer la connexion à la base de données
db.close()
