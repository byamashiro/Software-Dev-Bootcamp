import requests

api_url = "https://api.nasa.gov/DONKI/SEP?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=DEMO_KEY" # Example public API

try:
    response = requests.get(api_url)
    response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)

    data = response.json()
    print("Fetched Data:")
    # print(data)
    print(f"sepID: {data[0]['sepID']}")
    print(f"eventTime: {data[0]['eventTime']}")
    print(f"instruments: {data[0]['instruments']}")


except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")