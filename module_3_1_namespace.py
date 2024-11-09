calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    string_param = (len(string), string.upper(), string.lower())
    count_calls()
    return string_param

def is_contains(string, list_to_search):
    list_to_search_upp = []
    for i in list_to_search:
        list_to_search_upp.append(i.upper())

    is_it_here = list_to_search_upp.count(string.upper())
    if is_it_here > 0:
        count_calls()
        return True
    else:
        count_calls()
        return False
    # for i in list_to_search:
    #     if i == string:
    #         return True
    #     else:
    #         return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)