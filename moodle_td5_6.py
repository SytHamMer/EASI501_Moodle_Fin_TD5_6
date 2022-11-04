#NE PAS MODIFIER LES FONCTIONS
#JUSTE LES VALEURS EN BAS SOUS LE if __name__ == '__main__':

#NE PAS VALIDER LES REPONSES EN 1 MINUTE SUR LE MOODLE ON VA ETRE GRILLER


#JE NE GARANTIS PAS LE 100% DE REUSSITE ET JE SUIS EN AUCUN CAS RESPONSABLE DE VOTRE ECHEC
#SI VOUS ETES PAS CONTENT APPRENEZ LE COURS ET FAITES LE POUR DE VRAI !
#CA MARCHE PAS FORCEMENT REGARDEZ LE SUJET
from math import exp
from math import log
from math import pi

# A voir si on prend math.pi OU 3.14

def ex1(Ke_V, Ke_tr_min, i, Tp, R, vit_rota):
    # Q2 : Te => couple Electromagnétique
    Kt = (Ke_V / Ke_tr_min) * (30 / 3.14)
    q2 = Kt * i
    print(f'Q2 : {q2} Nm')

    # Q3 : Tu => Couple Utile
    q3 = q2 - Tp
    print(f'Q3 : {q3} Nm')

    # Q4 : U => Tension d'alimentation
    q4 = Kt * (vit_rota * ( 3.14 /30 )) + R * i
    print(f'Q4 : {q4} V ')

    # Q5 : Pu => Puissance Utile
    q5 = q3 * (3.14 / 30) * vit_rota
    print(f'Q5 : {q5} W')

    # Q6 : r => Rendement du moteur
    q6 = q5 / (q4 * i)
    print(f'Q6 : {q6} ')


# TO DO !
# def ex2(e,r1,r2,c,uc1,uc2):
#
#     q7= (r1*c)/1000
#     print(f'Q7 : {q7} ms')
#     q8=-q7*log((uc2-e)/(uc1-e))
#     print(f'Q8 : {q8} ms')
#     q9=(uc1-e)*exp(-q8/(2*q7))+e
#     print(f'Q9 : {q9} V')
#     q10=(r2*c)/1000
#     print(f'Q10 : {q10} ms')
#     q11=-q10*log(uc1/uc2)+q8
#     print(f'Q11 : {q11} ms')
#     t2 = -(q11-q8)/2
#     q12=uc2*exp(t2/q10)
#     print(f'Q12 : {q12} V')



if __name__ == '__main__':
    #Mettre les valeurs dans les mêmes unités que proposer par exemple
    # pour 11.4mH -> écrire 11.4
    #SI CHIFFRE A VIRGULE C'EST UN POINT A METTRE !!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Pour l'exo 1 mettre aussi Tp (valeur en question 3)
    #Pour l'exo 1 mettre aussi R (valeur en question 4)


    #ex1(Ke en V, Ke en tr/min , I en A, Tp (Q3) en Nm, R (Q4) en Kohm, vit_rota (Q4) en tr/min )
    ex1(27, 1000, 5.2, 0.3, 1.2, 1430)

    #ATTENTION AUX UNITES QUE JE DEMANDE
    #la réponse est toujours donnée dans l'unité demandé ex q7 en ms
    #ex2(E en V,r1 en kohm,r2 en kohm ,c en nF,uc1 en V,uc2 en V)
    # ex2(12, 1.2, 2.7, 665, 2.6, 9.0)

