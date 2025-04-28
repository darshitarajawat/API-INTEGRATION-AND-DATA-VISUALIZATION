import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = '0513ec03a648dd57a9b04c38d4fe82c1' 
CITY = 'New York'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    dates = []
    temperatures = []

    for item in data['list']:
        dates.append(item['dt_txt'])
        temperatures.append(item['main']['temp'])

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14,6))
    sns.lineplot(x=dates, y=temperatures, marker='o')
    plt.title(f"5-Day Temperature Forecast for {CITY}")
    plt.xlabel('Date-Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
