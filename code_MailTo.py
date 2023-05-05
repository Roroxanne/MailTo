import imaplib
import email
import csv

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
            print("subj:", mess["subject"]) #print l'objet
            print("from:", mess["from"]) #print par qui
            body = email.message_from_string(mess.as_string())
            for payload in body.get_payload():
                if payload.get_content_type() == 'text/plain': #affichera juste le message
                    print(payload.get_payload())
            for i in mess['from']:
                mail = mess['from']
                text = mail.split() #décompose le texte par mot, dans une liste
            print(text[2])

with open("table.csv", "w", encoding="UTF8") as fichier: #création du fichier csv
    writer = csv.writer(fichier)