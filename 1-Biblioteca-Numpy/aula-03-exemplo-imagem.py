from skimage import io
import numpy as np
import matplotlib.pyplot as plt

# Carregamento da imagem
img = io.imread('./images/numpy-logo.jpg') 

# todos os pixels da imagem
print(f'Todos os pixels da imagem da logo do numpy --> \n{img}\n')

# Shape dessa imagem, ou seja, o formato, as dimensões, quantos pixels ela tem etc...
print(f'Shape da imagem da logo do numpy --> \n{img.shape}\n')

# vamos criar uma nova imagem com um pedaço da imagem original da logo do numpy:
nova_img = img[0:256]

# vamos criar uma nova imagem com um pedaço vertical da imagem original da logo do numpy:
nova_img2 = img[:, 0:250]

pergunta = int(input("Qual imagem você deseja ver? \nDigite 1, 2 ou 3: \n"))

if (pergunta == 1):
    # Exibição da imagem:
    plt.imshow(img)
    plt.show()
elif (pergunta == 2):
    # Exibição da nova imagem:
    plt.imshow(nova_img)
    plt.show()
elif (pergunta == 3):
    # Exibição da nova imagem 2:
    plt.imshow(nova_img2)
    plt.show()
else:
    print('Você não digitou um valor válido... DIGITE NOVAMENTE!\n')
    pergunta = int(input("Qual imagem você deseja ver? \nDigite 1, 2 ou 3: \n"))
    
    