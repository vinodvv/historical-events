import requests


def get_historical_events():
    month = input("Enter the moth (e.g., 7 for July): ")
    day = input("Enter the day (e.g., 1 for 1st): ")
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    events = data.get('data', {}).get('Events', [])
    print(f"Historical Events on {month}/{day}:\n")

    for event in events:
        year = event['year']
        text = event['text']
        links = event.get('links', [])
        first_link = links[0]['link']

        print(f"Year: {year}\nDescription: {text}\nLink: {first_link}\n")


if __name__ == "__main__":
    get_historical_events()
