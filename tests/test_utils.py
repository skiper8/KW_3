from utils.func import *

list_operations = load_operations()
sort_operations = sort_list(list_operations)


def test_sort_list():
    assert sort_list(sort_operations) == [{'date': '2019-12-07T06:17:14.634890',
                                           'description': 'Перевод организации',
                                           'from': 'Visa Classic 2842878893689012',
                                           'id': 114832369,
                                           'operationAmount': {'amount': '48150.39',
                                                               'currency': {'code': 'USD', 'name': 'USD'}},
                                           'state': 'EXECUTED',
                                           'to': 'Счет 35158586384610753655'},
                                          {'date': '2019-11-19T09:22:25.899614',
                                           'description': 'Перевод организации',
                                           'from': 'Maestro 7810846596785568',
                                           'id': 154927927,
                                           'operationAmount': {'amount': '30153.72',
                                                               'currency': {'code': 'RUB', 'name': 'руб.'}},
                                           'state': 'EXECUTED',
                                           'to': 'Счет 43241152692663622869'},
                                          {'date': '2019-11-13T17:38:04.800051',
                                           'description': 'Перевод со счета на счет',
                                           'from': 'Счет 38611439522855669794',
                                           'id': 482520625,
                                           'operationAmount': {'amount': '62814.53',
                                                               'currency': {'code': 'RUB', 'name': 'руб.'}},
                                           'state': 'EXECUTED',
                                           'to': 'Счет 46765464282437878125'},
                                          {'date': '2019-10-30T01:49:52.939296',
                                           'description': 'Перевод с карты на счет',
                                           'from': 'Visa Gold 7756673469642839',
                                           'id': 509645757,
                                           'operationAmount': {'amount': '23036.03',
                                                               'currency': {'code': 'RUB', 'name': 'руб.'}},
                                           'state': 'EXECUTED',
                                           'to': 'Счет 48943806953649539453'},
                                          {'date': '2019-09-29T14:25:28.588059',
                                           'description': 'Перевод со счета на счет',
                                           'from': 'Счет 35421428450077339637',
                                           'id': 888407131,
                                           'operationAmount': {'amount': '45849.53',
                                                               'currency': {'code': 'USD', 'name': 'USD'}},
                                           'state': 'EXECUTED',
                                           'to': 'Счет 46723050671868944961'}]


def test_date_format():
    assert date_format(sort_operations) == [{'date': '07.12.2019',
                                             'description': 'Перевод организации',
                                             'from': 'Visa Classic 2842878893689012',
                                             'id': 114832369,
                                             'operationAmount': {'amount': '48150.39',
                                                                 'currency': {'code': 'USD', 'name': 'USD'}},
                                             'state': 'EXECUTED',
                                             'to': 'Счет 35158586384610753655'},
                                            {'date': '19.11.2019',
                                             'description': 'Перевод организации',
                                             'from': 'Maestro 7810846596785568',
                                             'id': 154927927,
                                             'operationAmount': {'amount': '30153.72',
                                                                 'currency': {'code': 'RUB', 'name': 'руб.'}},
                                             'state': 'EXECUTED',
                                             'to': 'Счет 43241152692663622869'},
                                            {'date': '13.11.2019',
                                             'description': 'Перевод со счета на счет',
                                             'from': 'Счет 38611439522855669794',
                                             'id': 482520625,
                                             'operationAmount': {'amount': '62814.53',
                                                                 'currency': {'code': 'RUB', 'name': 'руб.'}},
                                             'state': 'EXECUTED',
                                             'to': 'Счет 46765464282437878125'},
                                            {'date': '30.10.2019',
                                             'description': 'Перевод с карты на счет',
                                             'from': 'Visa Gold 7756673469642839',
                                             'id': 509645757,
                                             'operationAmount': {'amount': '23036.03',
                                                                 'currency': {'code': 'RUB', 'name': 'руб.'}},
                                             'state': 'EXECUTED',
                                             'to': 'Счет 48943806953649539453'},
                                            {'date': '29.09.2019',
                                             'description': 'Перевод со счета на счет',
                                             'from': 'Счет 35421428450077339637',
                                             'id': 888407131,
                                             'operationAmount': {'amount': '45849.53',
                                                                 'currency': {'code': 'USD', 'name': 'USD'}},
                                             'state': 'EXECUTED',
                                             'to': 'Счет 46723050671868944961'}]


def test_check_formate():
    assert check_format(sort_operations) == [{'date': '07.12.2019',
                                              'description': 'Перевод организации',
                                              'from': 'Visa Classic 2842 **** **** 9012',
                                              'id': 114832369,
                                              'operationAmount': {'amount': '48150.39',
                                                                  'currency': {'code': 'USD', 'name': 'USD'}},
                                              'state': 'EXECUTED',
                                              'to': 'Счет **3655'},
                                             {'date': '19.11.2019',
                                              'description': 'Перевод организации',
                                              'from': 'Maestro 7810 **** **** 5568',
                                              'id': 154927927,
                                              'operationAmount': {'amount': '30153.72',
                                                                  'currency': {'code': 'RUB', 'name': 'руб.'}},
                                              'state': 'EXECUTED',
                                              'to': 'Счет **2869'},
                                             {'date': '13.11.2019',
                                              'description': 'Перевод со счета на счет',
                                              'from': 'Счет 3861************9794',
                                              'id': 482520625,
                                              'operationAmount': {'amount': '62814.53',
                                                                  'currency': {'code': 'RUB', 'name': 'руб.'}},
                                              'state': 'EXECUTED',
                                              'to': 'Счет **8125'},
                                             {'date': '30.10.2019',
                                              'description': 'Перевод с карты на счет',
                                              'from': 'Visa Gold 7756 **** **** 2839',
                                              'id': 509645757,
                                              'operationAmount': {'amount': '23036.03',
                                                                  'currency': {'code': 'RUB', 'name': 'руб.'}},
                                              'state': 'EXECUTED',
                                              'to': 'Счет **9453'},
                                             {'date': '29.09.2019',
                                              'description': 'Перевод со счета на счет',
                                              'from': 'Счет 3542************9637',
                                              'id': 888407131,
                                              'operationAmount': {'amount': '45849.53',
                                                                  'currency': {'code': 'USD', 'name': 'USD'}},
                                              'state': 'EXECUTED',
                                              'to': 'Счет **4961'}]