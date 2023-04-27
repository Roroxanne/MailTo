import smtplib 

serveur = smtplib.SMTP_SSL("smtp.gmail.com", 465)
serveur.login("notre_email", "mot_de_passe")
