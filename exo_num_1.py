# -*- coding: UTF-8 -*-
# fichier : exo_num_1.py by J.Tschanz
# fonction : quelques opérations sur les nombres.

nbr_1 = 3 # entier normal
nbr_2 = 999999999L # entier long
nbr_3 = 1.24 # virgule flottante
nbr_4 = 0xff # nombre hexa.
nbr_5 =  25 + 4.0j # complexe
nbr_6 = 4

# simple calculs !!

print "Un entier sur un flottant : %s " % (nbr_1/nbr_3)
print "Un hexa + un complexe : %s " % (nbr_4+nbr_5)
print "Un long - (un entier * un hexa.) : %s " % (nbr_2 - nbr_1*nbr_4)
print "Une puissance : %s " % (nbr_3**nbr_1) # puissance
print "Un entier sur un entier !? : %s" % (nbr_6/nbr_1) # attention entier divisé par un entier
print "Un modulo avec un réel : %s " % (nbr_6%nbr_3) # modulo avec un réel 

# fin du fichier exo_num_1.py