from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BankAccount

# view의 역활은 Spring에서 Controller와 같다.
# view에서 가져오거나 전달할 것 처리하고 url에서 매핑해준다. 이후에 html에서 템플릿 작성
# 그게 MVT 방법의 가장 큰 예시

# Create your views here.
def index(request):
    return render(request, 'index.html')


# 20231119 김용록 계좌 연결1 view -> urls -> templetes.banking.account_detail
def account_detail(request, account_id):
    # Assuming Account model has an 'id' field
    account = BankAccount.objects.get(id=account_id)
    return render(request, 'banking/account_detail.html', {'account': account})


# 202311201453 김용록 양식 설정 (forms -> views -> urls -> templtes)
from .forms import TransactionForm
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view')  # 'some_view'는 다른 뷰의 URL 패턴 이름으로 대체해야 함
    else:
        form = TransactionForm()
    
    return render(request, 'banking/create_transaction.html', {'form': form})


def hosptal_main(request):
    # if request.method == 'POST':
    #     form = TransactionForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('some_view')  # 'some_view'는 다른 뷰의 URL 패턴 이름으로 대체해야 함
    # else:
    #     form = TransactionForm()
    
    return render(request, 'hosptal/hosptal_main.html', {'form': form})