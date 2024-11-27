import os
import base64
import requests
from requests.auth import HTTPBasicAuth
import datetime

class MpesaAccessToken:
    access_token = None
    token_expiry_time = None

    @staticmethod
    def get_access_token():
        consumer_key = os.getenv('MPESA_CONSUMER_KEY')  # Load from environment variable
        consumer_secret = os.getenv('MPESA_CONSUMER_SECRET')  # Load from environment variable
        api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

        try:
            response = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
            response.raise_for_status()  # Raise an error for bad responses
            json_response = response.json()
            MpesaAccessToken.access_token = json_response['access_token']
            MpesaAccessToken.token_expiry_time = datetime.datetime.now() + datetime.timedelta(minutes=59)  # Token is valid for 60 minutes
            return MpesaAccessToken.access_token
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving access token: {e}")
            return None

    @classmethod
    def validated_mpesa_access_token(cls):
        if cls.access_token is None or datetime.datetime.now() >= cls.token_expiry_time:
            return cls.get_access_token()
        return cls.access_token

class LipanaMpesaPpassword:
    Business_short_code = os.getenv('MPESA_BUSINESS_CODE')  # Load from environment variable
    Shortcode_password = os.getenv('MPESA_PASS_KEY')  # Load from environment variable
    
    @staticmethod
    def get_lipa_time():
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    @property
    def decode_password(self):
        lipa_time = self.get_lipa_time()
        password = f"{self.Business_short_code}{self.Shortcode_password}{lipa_time}"
        return base64.b64encode(password.encode()).decode()