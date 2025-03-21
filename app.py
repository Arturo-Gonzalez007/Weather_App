import sys  # test commit
import requests  # pip install requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
#pip install PyQt5
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()
        self.user_city = QLabel("enter city: ", self)
        self.city_input = QLineEdit(self)
        self.user_unit = QLabel("enter unit: 'F'/'C' ", self)
        self.unit_input = QLineEdit(self)
        self.get_weather_btn = QPushButton("Confirm", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.temp_highLow = QLabel(self)
        self.wind_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 500)  # Adjusted window size

        vbox = QVBoxLayout()
        vbox.setSpacing(15)  # Add spacing between elements

        vbox.addWidget(self.user_city)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.user_unit)
        vbox.addWidget(self.unit_input)
        vbox.addWidget(self.get_weather_btn)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.temp_highLow)
        vbox.addWidget(self.wind_label)  # Add wind label


        self.setLayout(vbox)

        # Center alignment
        self.user_city.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.user_unit.setAlignment(Qt.AlignCenter)
        self.unit_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.temp_highLow.setAlignment(Qt.AlignCenter)
        self.wind_label.setAlignment(Qt.AlignCenter)

        # Object Names for Styling
        self.setObjectName("main_window")
        self.user_city.setObjectName("user_city")
        self.city_input.setObjectName("city_input")
        self.user_unit.setObjectName("user_unit")
        self.unit_input.setObjectName("unit_input")
        self.temp_label.setObjectName("temp_label")
        self.temp_highLow.setObjectName("temp_highLow")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.get_weather_btn.setObjectName("get_weather_btn")
        self.wind_label.setObjectName("wind_label")


        # Apply CSS Stylesheet
        self.setStyleSheet("""
            QWidget#main_window {
                background-color: #F0F8FF;
            }
            QLabel, QPushButton {
                font-family: Calibri, Arial;
            }
            QLabel#user_city, QLabel#user_unit {
                font-size: 22px;
                font-style: italic;
            }
            QLineEdit {
                font-size: 18px;
                padding: 8px;
                border: 2px solid #ccc;
                border-radius: 8px;
            }
            QPushButton#get_weather_btn {
                font-size: 20px;
                font-weight: bold;
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton#get_weather_btn:hover {
                background-color: #45a049;
            }
            QLabel#temp_label {
                font-size: 40px;
                font-weight: bold;
            }
            QLabel#temp_highLow {
                font-size: 20px;
            }
            QLabel#emoji_label {
                font-size: 60px;
                font-family: 'Segoe UI Emoji';
            }
            QLabel#description_label {
                font-size: 24px;
            }
        """)

        self.get_weather_btn.clicked.connect(self.get_weather)

        self.get_weather_btn.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = 'aacbd94389d8202d7d751038787ac835'
        city = self.city_input.text()




        try:
            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
            weather_data.raise_for_status()
            weather = weather_data.json() # Test commit by omar\
            print(weather)

            if weather["cod"] == 200:
                self.display_weather(weather)

        except requests.exceptions.HTTPError as http_error:
            match  weather_data.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess denied")
                case 404:
                    self.display_error("Not Found:\nInvalid city, try again")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 30px")
        self.temp_label.setText(message)
        self.emoji_label.setText(" ")
        self.description_label.setText(" ")
        self.temp_highLow.setText(" ")

    def display_weather(self, weather):
        self.temp_label.setStyleSheet("font-size: 60px")

        unit = self.unit_input.text()
        weather_temp = weather["main"]["temp"]
        weather_high = weather["main"]["temp_max"]
        weather_low = weather["main"]["temp_min"]
        weather_id = weather["weather"][0]["id"]
        weather_description = weather["weather"][0]["description"]
        wind_speed = weather["wind"]["speed"]

        if unit == "F":
            self.temp_label.setText(f"{weather_temp:.0f}°F")
            self.temp_highLow.setText(f"H:{weather_high:.0f}° L:{weather_low:.0f}°")
            self.wind_label.setText(f"🌬 Wind: {wind_speed:.1f} mph")
        elif unit == "C":
            self.temp_label.setText(f"{((weather_temp - 32) * 5 / 9):.0f}°C")
            self.temp_highLow.setText(f"H:{((weather_high - 32) * 5 / 9):.0f}° L:{((weather_low - 32) * 5 / 9):.0f}°")
            self.wind_label.setText(f"🌬 Wind: {(wind_speed * 1.609):.1f} km/h")
        else:
            self.display_error("Invalid unit:\nPlease try again")

        self.emoji_label.setText(self.get_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return"🌪️"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""




if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())


