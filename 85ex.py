import requests

def check_website_access(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        # Check the status code
        if response.status_code == 200:
            print(f"The website {url} is accessible.")
        else:
            print(f"The website {url} returned status code {response.status_code}.")
    except requests.ConnectionError:
        print(f"Could not connect to {url}. The website might be down or unreachable.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# URL of the IEFP website
url = "https://www.iefp.pt/"
check_website_access(url)
