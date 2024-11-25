from requests.auth import HTTPBasicAuth
from datetime import datetime
import json
import requests
import base64
from decouple import config
class MpesaCredentials:
    consumer_key = config('MPESA_CONSUMER_KEY')
    consumer_secret = config('MPESA_CONSUMER_SECRET')
    api_url = config('MPESA_API_URL')


class MpesaAccessToken:
    r = requests.get(MpesaCredentials.api_url, auth=HTTPBasicAuth(MpesaCredentials.consumer_key, MpesaCredentials.consumer_secret))
    
    mpesa_access_token = json.loads(r.text)
    validate_access_token = mpesa_access_token['access_token']


class MpesaPassword:
    time = datetime.now().strftime('%Y%m%d%H%m%S')
    business_short_code = config('MPESA_BUSINESS_CODE')
    offsetValue = config('MPESA_OFFSET_VALUE') # 0 
    passkey = config('MPESA_PASS_KEY') # get passkey 
    encode_data = business_short_code + passkey + time
    generated_ppassword = base64.b64encode.encode(encode_data.encode())
    decode_generated_password = generated_ppassword.decode('utf-8')
    