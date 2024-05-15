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
from barcode_decoder import decode_barcode  # decode_barcode 함수를 별도의 모듈로 관리하는 것을 가정

from django.core.files.storage import FileSystemStorage

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

        return JsonResponse(barcode_data, safe=False)
    return JsonResponse({'error': 'No file uploaded'}, status=400)