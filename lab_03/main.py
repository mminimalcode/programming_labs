import sys

from variant9_mod import (
    find_hotspots,
    get_rack_averages,
    get_unique_warnings
)

def main():
    if len(sys.argv) > 1:
     max_temp = float(sys.argv[1])
    else:
     max_temp = 35.0
    racks = {
        'Rack-1': [28.5, 29.0, 30.1],
        'Rack-2': [36.2, 38.0, 35.5],
        'Rack-3': [25.0, 26.1, 25.5]
    }

    averages = get_rack_averages(racks)
    hotspots = find_hotspots(racks, max_temp)

    warning_events = list(hotspots.keys()) + list(hotspots.keys())
    unique_warnings = get_unique_warnings(warning_events)

    print("=== МОНИТОРИНГ КЛИМАТА ЦОД ===")
    print(f"Предельная температура: {max_temp}°C")
    print(f"Средние температуры стоек: {averages}")
    print(f"Перегретые стойки (>{max_temp}°C): {hotspots}")
    print(f"Уникальные аварийные стойки (set): {unique_warnings}")

if __name__ == '__main__':
    main()