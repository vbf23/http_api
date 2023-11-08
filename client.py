import requests

def get_website_headers(website_url):
    api_url = "http://your_server_ip/api/get_website_headers"  # Replace with your server's IP or domain name

    # Data to be sent in the request
    data_to_send = {"website_url": website_url}

    # Make a POST request to the API endpoint
    response = requests.post(api_url, json=data_to_send)

    # Check the response from the server
    if response.status_code == 200:
        # The request was successful, return the headers
        return response.json()
    else:
        # There was an error, return None or handle the error
        print(f"Error: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    # Example usage
    website_url = "https://example.com"
    headers = get_website_headers(website_url)
    
    if headers:
        print("Website Headers:", headers)
    else:
        print("Failed to retrieve website headers.")
