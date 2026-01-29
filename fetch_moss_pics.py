import requests

moss_url = "https://loremflickr.com/1080/720/moss"
count_file = "moss_count.txt"
def download_moss():
    try:
        response = requests.get(moss_url, timeout=10)
        # Check if the request was successful (Status 200)
        if response.status_code == 200:
            with open("today_moss.jpeg", "wb") as f:
                f.write(response.content)

            current_counter = 0

            if os.path.exists(count_file):
                with open(count_file, "r") as f:
                    try:
                        content = f.read().strip()
                        if content:
                            current_counter = int(content)
                    except ValueError:
                        current_counter = 0

            new_count = current_counter + 1

            with open(count_file, "w") as f:
                f.write(str(new_count))

            print("Success! Your moss image has been saved.")
        else:
            print(f"Error: Server returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_moss()