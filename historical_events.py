import requests


def get_historical_events():
    """
    Fetches and displays historical events for a specific date.

    Prompts the user to enter a month and a day, validates the input, and fetches historical events
    that occurred on that date from the 'history.muffinlabs.com' API. The function prints the events,
    including the year, description and link to more information.

    The user is prompted to re-enter the month or day if the input is invalid.

    Raises:
        Exception: If there is an issue with the API request or data processing.

    Example:
        Enter the month (e.g., 7 for July): 7
        Enter the day (e.g., 1 for 1st): 4

        Historical Events on 7/4:

        Year: 1776
        Description: The United States Declaration of Independence is adopted by the Second Continental Congress.
        Link: https://en.wikipedia.org/wiki/United_States_Declaration_of_Independence

        Year: 1826
        Description: Thomas Jefferson and John Adams, respectively the second and third presidents of the United States, die on the 50th anniversary of the Declaration of Independence.
        Link: https://en.wikipedia.org/wiki/Thomas_Jefferson
    """
    try:
        month = validate_input("Enter the moth (e.g., 7 for July): ", 1, 12)
        day = validate_input("Enter the day (e.g., 1 for 1st): ", 1, 31)

        url = f"http://history.muffinlabs.com/date/{month}/{day}"
        response = requests.get(url)
        data = response.json()
        events = data.get('data', {}).get('Events', [])
        print(f"Historical Events on {month}/{day}:\n")

        if not events:
            print("No events found for this date.")
            return

        for event in events:
            year = event['year']
            text = event['text']
            links = event.get('links', [])
            first_link = links[0]['link']

            print(f"Year: {year}\nDescription: {text}\nLink: {first_link}\n")

    except Exception as e:
        print(f"An error occurred: {e}")


def validate_input(prompt, min_value, max_value):
    """
    Prompts the user for input and validates it within the specified range.

      Args:
          prompt: String representing the prompt message.
          min_value: Integer representing the minimum allowed value.
          max_value: Integer representing the maximum allowed value.

      Returns:
          Integer representing the validated user input.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Invalid input. Please enter a number between {min_value} and {max_value}")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    get_historical_events()
