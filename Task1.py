temperatures = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5, 
                16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3, 
                13.4, 8.1, 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7, 
                7.8, 17.5, 13.6, 8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3, 
                16.4, 12.7, 8.9, 18.2, 13.1, 7.8, 16.6, 12.5]
cold = []
mild = []
comfortable = []
for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp <= 20:
        comfortable.append(temp)
print("Cold temperatures (<10°C):", cold)
print("Mild temperatures (10°C - 15°C):", mild)
print("Comfortable temperatures (15°C - 20°C):", comfortable)
print("\n")
#Task 2
mild_count = len(mild)
print("Number of times it was mild:", mild_count)
comfortable_count = len(comfortable)
print("Number of times it was comfortable:", comfortable_count)
cold_count = len(cold)
print("Number of times it was cold:", cold_count)
print("\n")
#Task3
# Task 3: Convert Celsius to Fahrenheit
temperatures_fahrenheit = [(temp * 9 / 5) + 32 for temp in temperatures]
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
print("\n")
#Task4
night_temps = []
evening_temps = []
day_temps = []
for i in range(len(temperatures)):
    if i % 3 == 0:  
        night_temps.append(temperatures[i])
    elif i % 3 == 1:  
        evening_temps.append(temperatures[i])
    else:  
        day_temps.append(temperatures[i])
avg_night_temp = sum(night_temps) / len(night_temps)
avg_evening_temp = sum(evening_temps) / len(evening_temps)
avg_day_temp = sum(day_temps) / len(day_temps)

print(f"Average Night Temperature: {avg_night_temp:.2f}°C")
print(f"Average Evening Temperature: {avg_evening_temp:.2f}°C")
print(f"Average Day Temperature: {avg_day_temp:.2f}°C")

print("\n") 
