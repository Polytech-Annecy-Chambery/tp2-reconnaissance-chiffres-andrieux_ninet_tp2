from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    prop_max = 0
    indice_max = 0
    image_binarisee = image.binarisation(S)
    image_localisee = image_binarisee.localisation()
    for i in range (0,len(liste_modeles)):
        image_resizee = image_localisee.resize(liste_modeles[i].H, liste_modeles[i].W)
        proportion  = image_resizee.similitude(liste_modeles[i])
        if proportion > prop_max:
            prop_max = proportion
            indice_max = i
    return indice_max
