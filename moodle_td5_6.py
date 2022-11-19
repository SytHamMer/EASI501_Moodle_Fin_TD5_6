#NE PAS MODIFIER LES FONCTIONS
#JUSTE LES VALEURS EN BAS SOUS LE if __name__ == '__main__':

#NE PAS VALIDER LES REPONSES EN 1 MINUTE SUR LE MOODLE ON VA ETRE GRILLER


#JE NE GARANTIS PAS LE 100% DE REUSSITE ET JE SUIS EN AUCUN CAS RESPONSABLE DE VOTRE ECHEC
#SI VOUS ETES PAS CONTENT APPRENEZ LE COURS ET FAITES LE POUR DE VRAI !
#CA MARCHE PAS FORCEMENT REGARDEZ LE SUJET
from math import exp
from math import log
from math import pi, cos, sin, radians
from math import sqrt
from math import atan
from math import degrees

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


def ex2(i_Veff, i_Omega, i_angle, v_Veff, v_Omega, v_angle):

    yEq_exp_val = i_Veff / v_Veff
    yEq_exp_angle = i_angle - v_angle

    yEq_carte_real_part = yEq_exp_val * cos( radians(yEq_exp_angle) )
    yEq_carte_im_part = yEq_exp_val * sin( radians(yEq_exp_angle) )

    q7 = 1 / (yEq_carte_im_part*-1 * i_Omega ) * 1000
    print(f'Q7 : {q7} mH')

    q8 = 1 / yEq_carte_real_part
    print(f'Q8 : {q8} ohm')
def ex3(Condo,Resist,v_Veff,v_Omega):
    Zeq_carte_real_part = Resist
    Zeq_carte_im_part = -1/((Condo*10**(-6))*v_Omega)

    Zeq_exp_val_part = sqrt(Zeq_carte_real_part**2+Zeq_carte_im_part**2)
    Zeq_exp_angle_part = degrees(atan(Zeq_carte_im_part/Zeq_carte_real_part))

    i_exp_val_part = v_Veff/Zeq_exp_val_part
    i_exp_angle_part = 0-Zeq_exp_angle_part
    vr_Veff = Resist*i_exp_val_part

    q9 = i_exp_val_part
    print(f'Q9 : {q9} A')
    q10 = vr_Veff
    print(f'Q10 : {q10} V')
    q11 = i_exp_angle_part
    print(f'Q11 : {q11} °')

if __name__ == '__main__':
    #Mettre les valeurs dans les mêmes unités que proposer par exemple
    # pour 11.4mH -> écrire 11.4
    #SI CHIFFRE A VIRGULE C'EST UN POINT A METTRE !!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Pour l'exo 1 mettre aussi Tp (valeur en question 3)
    #Pour l'exo 1 mettre aussi R (valeur en question 4)


    #ex1(Ke en V, Ke en tr/min , I en A, Tp (Q3) en Nm, R (Q4) en Kohm, vit_rota (Q4) en tr/min )
    # ex1(27, 1000, 5.2, 0.3, 1.2, 1430)

    #ATTENTION AUX UNITES QUE JE DEMANDE
    #la réponse est toujours donnée dans l'unité demandé ex q7 en ms
    #ATTENTION : pour i_Omega ET v_Omega si 100*pi -> Mettre 100*pi
    #ex2(i_Veff, i_Omega, i_angle , v_Veff, v_Omega,uc2 en V)
    ex2(8.2, 100*pi, -35, 230, 100*pi, 0)


    #ATTENTION : pour i_Omega ET v_Omega si 100*pi -> Mettre 100*pi
    #ex3(Condo,Resist,v_Veff,v_Omega)
    ex3(122,33,230,100*pi)


