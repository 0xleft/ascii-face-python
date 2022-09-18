import pygame
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
pygame.init()

def main():
    letters_numbers, counts = [], []
    with open('abc.txt', "r") as file:
        abc = file.readline().strip()
        abc = [str(letter) for letter in abc]
    #abc = ["a", "b", "c", "d"]
    for letter in abc:
        img = cv2.imread("16_16.png")
        img = cv2.putText(img, letter, (4,12), cv2.FONT_HERSHEY_PLAIN, fontScale=0.7, color=(0, 0, 0), thickness=1)
        img_list = list(np.array(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)))
        count_list = [count for row in img_list for count in row if count == 0]
        letters_numbers.append((len(count_list), letter))


    letters_numbers.sort()
    letters = [letter[1] for letter in letters_numbers]
    letters_n = [letter[0] for letter in letters_numbers]
    print(letters_n)
    print(letters)
    print(sum(letters_n)/len(letters_n), "avg")
    plt.bar(letters, letters_n)
    plt.show()



if __name__ == "__main__":
    main()
    pygame.quit()