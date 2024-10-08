import sys  #test commit
import requests #pip install requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout) #pip install PyQt5

from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.user_input = QLabel("enter city: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_btn = QPushButton("Continue", self)
        self.temp_label = QLabel("70°F", self)
        self.emoji_label = QLabel("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

api_key = 'aacbd94389d8202d7d751038787ac835'


weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']             #Test commit by omar
temp = round(weather_data.json()['main']['temp'])

print(weather, temp)