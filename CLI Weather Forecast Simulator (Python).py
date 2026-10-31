import random

class WeatherSimulator:
    def __init__(self):
        self.conditions = ["Sunny ☀️", "Partly Cloudy ⛅", "Rainy 🌧️", "Thunderstorm ⛈️", "Windy 🌬️"]

    def get_forecast(self, city):
        temp_celsius = random.randint(10, 38)
        condition = random.choice(self.conditions)
        humidity = random.randint(30, 90)
        
        return {
            "city": city.title(),
            "temperature": temp_celsius,
            "condition": condition,
            "humidity": humidity
        }

if __name__ == "__main__":
    simulator = WeatherSimulator()
    print("=== City Weather Simulator ===")
    city_input = input("Enter city name: ")
    
    forecast = simulator.get_forecast(city_input)
    
    print(f"\n--- Weather Report for {forecast['city']} ---")
    print(f"Condition: {forecast['condition']}")
    print(f"Temperature: {forecast['temperature']}°C ({forecast['temperature'] * 9/5 + 32:.1f}°F)")
    print(f"Humidity: {forecast['humidity']}%")
