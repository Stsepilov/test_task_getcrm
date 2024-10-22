import places


def solution():
    TIME: int = 48
    TIME_FOR_SLEEP: int = 16
    TIME_FOR_PLACES: int = TIME - TIME_FOR_SLEEP
    PLACES = places.places
    names = [i['name'] for i in PLACES]
    time = [i['time_spent'] for i in PLACES]
    importance = [i['importance'] for i in PLACES]
    n = len(time)
    place_list = []
    for i in range(n):
        place_info = {
            'vpw': abs(importance[i] - 21) / time[i],
            'weight': time[i],
            'name': names[i]
        }
        if len(place_list) == 0:
            place_list.append(place_info)
        else:
            k = 0
            while k < len(place_list) and place_list[k]['vpw'] > place_info['vpw']:
                k += 1
            place_list.insert(k, place_info)
    total_importance = 0
    time_left = TIME_FOR_PLACES
    visited_places = []
    for place in place_list:
        if time_left - place['weight'] >= 0:
            total_importance += place['vpw'] * place['weight']
            visited_places.append(place['name'])
            time_left -= place['weight']
    print(total_importance)
    print(time_left)
    print(*visited_places, sep=" -> ")


if __name__ == '__main__':
    solution()
