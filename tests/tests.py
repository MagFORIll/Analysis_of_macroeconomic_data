import csv
import pytest
import main

@pytest.fixture(autouse=True)
def clear_storage():
    main.STORAGE.clear()

def test_get_data_from_csv_success(tmp_path):
    file_path = tmp_path / "test.csv"
    file_path.write_text("country,gdp\nUSA,100\nUSA,200\n")

    data = list(main.get_data_from_csv(str(file_path)))

    assert len(data) == 2
    assert data[0]["country"] == "USA"
    assert data[0]["gdp"] == "100"

def test_get_data_from_csv_error():
    data = main.get_data_from_csv("not_existing.csv")

    assert isinstance(data, list)
    assert data[0]["status"] == "Error"
    assert "No such file" in str(data[0]["message"])

def test_calculating_average_gdp_single_country():
    data = [
        {"country": "USA", "gdp": "100"},
        {"country": "USA", "gdp": "300"},
    ]

    result = main.calculating_average_gdp(data)

    assert result["USA"][0] == 400
    assert result["USA"][1] == 2

def test_calculating_average_gdp_multiple_countries():
    data = [
        {"country": "USA", "gdp": "100"},
        {"country": "USA", "gdp": "300"},
        {"country": "FR", "gdp": "200"},
    ]

    result = main.calculating_average_gdp(data)

    assert result["USA"] == [400, 2]
    assert result["FR"] == [200, 1]

def test_upload_data_to_csv(tmp_path):
    output_file = tmp_path / "out.csv"
    data = [("USA", 200.0), ("FR", 150.0)]

    main.upload_data_to_csv(str(output_file), data)

    with open(output_file, newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows[0] == ["country", "gpd"]
    assert rows[1] == ["USA", "200.0"]
    assert rows[2] == ["FR", "150.0"]