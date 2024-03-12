from Voiture1 import *

if __name__ == "__main__":
    mycar1 = Voiture("renault", "modus", "4", "grise")
    mycar2 = Voiture("C4picasso","4","bleu") #Poistionnement
    mycar3 = Voiture(modele ="c3", PuissanceFiscale="4", couleur="vert") #argumentnommé
    mycar4 = Voiture("citroën","C4picasso","4",couleur="vert")

    #print(mycar1.marque, mycar1.modele, mycar1.puissance_fiscal, mycar1.couleur)
    #print(mycar2.marque, mycar2.modele, mycar2.puissance_fiscal, mycar2.couleur)
    #print(mycar3.marque, mycar3.modele, mycar3.puissance_fiscal, mycar3.couleur)
    #print(mycar4.marque, mycar4.modele, mycar4.puissance_fiscal, mycar4.couleur)

    print(mycar1.get_marque())
    mycar1.set_marque("peugot")
    print(mycar1.get_marque())
    mycar1.set_options(1)

    mycar3.__str__()