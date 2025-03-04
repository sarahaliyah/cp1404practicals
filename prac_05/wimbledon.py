"""
Estimated time: 30 minutes
Actual time: 45 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read the data file and display the processed data of Wimbledon champions and countries."""
    data = load_data(FILENAME)
    champion_counts, countries = process_data(data)
    display_results(champion_counts, countries)


def display_results(champion_counts, countries):
    """Display the results of champion wins and countries."""
    print("Wimbledon Champions: ")
    for champion, count in champion_counts.items():
        print(f"{champion} {count}")
    sorted_countries = sorted(countries)
    countries_string = ", ".join(sorted_countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(countries_string)


def process_data(data):
    """Create a dictionary and get champions count and their countries."""
    champion_counts = {}
    countries = set()
    for row in data:
        countries.add(row[INDEX_COUNTRY])
        try:
            champion_counts[row[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_counts[row[INDEX_CHAMPION]] = 1
    return champion_counts, countries


def load_data(filename):
    """Load the data from the file in list of lists form."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline().strip().split(',')
        for line in in_file:
            row = line.strip().split(',')
            data.append(row)
    return data


main()
