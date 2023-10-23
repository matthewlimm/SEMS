import Adafruit_BMP.BMP085 as BMP085
import csv
import time

# Function to read BMP180 data
def read_bmp180_data():
    sensor = BMP085.BMP085()
    temperature = sensor.read_temperature()
    pressure = sensor.read_pressure()
    return temperature, pressure

# Function to calculate altitude
def calculate_altitude(pressure, sea_level_pressure=101325.0):
    altitude = 44330.0 * (1.0 - (pressure / sea_level_pressure) ** 0.1903)
    return altitude

# Function to write data to a CSV file
def write_to_csv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)

if __name__ == "__main__":
    # Define the CSV file name
    csv_filename = "bmp180_data.csv"
   
    # You can adjust this value to match your location
    sea_level_pressure = 101325.0
   
    try:
        while True:
            temperature, pressure = read_bmp180_data()
            altitude = calculate_altitude(pressure, sea_level_pressure)
           
            # Get the current timestamp
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
           
            # Create a list of data to write to the CSV file
            data_to_write = [timestamp, temperature, pressure, altitude]
           
            write_to_csv(csv_filename, data_to_write)
           
            print(f"Timestamp: {timestamp}, Temperature: {temperature} °C, Pressure: {pressure} Pa, Altitude: {altitude} meters")
           
            # Wait for a specified interval (e.g., 5 seconds)
            time.sleep(5)
   
    except KeyboardInterrupt:
        print("Data collection stopped.")