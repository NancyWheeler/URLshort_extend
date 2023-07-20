import pyshorteners as ps
from dotenv.main import load_dotenv
import os


load_dotenv()

s = ps.Shortener(api_key=os.getenv('BITLY_KEY'))

url = input("Enter the URL to shorten/extend: ")
choice = input("\nShorten(y)/Extend(n) URL? ")

if choice.lower() == 'y':
    short_url = s.bitly.short(url)
    print("\nThe shortened URL is: " + short_url)
else:
    long_url = s.bitly.expand(url)
    total_clicks = s.bitly.total_clicks(url)
    print("\n%s ==> %s and has been clicked on %d times." % (url, long_url, total_clicks))
