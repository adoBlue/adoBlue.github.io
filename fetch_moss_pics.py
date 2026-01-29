import requests

# LoremFlickr is a great alternative for keyword-based random images
moss_url = "https://loremflickr.com/1080/720/moss"

def download_moss():
    try:
        response = requests.get(moss_url, timeout=10)
        # Check if the request was successful (Status 200)
        if response.status_code == 200:
            with open("today_moss.jpeg", "wb") as f:
                f.write(response.content)
            print("Success! Your moss image has been saved.")
        else:
            print(f"Error: Server returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_moss()