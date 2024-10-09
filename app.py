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
        self.temp_label = QLabel("70°F", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

api_key = 'aacbd94389d8202d7d751038787ac835'

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']  # Test commit by omar
temp = round(weather_data.json()['main']['temp'])

print(weather, temp)
