import csv
import matplotlib.pyplot as plt

# jupyter notebook !pip install matplotlib

def read_sensor_data(filename):
    timestamps = []
    temperatures = []
    humidities = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the header
        for row in reader:
            timestamps.append(row[0])
            temperatures.append(float(row[1]))
            humidities.append(float(row[2]))
    return timestamps, temperatures, humidities

def analyze_data(data_list):
    avg_data = sum(data_list) / len(data_list)
    max_data = max(data_list)
    min_data = min(data_list)
    return avg_data, max_data, min_data

def plot_data(timestamps, temperatures, humidities):
    avg_temp, max_temp, min_temp = analyze_data(temperatures)
    avg_hum, max_hum, min_hum = analyze_data(humidities)
    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    
    ax1.plot(timestamps, temperatures, 'b-', label="Temperature")
    ax2.plot(timestamps, humidities, 'g-', label="Humidity")
    
    ax1.set_xlabel("Timestamp")
    ax1.set_ylabel("Temperature (°C)", color="blue")
    ax2.set_ylabel("Humidity (%)", color="green")
    
    ax1.tick_params(axis="y", colors="blue")
    ax2.tick_params(axis="y", colors="green")

    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    
    plt.title("AM2303 Sensor Data Analysis")
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    filename = "sensor_data.csv"
    timestamps, temperatures, humidities = read_sensor_data(filename)
    plot_data(timestamps, temperatures, humidities)
