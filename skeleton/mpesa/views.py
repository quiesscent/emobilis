from django.shortcuts import render
from decouple import config
from django.http import HttpResponse
from .forms import MpesaPaymentForm
from .credentials import MpesaAccessToken, MpesaCredentials, MpesaPassword
# Create your views here.

def pay(request):
    form = MpesaPaymentForm()
    
    return render(request, 'pay.html', {'form': form})


def stk(request):
    
    if request.method == 'POST':
        if form.is_valid():
            number = form.cleaned_data['number']
            amountt = form.cleaned_data['amount']
            access_token = MpesaAccessToken.mpesa_access_token
            api_url = config('MPESA_SANDBOX_URL')
            headers = {
                "Authorization": "Bearer  %s" % access_token
            }
            request = {    
                    "BusinessShortCode": "174379",    
                    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",    
                    "Timestamp":"20160216165627",    
                    "TransactionType": "CustomerPayBillOnline",    
                    "Amount": "1",    
                    "PartyA":"254708374149",    
                    "PartyB":"174379",    
                    "PhoneNumber":"254708374149",
                    "CallBackURL": "https://mydomain.com/pat",    
                    "AccountReference":"Test",    
                    "TransactionDesc":"Test"
                }
            response = request.post(api_url, json=request, headers=headers)
            return HttpResponse('Success')