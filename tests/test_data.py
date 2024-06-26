import pytest
from main import sort_by_area, sort_by_population
import os
from main import read_population_data, sort_by_area, sort_by_population


def test_read_population_data():
    """
       Test if the read_population_data function correctly reads data from a file.
    """
    file_name = "test_data.txt"
    with open(file_name, 'w') as file:
        file.write("Country1,100,1000\n")
        file.write("Country2,200,2000\n")
    population_data = read_population_data(file_name)
    assert population_data == [('Country1', 100.0, 1000), ('Country2', 200.0, 2000)]
    os.remove(file_name)


def test_sort_by_area():
    """
        Test sorting population data by area.
    """
    population_data = [('Country2', 200.0, 2000), ('Country1', 100.0, 1000)]
    sorted_data = sort_by_area(population_data)
    assert sorted_data == [('Country1', 100.0, 1000), ('Country2', 200.0, 2000)]


def test_sort_by_population():
    """
        Test sorting population data by population.
    """
    population_data = [('Country2', 200.0, 2000), ('Country1', 100.0, 1000)]
    sorted_data = sort_by_population(population_data)
    assert sorted_data == [('Country1', 100.0, 1000), ('Country2', 200.0, 2000)]


@pytest.fixture
def population_data():
    return [('Country2', 200.0, 2000), ('Country1', 100.0, 1000)]


def test_sort_by_area(population_data):
    """
    Test sorting population data by area using fixture.
    """
    sorted_data = sort_by_area(population_data)
    assert sorted_data == [('Country1', 100.0, 1000), ('Country2', 200.0, 2000)]


def test_sort_by_population(population_data):
    """
        Test sorting population data by population using fixture.
    """
    sorted_data = sort_by_population(population_data)
    assert sorted_data == [('Country1', 100.0, 1000), ('Country2', 200.0, 2000)]
