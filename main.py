from pygame.time import Clock
from camera import *
import numpy

#print(chr(27) + "[2J")

clock = Clock()
cam = Camera()


def main():
    picture_dimensions=(256,256)
    symbols = [' ','.', "'", '`', ',', ':', '_', '-', 'I', 'l', '"', '1', '~', ';', 'i', 'r', 'v', '(', ')', '/', '?', 'Y', '\\', '|', '<', '>', 'J', '^', '!', '+', '7', 'L', 'T', 'f', 't', 'x', 'c', 'j', '{', '}', '=', 'V', '[', ']', 'k', 'n', 'o', 'u', 'y', '4', 'A', 'C', 'F', 'a', 'e', 's', 'z', '*', 'K', 'X', 'h', '2', 'U', 'Z', 'w', '0', '5', 'H', 'P', 'S', '3', 'G', 'O', 'm', 'D', 'E', 'N', 'b', 'd', 'p', 'q', '6', '9', 'Q', 'R', '&', '8', 'W', 'g']
    while not cv2.waitKey(1) & 0xFF == ord('q'):
        frame = list(numpy.array(cv2.resize(cam.transformFrame(cam.readFrame()), picture_dimensions, fx=0.2, fy=0.2)))
    
        frame = [symbols[int(item/255*(len(symbols)-1))] for row in frame for item in row]
        [print(frame[i*picture_dimensions[0]:(i+1)*picture_dimensions[0]]) for i in range(0, picture_dimensions[1])]
        cv2.imshow("nice", cv2.resize(cam.transformFrame(cam.readFrame()), picture_dimensions, fx=0.2, fy=0.2))
    print(symbols[0:4])

if __name__ == "__main__":
    main()
    cam.release()
    cv2.destroyAllWindows()