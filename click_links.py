import requests


# click links
def click_links(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print(f"Successfully clicked link: {link}")
        else:
            print("Failed to visit", link, "error code:", response.status_code)
    except Exception as e:
        print("Error with", link, str(e))
