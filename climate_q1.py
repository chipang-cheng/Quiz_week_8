import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()
years = []
co2 = []
temp = []

cursor.execute("SELECT year, co2, temperature FROM ClimateData")
data = cursor.fetchall()

for row in data:
    year, tco2, temperature = row
    years.append(year)
    co2.append(tco2)
    temp.append(temperature)

conn.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
