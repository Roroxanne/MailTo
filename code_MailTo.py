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
            body = email.message_from_string(mess.as_string())
            for payload in body.get_payload():
                print('body:', body)
            for i in mess['from']:
                ligne = mess['from']
                text = ligne.split() #sépare le texte par mot dans une liste
                prenom = text[0] #prend le premier élément de la liste qui est le Prénom
                nom = text[1] #prend le nom
                adresse= text[2] #prend l'adresse
            # print(f"[{prenom}, {nom}, {adresse}]") -> test pour voir si le code est bon et prend bien les mots