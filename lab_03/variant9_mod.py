def find_hotspots(rack_dict, max_temp=35.0):
    hotspots = {}

    for rack_id, temperatures in rack_dict.items():
        for temp in temperatures:
            if temp > max_temp:
                hotspots[rack_id] = temperatures
                break

    return hotspots

def get_rack_averages(rack_dict):
    averages = {}

    for rack_id, temperatures in rack_dict.items():
        if temperatures:
            averages[rack_id] = round(sum(temperatures) / len(temperatures), 2)
        else:
            averages[rack_id] = 0.0

    return averages

def get_unique_warnings(warning_events):
    return set(warning_events)

if __name__ == '__main__':
    test_racks = {
        'Rack-1': [28.5, 29.0, 30.1],
        'Rack-2': [36.2, 38.0, 35.5],
        'Rack-3': [25.0, 26.1, 25.5]
    }

    print("Перегретые стойки:", find_hotspots(test_racks))
    print("Средние температуры:", get_rack_averages(test_racks))
    print("Уникальные предупреждения:",
          get_unique_warnings(['Rack-2', 'Rack-2', 'Rack-1']))