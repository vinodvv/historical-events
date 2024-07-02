# Historical Events by date with Python
This Python script fetches historical events for a specific date using the 'history.muffinlabs.com' API.

# Functionality
* Prompts the user to enter a month (1-12) and day (1-31).
* Validates the user input.
* Retrieves historical events for the entered date from the API.
* Displays the year, description, and link to more information for each event.
* Informs the user if no events are found for the entered date.
# Usage
* Save the script as a Python file (e.g., historical_events.py).
* Run the script from your terminal using python historical_events.py.
* Follow the prompts to enter the month and day.
# Dependencies
This script requires the requests library. You can install it using pip:

# Bash
* pip install requests

# Example
Here's an example of the script output:

* Enter the month (e.g., 7 for July): 7
* Enter the day (e.g., 1 for 1st): 4

## Output
Historical Events on 7/4:
###
* Year: 1776
* Description: The United States Declaration of Independence is adopted by the Second Continental Congress.
* Link: https://en.wikipedia.org/wiki/United_States_Declaration_of_Independence
### 
* Year: 1826
* Description: Thomas Jefferson and John Adams, respectively the second and third presidents of the United States, die on the 50th anniversary of the Declaration of Independence.
* Link: https://en.wikipedia.org/wiki/Thomas_Jefferson

# License
This script is provided for educational purposes and does not have a specific license. However, feel free to use and modify it as needed.