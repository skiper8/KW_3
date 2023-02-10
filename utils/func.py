import requests
from datetime import datetime
from operator import itemgetter


def load_operations():
    """Забирает список операций банка в формате json и отсеивает успешные"""

    response = requests.get(
        'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676135093848&signature=imvE79xXXeW-6wlUeUxzhVhRTMFfqkC1FRoMwcaA9DI&downloadName=operations.json')
    list_operations = response.json()
    return list_operations


def sort_list(list_operations):
    """Сортировка операций по дате и сохранение 5-и последних"""

    sort_operations = []
    for item in list_operations:
        if 'state' in item:
            if item['state'] in 'EXECUTED':
                if 'from' in item:
                    sort_operations.append(item)
    sort_operations = sorted(sort_operations, key=itemgetter('date'), reverse=True)
    return sort_operations[:5]


def date_format(sort_operations):
    """Перевод даты в нужный формат"""

    for date in sort_operations:
        date['date'] = datetime.strptime(date['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    return sort_operations


def check_format(sort_operations):
    """Перевод номера счета в нужный формат"""

    for check in sort_operations:
        check['to'] = check['to'][:4] + ' **' + check['to'][-4:]
        if 'Счет' in check['from']:
            check['from'] = check['from'][:-16] + '************' + check['from'][-4:]
        else:
            check['from'] = check['from'][:-12] + ' **** **** ' + check['from'][-4:]
    return sort_operations
