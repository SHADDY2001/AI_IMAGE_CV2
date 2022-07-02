


from ast import Invert
import  cv2
image=cv2.imread("bat.png")
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

invert= cv2.bitwise_not(grey_img)

blur=cv2.GaussianBlur(invert,(21,21),0)

Invertedblur  = cv2.bitwise_not(blur)

zketch= cv2.divide(grey_img,Invertedblur,scale=256.0)

cv2.imwrite("zkeched.png",zketch)