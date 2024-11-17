import sys  # test commit
import requests  # pip install requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.QtCore import Qt


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()
        self.user_city = QLabel("enter city: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_btn = QPushButton("Continue", self)
        self.temp_label = QLabel (self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.user_city)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_btn)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.user_city.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.user_city.setObjectName("user_city")
        self.city_input.setObjectName("city_input")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.get_weather_btn.setObjectName("get_weather_btn")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#user_city{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_btn{
               font-size: 30px;
               font-weight: bold; 
            }
            QLabel#temp_label{
                font-size: 60px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        
        """)

        self.get_weather_btn.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = 'aacbd94389d8202d7d751038787ac835'
        city = self.city_input.text()

        try:
            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
            weather_data.raise_for_status()
            weather = weather_data.json()  # Test commit by omar

            if weather["cod"] == 200:
                self.display_weather(weather)

        except requests.exceptions.HTTPError as http_error:
            match  weather_data.status_code:
                case 400:
                    print("Bad request\nPlease check your input")
                case 401:
                    print("Unauthorized\nInvalid API key")
                case 403:
                    print("Forbidden\nAccess denied")
                case 404:
                    print("Not Found\nInvalid city, try again")
                case 500:
                    print("Internal Server Error\nPlease try again later")
                case 502:
                    print("Bad Gateway\nInvalid response from the server")
                case 503:
                    print("Service Unavailable\nServer is down")
                case 504:
                    print("Gateway Timeout\nNo response from the server")
                case _:
                    print(f"HTTP error occurred\n{http_error}")

        except requests.exceptions.RequestException:
            pass


    def display_error(self, message):
        pass

    def display_weather(self, data):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())


