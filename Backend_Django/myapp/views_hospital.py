from .forms_hospital import ImageForm
from django.shortcuts import render,redirect
from django.http import HttpResponse


########################################################################################################################
# 202405101740 김용록 hosptal RSA 만들기
def hospital_main(request):
    
    if request.method == 'POST': # post로 날리는데
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view') 
    else:
        form = ImageForm() # post가 아닌 요청 처리(ex:get인듯)
    
    return render(request, 'hospital/hospital_main.html', {'form': form})



# 202405151955 김용록 바코드 오픈소스 테스트 
from django.http import JsonResponse
# from barcode_decoder import decode_barcode  # decode_barcode 함수를 별도의 모듈로 관리하는 것을 가정
from django.core.files.storage import FileSystemStorage

# request -> HTTP 요청 객체
def barcode_view(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        path_to_image = fs.path(filename)
        
        # 바코드 디코드 함수 호출
        barcode_data = decode_barcode(path_to_image)
        
        # 파일 삭제 (옵션)
        fs.delete(filename)

        # redo : 여기다가 바코드를 구현하면 되나?
        return JsonResponse(barcode_data, safe=False)
    return JsonResponse({'error': 'No file uploaded'}, status=400)


# 202405160319 김용록 웹캠 실행
from django.http import StreamingHttpResponse
import cv2

# 202405160322 김용록 바코드 분석 라이브러리
import pyzbar.pyzbar as pyzbar

# 202405160923 감용록 pyzbar가 환경변수 설정해도 연결이 안돼 명시적으로 연결
import os
os.environ['DYLD_LIBRARY_PATH'] = '/Users/kim-yongrok/Github_Blog/Learn-conversational-English-by-chatGPT/myenv/lib'

def gen(camera):
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        

        # 202405160325 김용록 바코드   
        for code in pyzbar.decode(frame):
            my_code = code.data.decode('utf-8')


            # 202405171612 김용록 바코드/QR 코드 위치에 사각형 그리기
            # (x, y, w, h) = code.rect
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print("인식 성공 : ", my_code)


            # 202405160328 김용록 인식된 데이터 화면에 표시
            cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('cam', frame)



        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    # Django의 HTTP 응답 클래스 중 하나. 서버가 클라이언트에 데이터를 스트리밍 방식으로 전송할 수 있게 해줌
    return StreamingHttpResponse(gen(cv2.VideoCapture(0)),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


# 202405160323 김용록 바코드 실시간 처리
def barcode_data(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        # 여기서 바코드 데이터를 처리할 수 있습니다.



        print("Received barcode data:", barcode)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})