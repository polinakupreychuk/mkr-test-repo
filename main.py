def read_population_data(filename):
    population_data = []
    with open(filename, 'r') as file:
        for line in file:
            # Розділити рядок за комою і видалити зайві пробіли
            country, area, population = map(str.strip, line.split(','))
            # Додати дані про популяцію у список
            population_data.append((country, float(area), int(population)))
    return population_data

def sort_by_area(population_data):
    # Сортувати дані за площею
    sorted_by_area = sorted(population_data, key=lambda x: x[1], reverse=True)
    return sorted_by_area

def sort_by_population(population_data):
    # Сортувати дані за населенням
    sorted_by_population = sorted(population_data, key=lambda x: x[2], reverse=True)
    return sorted_by_population

def main():
    filename = input("Введіть назву файлу: ")
    try:
        # Зчитати дані про популяцію з файлу
        population_data = read_population_data(filename)
        # Відсортувати дані за площею
        sorted_by_area = sort_by_area(population_data)
        # Відсортувати дані за населенням
        sorted_by_population = sort_by_population(population_data)

        # Вивести результати
        print("Дані, відсортовані за площею:")
        for country, area, population in sorted_by_area:
            print(f"{country}: площа - {area}, населення - {population}")

        print("\nДані, відсортовані за населенням:")
        for country, area, population in sorted_by_population:
            print(f"{country}: площа - {area}, населення - {population}")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()
