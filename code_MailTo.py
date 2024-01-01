from simplegmail import Gmail 
import pandas as pd

gmail = Gmail()

objet_recherche = gmail.get_messages(query="subject:(Question* OR Rattrapage* OR Devoir*")

data = {
    "Objet": [],
    "le_mail": [],
    "adresse_mail": [],
    "receveur":[]
}


for message in objet_recherche:
    sender = message.sender
    adresse = sender.split()
    adresse_separee = adresse[2]
    body = message.plain
    objet_du_mail = message.subject
    receveur = message.recipient
    data["Objet"].append(objet_du_mail)
    data["le_mail"].append(body)
    data["adresse_mail"].append(adresse_separee)
    data["receveur"].append(receveur)

objet_recherche2 = gmail.get_messages(query="subject:Contact")

data2 = {
    "Adresse": [],
    "Nom": [],
    "Prenom":[],
    "Année":[],
    "Lycée": []
}


for message in objet_recherche2:
    sender = message.sender
    adresse = sender.split()
    adresse_separee = adresse[2]
    body = message.plain
    nom_split = body.split()
    if len(nom_split)==4:
        prenom, nom, annee, lycee = nom_split
        data2["Adresse"].append(adresse_separee)
        data2["Nom"].append(nom)
        data2["Prenom"].append(prenom)
        data2["Année"].append(annee)
        data2["Lycée"].append(lycee)
        

dataframe_contact = pd.DataFrame(data2)
df = pd.DataFrame(data)
df['le_mail'] = df['le_mail'].str.replace('\r', '').str.replace('\n', '')
pd.display(df)
pd.display(dataframe_contact)



  