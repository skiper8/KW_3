import requests


def load_operations():
    """Забирает список операций банка в формате json"""

    response = requests.get(
        'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230208T094403Z&X-Amz-Expires=86400&X-Amz-Signature=60524437dae9a824b95587edaaefa6def6579b4348c3d05e6872eecdaca2df93&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject')
    client_operations = response.json()
    for item in client_operations:
        if item['state'] in 'EXECUTED':
            print(item)

load_operations()