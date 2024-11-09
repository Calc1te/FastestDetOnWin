import cv2
video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    video.release()
print("helloworld")