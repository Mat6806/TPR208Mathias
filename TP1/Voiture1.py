class Voiture:
    def __init__(self, marque ="toyota", modele="prius", PuissanceFiscale="3", couleur="bleu", option=""):
        self.__marque = marque
        self.__modele = modele 
        self.__puissance_fiscal = PuissanceFiscale
        self.__couleur = couleur
        self.__option = []

    def get_marque(self):
        return (self.__marque)

    def set_marque(self,marque):
        if isinstance(marque,str):
            self.__marque = marque 
    
    def get_options(self):
        return (self.__option)
    
    def set_options(self):
        if isinstance([], list):
            self.__option = []
            
    def suppr_options(self):
        **
    
    def __str__(self):
        print("- marque :", self.__marque,"\n", "- modele :",self.__modele,"\n","- puissance :",self.__puissance_fiscal,"\n", "- couleur :",self.__couleur, "\n", "- options :", self.__option)