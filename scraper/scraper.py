import requests


def test_scraper():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data retrieved successfully!")
        print(response.json())
    else:
        print("Error:", response.status_code)



