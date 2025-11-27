import requests

def test_api(name, url):
    print(f"Testing {name} at {url}...")
    try:
        response = requests.get(url, timeout=10)
        print(f"Status: {response.status_code}")
        if response.ok:
            try:
                data = response.json()
                print(f"Data keys: {list(data.keys()) if isinstance(data, dict) else 'List'}")
                print(f"Sample: {str(data)[:100]}")
            except:
                print("Not JSON")
        else:
            print(f"Error: {response.text[:100]}")
    except Exception as e:
        print(f"Exception: {e}")
    print("-" * 20)

test_api("DogeMeme", "https://api.doge-meme.lol/meme")
test_api("Catch The Show", "https://catchtheshow.herokuapp.com/api/shows")
