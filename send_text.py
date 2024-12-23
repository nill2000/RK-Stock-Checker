import urllib.parse
from dotenv import load_dotenv
import http.client, urllib
import os

load_dotenv()
conn = http.client.HTTPSConnection("api.pushover.net:443")

poTOKEN = os.getenv("po_api_token")
poUSER = os.getenv("po_user_key")
subject = "Email Testing"
message = "Hello"

try:
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": poTOKEN,
        "user": poUSER,
        "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    response = conn.getresponse()

    if response.status == 200:
        print("Response Successful")
    else:
        print("Error occurred")
        
except Exception as e:
    print(e)
    
finally:
    conn.close()

