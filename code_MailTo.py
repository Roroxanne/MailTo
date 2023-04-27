import imaplib

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("roro.enzo.test@gmail.com","pnrbwptkjsvevasv") #se connecter

mail.select("Inbox") #acceder aux mail qu'on reçoit

clé = "FROM" #prendre comme clé FROM
valeur = "roxanne.galura@gmail.com" # dans from prendre une adresse
résultat, data = mail.search(None, clé, valeur) #va donc rechercher l'adresse

mail_id_list = data[0].split() #obtient les id des messages et les sépare

