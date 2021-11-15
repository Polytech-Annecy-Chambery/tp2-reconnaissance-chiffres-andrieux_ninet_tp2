import matplotlib.pyplot as plt
from image import Image
from reconnaissance import reconnaissance_chiffre, lecture_modeles


if __name__ == '__main__':

    # Variables utiles
    path_to_assets = '../assets/'
    plt.ion() # Mode interactif de matplotlib our ne pas bloquer l'éxécutions lorsque l'on fait display

    #==============================================================================
    # Lecture image et affichage
    #==============================================================================
    image = Image()
    image.load(path_to_assets + 'test4.JPG')
    image.display("Exemple d'image")
    S = 70
    liste_modeles = lecture_modeles(path_to_assets)
    chiffre = reconnaissance_chiffre(image, liste_modeles, 70)
    print("Le chiffre reconnu est : ", chiffre)
