import mysql.connector

# Se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="LaPlateforme"
)

# Créer un curseur pour exécuter des commandes SQL
mycursor = mydb.cursor()

# Exécuter la commande SQL SELECT
mycursor.execute("SELECT * FROM salles")

# Récupérer les résultats de la commande SELECT
resultats = mycursor.fetchall()

# Afficher les résultats
for resultat in resultats:
  print(resultat[0], resultat[1])
