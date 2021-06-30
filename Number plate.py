import cv2

Width = 650
Height = 650
Cascadefile = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
min = 200
color = (255,255,255)

cap = cv2.VideoCapture(0)
cap.set(3, Width)
cap.set(4, Height)
cap.set(10,150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates = Cascadefile.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area >min:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            cv2.putText(img,"plate is here",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("saved/"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(650,300),(255,255,255),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        k=cv2.waitKey(500)
        count +=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break