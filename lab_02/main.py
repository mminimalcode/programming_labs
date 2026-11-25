def analyze_power_quality(u_list):
    dips = 0
    overvoltages = 0

    for u in u_list:
        if u < 207:
            dips = dips + 1
        elif u > 253:
            overvoltages += 1

    deviations = dips + overvoltages
    total = len(u_list)

    if total == 0:
        return False, dips, overvoltages

    compliance = deviations / total < 0.05

    return compliance, dips, overvoltages

u_list = [220, 225, 205, 230, 250, 260, 215, 218, 240, 200,
          222, 245, 255, 220, 235, 210, 250, 219, 225, 230]

result, dips, overvoltages = analyze_power_quality(u_list)

print("Результаты анализа качества электроэнергии:")
print(f"Количество замеров: {len(u_list)}")
print(f"Количество провалов напряжения: {dips}")
print(f"Количество перенапряжений: {overvoltages}")

if result:
    print("Качество электроэнергии соответствует ГОСТ.")
else:
    print("Качество электроэнергии не соответствует ГОСТ.")