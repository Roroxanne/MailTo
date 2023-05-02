import imaplib
import email

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("roro.enzo.test@gmail.com","pnrbwptkjsvevasv") #se connecter

mail.select("Inbox") #acceder aux mail qu'on reçoit

clé = "SUBJECT" #prendre comme clé FROM
valeur = "Contact" # dans from prendre une adresse
résultat, data = mail.search(None, clé, valeur) #va donc rechercher l'adresse

mail_id_list = data[0].split() #obtient les id des messages et les sépare

messages = [] #creer liste pour mettre les infos
for num in mail_id_list:
    résultat, data = mail.fetch(num, "(RFC822)")
    messages.append(data)

for info in messages:
    for response_part in info:
        if type(response_part) is tuple:
            mess = email.message_from_bytes(response_part[1])
            print("subj:", mess["subject"])
            print("from:", mess["from"])
            print("body:")
            for i in mess['from']:
                mail = mess['from']
                po = mail.split() #decompose le text par mot dans une liste
            print(po[2]) #affiche les mails
