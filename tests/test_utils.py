import requests
from utils.func import *


# тест на сортировку списка операций
def test_sort_list(test_data):
    data = sort_list(test_data)

    assert data is not None
    assert type(data) is list
    assert data == [
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-26T15:40:13.413061",
            "operationAmount": {
                "amount": "50870.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 43597928997568165086"
        },
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-21T15:40:13.413061",
            "operationAmount": {
                "amount": "50870.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Счет 43597928997568165086",
            "to": "Счет 43597928997568165086"
        }
    ]


# тест на форматирование даты
def test_date_format(test_data):
    data = date_format(sort_list(test_data))

    assert data is not None
    assert type(data) is list
    assert type(data[0]) is dict
    assert data[0]["date"] == "26.01.2018"


# тест на формирование номеров карт и счетов
def test_check_formate(test_data):
    check = check_format(sort_list(test_data))
    assert check is not None
    assert type(check) is list
    assert type(check[0]) is dict
    assert check[0]['from'] == "Maestro 4598 **** **** 4501"
    assert check[1]['from'] == "Счет 4359************5086"
    assert check[0]['to'] == "Счет **5086"


# тест на загрузку листа операций
def test_load_operations():
    load_operations('https://www.jsonkeeper.com/b/J0N1')
