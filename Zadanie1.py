from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def main():
    image = Image.open("Lemon.bmp") #Wczytanie obrazu Lemon.bmp, przypisanie go do zmiennej image
    imageArray = np.asarray(image) #przetworzenie obrazu w zmiennej image na tablicę, przypisanie jej do zmiennej imageArray
    
    plt.imshow(imageArray, cmap=cm.gray, vmin=0, vmax=255) #przygotowuje obraz do wyświetlenia. Dodatkowe argumenty są ignorowane, ponieważ jest to obraz RGB, ale umożliwiłyby prawidłowe wyświetlenie w przypadku obrazu grayscale
    plt.show() #wyświetla przygotowany obraz w oknie

    width, height = image.size #pobiera wartości wysokości i szerokości obrazu do zmiennych
    image = image.resize((int(width*0.5), int(height*0.5))) #skaluje obraz do połowy rozdzielczości
    image = image.convert("L") #konwertuje obraz na grayscale
    image = image.rotate(90, expand = 1) #obraca obraz o 90 stopni w prawo. Argument expand = 1 sprawia, że nowy obraz będzie miał poprawne wymiary
    
    imageArray = np.asarray(image)
    plt.imshow(imageArray, cmap=cm.gray, vmin=0, vmax=255) #tutaj dodatkowe argumenty są konieczne, by obraz nie został wyświetlony jako pseudokolorowy
    plt.show()

    print(str(imageArray)) #wypisuje w skrócony sposób macierz obrazu w postaci tablicy. Jest to obraz grayscale, więc tablica ta jest dwuwymiarowa
    
    #Poniższy kod wypisuje całość macierzy w terminalu
    #
    #y, x = imageArray.shape
    #for i in range(y):
    #    for j in range(x):
    #        print(imageArray[i][j], end=" ")
    #    print()

if __name__ == "__main__":
    main()