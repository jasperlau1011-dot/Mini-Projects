import random
laps = 10
print("Available F1 Tracks:")
print("1- Albert Park Grand Prix Circuit")
print("2- Shanghai International Circuit")
print("3- Suzuka Circuit")
print("4- Jeddah Corniche Circuit")
print("5- Miami International Autodrome")
print("6- Circuit Gilles Villeneuve")
print("7- Circuit de Monaco")
print("8- Circuit de Barcelona-Catalunya")
print("9- Circuito de Madrid")
print("10- Red Bull Ring")
print("11- Silverstone Circuit")
print("12- Circuit de Spa-Francorchamps")
print("13- Hungaroring")
print("14- Circuit Zandvoort")
print("15- Autodromo Nazionale Monza")
print("16- Baku City Circuit")
print("17- Marina Bay Street Circuit")
print("18- Circuit of the Americas")
print("19- Autódromo Hermanos Rodríguez")
print("20- Autódromo José Carlos Pace")
print("21- Las Vegas Strip Street Circuit")
print("22- Losail International Circuit")
print("23- Yas Marina Circuit")
selected_track = input("\nEnter the name of the F1 track by number: ")
statistics_qualifying_pos = [
    "Lando Norris", "Oscar Piastri", "George Russell", "Kimi Antonelli", "Charles Leclerc",
    "Lewis Hamilton", "Max Verstappen", "Carlos Sainz", "Liam Lawson", "Arvid Lindblad", "Pierre Gasly",
    "Franco Colapinto", "Fernando Alonso", "Lance Stroll", "Gabriel Bortoleto", "Nico Hulkenberg",
    "Esteban Ocon", "Oliver Bearman", "Issac Hadjar", "Alex Albon", "Sergio Perez", "Valtteri Bottas"
]
original_drivers = statistics_qualifying_pos.copy()
original_overtaking_stat = [90, 85, 85, 80, 95, 95, 100, 85, 80, 75, 80, 80, 95, 75, 75, 80, 80, 80, 75, 85, 80, 70]
race_start_ot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
race_start_ot_prob = [1, 1, 1, 2, 2, 3, 4, 3, 5, 6, 6, 7, 9 ,11, 13, 17, 26, 38, 51, 83, 96, 103, 104, 98, 76, 68, 52, 39, 30, 20]
probability = [155, 45, 210, 285, 75, 80, 90, 5, 8, 4, 22, 3, 12, 2, 1, 1, 1, 3, 9, 2, 2, 1]
dist_pos_start = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
overtaking_stat = [90, 85, 85, 80, 95, 95, 100, 85, 80, 75, 80, 80, 95, 75, 75, 80, 80, 80, 75, 85, 80, 70]
defending_stat = [90, 85, 90, 70, 85, 95, 100, 90, 80, 70, 80, 75, 100, 70, 75, 85, 85, 75, 70, 80, 80, 80]
qualifying_results = []
numbers = ['0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5']
dist_prob = [121, 108, 122, 139, 119, 110, 124, 98, 90, 86, 97, 92, 107, 79, 87, 87, 85, 89, 98, 89, 76, 78]
if selected_track == "1":
    rain_prob = 121
    last_prob = random.randint(10, 20)
    probability[6] += 60
if selected_track == "2":
    rain_prob = 357
    last_prob = random.randint(60, 360)
    probability[6] += 70
    probability[2] += 20
    probability[7] += 33
    probability[13] += 34
if selected_track == "3":
    rain_prob = 212
    probability[7] += 64
    probability[4] += 86
    probability[2] += 70
    probability[6] += 50
    probability[5] += 54
if selected_track == "4":
    rain_prob = 0
    last_prob = 0
    probability[7] += 88
    probability[21] += 70
    probability[6] += 62
    probability[2] += 35
    probability[5] += 30
if selected_track == "5":
    rain_prob = 30
    last_prob = random.randint(10, 20)
    probability[4] += 88
    probability[7] += 75
    probability[1] += 60
    probability[5] += 55
    probability[2] += 30
if selected_track == "6":
    last_prob = random.randint(60, 360)
while statistics_qualifying_pos:
    result = random.choices(statistics_qualifying_pos, weights=probability, k=1)[0]
    qualifying_results.append(result)
    position = statistics_qualifying_pos.index(result)
    statistics_qualifying_pos.pop(position)
    probability.pop(position)
for i, driver in enumerate(qualifying_results, 1):
    print(f"P{i}: {driver}")
message = input("\nenter to continue:")
driver_def = result[0]
dice_roll_lap1 = random.choices(race_start_ot, weights=race_start_ot_prob, k=1)[0]
count_1 = dice_roll_lap1
drivers_lap1_ot = statistics_qualifying_pos
drivers_lap1_ot2 = statistics_qualifying_pos
count = 1
overtaking_drivers = []
print("Lap 1: Race Start")
while count_1 > 0:
    driver_ot = random.choices(original_drivers, weights=original_overtaking_stat, k=1)[0]
    overtaking_drivers.append(driver_ot)
    count_1 -= 1
for lap in range(1, laps + 1):
    if lap == 1:
        for driver_1 in overtaking_drivers:
            if driver_1 in qualifying_results:
                index_at = qualifying_results.index(driver_1)
                if index_at > 0:
                    index_def = index_at - 1
                    driver_def = qualifying_results[index_def]
                    qualifying_results[index_def] = driver_1
                    qualifying_results[index_at] = driver_def
                    print(f"-> {driver_1} overtook {driver_def}!")
    
        print("\n--- Order After Lap 1 ---")
        message = input("\nenter to continue")
        for i, driver in enumerate(qualifying_results, 1):
            print(f"P{i}: {driver}")
        count_1 = random.randint(0, 4)
        message = input("\nenter to continue (Next Lap)")
        overtaking_drivers = []
        for count_2 in range(1, count_1):
            driver_ot = random.choices(original_drivers, weights=original_overtaking_stat, k=1)[0]
            overtaking_drivers.append(driver_ot)
        for driver_123 in qualifying_results:
            if driver_123 == qualifying_results[0]:
                continue
            else:
                index_1 = qualifying_results.index(driver_123)
                index_2 = original_drivers.index(driver_123)
                drivers_12345 = [driver_123, qualifying_results[index_1 - 1]]
                chances = [dist_prob[index_1], dist_prob[index_1 - 1]]
                qualifying_dist = random.choices(drivers_12345, weights=chances, k=1)[0]
                if qualifying_dist == driver_123:
                    increase_dist = random.randrange(5, 51, 5) / 10
                    dist_pos_start[index_2] -= increase_dist
    else:
        for driver_12 in qualifying_results:
            if dist_pos_start[original_drivers.index(driver_12)] <= 2:
                index_12 = qualifying_results.index(driver_12)
                drivers_121 = [qualifying_results[index_12 - 1], driver_12]
                prob_12 = [defending_stat[original_drivers.index(qualifying_results[index_12 - 1])], overtaking_stat[original_drivers.index(driver_12)]]
                winning_ot = random.choices(drivers_121, weights=prob_12, k=1)[0]
                if winning_ot == driver_12:
                    qualifying_results[index_12 - 1] = driver_12
                    qualifying_results[index_12] = drivers_121[0]
                    print(f"-> {driver_12} overtook {qualifying_results[index_12]}!")
                for i, driver in enumerate(qualifying_results, 1):
                    print(f"P{i}: {driver}")
                    message = input("\nenter to continue (Next Lap)")

                    