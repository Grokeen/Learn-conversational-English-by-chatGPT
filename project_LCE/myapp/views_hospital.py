from .forms_hospital import Transaction_HospitalForm
from django.shortcuts import render,redirect
from django.http import HttpResponse


########################################################################################################################
# 202405101740 김용록 hosptal RSA 만들기
def hospital_main(request):
    
    if request.method == 'POST': # post로 날리는데
        form = Transaction_HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view') 
    else:
        form = Transaction_HospitalForm() # post가 아닌 요청 처리(ex:get인듯)
    
    return render(request, 'hospital/hospital_main.html', {'form': form})




