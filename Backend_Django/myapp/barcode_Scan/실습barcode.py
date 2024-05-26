import cv2
import pyzbar.pyzbar as pyzbar


cap = cv2.VideoCapture(0)



while True:
    success, frame = cap.read()

    if success :

        for code in pyzbar.decode(frame):
            my_code = code.data.decode('utf-8')
            print("인식 성공 : ", my_code)


        cv2.imshow('cam', frame)

        # 키 입력을 대기 (1ms 동안) -> ESC 키(ASCII 27) 누르면 break
        key = cv2.waitKey(1)
        if key == 27 :
            break

# break -> 카메라 헤제
cap.release()

# 모든 창 닫기
cv2.destroyAllWindows