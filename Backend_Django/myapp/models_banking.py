from django.db import models



# 20231119 김용록 데이터베이스 선언
class BankUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BankAccount(models.Model):
    user = models.ForeignKey('BankUser', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BankTransaction(models.Model):
    from_account = models.ForeignKey('BankAccount', related_name='transactions_from', on_delete=models.CASCADE)
    to_account = models.ForeignKey('BankAccount', related_name='transactions_to', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


