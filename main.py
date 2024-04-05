def read_population_data(file_name):
    """
        Read population data from a file.

        Args:
            file_name (str): The name of the file to read data from.

        Returns:
            list: A list of tuples containing country name, area, and population.
    """
    population_data = []
    with open(file_name, 'r') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            population_data.append((country, float(area), int(population)))
    return population_data


def sort_by_area(population_data):
    """
        Sort population data by area.

        Args:
            population_data (list): A list of tuples containing country name, area, and population.

        Returns:
            list: Population data sorted by area.
    """
    return sorted(population_data, key=lambda x: x[1])


def sort_by_population(population_data):
    """
        Sort population data by population.

        Args:
            population_data (list): A list of tuples containing country name, area, and population.

        Returns:
            list: Population data sorted by population.
    """
    return sorted(population_data, key=lambda x: x[2])


def main():
    """
        Read population data from a file and print sorted data by area and population.
    """
    file_name = "text.txt"
    population_data = read_population_data(file_name)

    sorted_by_area = sort_by_area(population_data)
    print("Sorted by area:")
    for country_data in sorted_by_area:
        print(country_data)

    sorted_by_population = sort_by_population(population_data)
    print("\nSorted by population:")
    for country_data in sorted_by_population:
        print(country_data)


if __name__ == "__main__":
    main()
