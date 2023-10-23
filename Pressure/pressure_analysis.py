import Adafruit_BMP.BMP085 as BMP085
import matplotlib.pyplot as plt
import csv



# Create a BMP180 sensor instance
sensor = BMP085.BMP085()

# Read temperature and pressure data
temperature = sensor.read_temperature()
pressure = sensor.read_pressure()

# Calculate altitude
# The following formula is a simple approximation and may not be accurate for all locations.
# You may need to adjust it according to your specific requirements.
altitude = sensor.read_altitude()

# Print the data
print(f"Temperature: {temperature} °C")
print(f"Pressure: {pressure} Pa")
print(f"Altitude: {altitude} meters")

# Perform your data analysis here, e.g., store data, plot it, etc.
# You can use libraries like matplotlib for data visualization and analysis.

# Example: Saving data to a CSV file

data = {'Temperature (°C)': temperature, 'Pressure (Pa)': pressure, 'Altitude (m)': altitude}
with open('bmp180_data.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)

# Example: Plotting data using matplotlib

# You'll need to collect and store data over time for meaningful plotting.
# Here's a simple example to get you started.
temperature_data = [temperature]
pressure_data = [pressure]
altitude_data = [altitude]

# Plot temperature over time
plt.plot(temperature_data, label='Temperature (°C)')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()

