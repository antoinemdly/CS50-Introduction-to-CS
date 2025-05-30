import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)

# date,state,fips,cases,deaths
# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):

    previous_cases = {}

    new_cases = {}

    next(reader)
    for row in reader:
        state = row['state']
        cases = int(row['cases'])

        if state not in new_cases:
            new_cases[state] = []

        #statetest = new_cases.get(state, state)
        #new_cases[state] = statetest


        if state in previous_cases:
            new_cases[state].append(cases - previous_cases[state])
        else:
            new_cases[state].append(cases)

        if len(new_cases[state]) > 14:
            new_cases[state].pop(0)

        previous_cases[state] = cases

    return new_cases

# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):

    for element in states:
        sum2 = sum(new_cases[element][0:8])
        average = round(sum2/7)

        sum_2 = sum(new_cases[element][8:15])
        average_2 = round(sum_2/7)

        pourcentage = round((average - average_2)/average_2)

        if pourcentage > 0:
            print(f"{element} had a 7-day average of {average} and a decrease of {abs(pourcentage)}%")
        else:
            print(f"{element} had a 7-day average of {average} and a increase of {abs(pourcentage)}%")

main()
