import requests
import os

moss_url = "https://source.unsplash.com/featured/?moss"

def download_moss():
    response = requests.get(moss_url)
    if response.status_code == 200:
        with open("today_moss.jpeg", "wb") as f:
            f.write(response.content)
    else:
        print("Error")
if __name__ == "__main__":
    download_moss()
