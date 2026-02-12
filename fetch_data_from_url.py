import requests
url="https://www.divyabhaskar.co.in/rashifal/15/today/"

try:
    response=requests.get(url,timeout=10)
    if response.status_code==200:
        print(response.text)
        print("Successfully fetched data from url")
    else:
        print("Failed to fetch data from url")
    
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")