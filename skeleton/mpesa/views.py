import requests
import json
from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
# from .models import Transaction
from .credentials import MpesaAccessToken, LipanaMpesaPpassword

def lipa_na_mpesa_online(request):
    if request.method == 'POST':
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}

        request_data = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": request.POST.get('amount'),
            "PartyA": request.POST.get('phone_number'),
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": request.POST.get('phone_number'),
            "CallBackURL": "https://yourcallbackurl.com/callback",
            "AccountReference": "YourAccountReference",
            "TransactionDesc": "Payment for goods"
        }

        response = requests.post(api_url, json=request_data, headers=headers)
        response_data = response.json()

        # Store transaction details in the database
        if response_data['ResponseCode'] == '0':
            # Transaction.objects.create(
            #     merchant_request_id=response_data['MerchantRequestID'],
            #     checkout_request_id=response_data['CheckoutRequestID'],
            #     response_code=response_data['ResponseCode'],
            #     response_description=response_data['ResponseDescription'],
            #     amount=request_data['Amount'],
            #     phone_number=request_data['PhoneNumber']
            # )
            return JsonResponse({'message': 'STK Push initiated successfully', 'data': response_data})
        else:
            return JsonResponse({'message': 'STK Push failed', 'data': response_data}, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=405)