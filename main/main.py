from utils.func import load_operations, date_format, check_format, sort_list

list_operations = load_operations("https://www.jsonkeeper.com/b/J0N1")

sort_operations = sort_list(list_operations)

date_format(sort_operations)

check_format(sort_operations)

for item in sort_operations:
    print(item['date'], item['description'])
    print(f"{item['from']} -> {item['to']}")
    print(item['operationAmount']['amount'], item['operationAmount']['currency']['name'])
    print('')
