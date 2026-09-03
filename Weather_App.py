class Weather:
    def __init__(self, city, temperature, humidity, condition):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.condition = condition

    def display(self):
        print("\n-----------------------------")
        print("      WEATHER REPORT")
        print("-----------------------------")
        print("City        :", self.city)
        print("Temperature :", self.temperature, "°C")
        print("Humidity    :", self.humidity, "%")
        print("Condition   :", self.condition)
        print("-----------------------------")


class WeatherService:
    def __init__(self):
        self.weather_list = []

    def add_weather(self):
        city = input("Enter City Name: ")
        temperature = float(input("Enter Temperature (°C): "))
        humidity = int(input("Enter Humidity (%): "))
        condition = input("Enter Weather Condition: ")

        weather = Weather(city, temperature, humidity, condition)
        self.weather_list.append(weather)

        print("Weather data added successfully!")

    def view_weather(self):
        if len(self.weather_list) == 0:
            print("No weather records found.")
        else:
            for weather in self.weather_list:
                weather.display()

    def search_city(self):
        city_name = input("Enter city name to search: ")

        found = False

        for weather in self.weather_list:
            if weather.city.lower() == city_name.lower():
                weather.display()
                found = True
                break

        if not found:
            print("City not found!")

    def delete_city(self):
        city_name = input("Enter city name to delete: ")

        for weather in self.weather_list:
            if weather.city.lower() == city_name.lower():
                self.weather_list.remove(weather)
                print("Record deleted successfully!")
                return

        print("City not found!")


def main():

    service = WeatherService()

    while True:

        print("\n=================================")
        print("      WEATHER APPLICATION")
        print("=================================")
        print("1. Add Weather Data")
        print("2. View All Weather Data")
        print("3. Search City Weather")
        print("4. Delete City Weather")
        print("5. Exit")
        print("=================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            service.add_weather()

        elif choice == 2:
            service.view_weather()

        elif choice == 3:
            service.search_city()

        elif choice == 4:
            service.delete_city()

        elif choice == 5:
            print("Thank you for using Weather Application.")
            break

        else:
            print("Invalid choice! Try again.")


main()
