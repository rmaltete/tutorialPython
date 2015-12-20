# -*- coding: UTF-8 -*-
# fichier : exo_chaine_1.py by J.Tschanz
# fonction : quelques opérations sur les chaînes.

# déclarations
s1 = 'Hello World'
s2 = " I'm here !!"
s3 = """Python is a good programming
language !!""" # sur plusieurs lignes !!

# opérations

print "Concaténation : " 
print s2+s1
print "Répétition : " 
print s1*4

"Longueur d'une chaîne : " 
print s3, len(s3)

"Insertion : "
print "I told you : %s" % s1
# fin du fichier exo_chaine_1.py