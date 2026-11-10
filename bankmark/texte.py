def analyser_modalites(texte) : 
    modalites = {}
    morceaux = texte.split(';')
    for morceau in morceaux : 
        morceau = morceau.strip()
        if not morceau : 
            continue

        gauche, separateur, droite = morceau.partition(':')
        if not separateur:
            raise ValueError(f"Format de modalité invalide : {morceau}")
        cle = gauche.strip()
        valeur = droite.strip()
        modalites[cle] = valeur

    return modalites

def analyser_ligne_codebook(lignes) :
    return 0

def lire_codebook() :
    return 0

def decouper_ligne(ligne) : 
    return 0

def est_entier(texte) :
    return 0

def numero_mois(abrev) : 
    return 0

def fiche_contact(codebook, entete, valeurs) :
    return 0

def histogramme_texte(effectifs, largeur) :
    return 0