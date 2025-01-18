from . import current
from . import coordenates
from key import key
import requests

class Weather(coordenates.Coords):
	def __init__(self, city="Porto", country=None):
		super().__init__(city, country)

		url = "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&units=metric"
		url = url.format(lat=self.lat, lon=self.lon, key=key)
		self.r = requests.get(url).json()

		self.weather = self.r["list"]
		for i in self.weather:
			i.pop("dt")
			i.pop("sys")
			i.pop("pop")
			i.pop("visibility")
			i["temp Cº"] = i["main"]["temp"]
			i["feels_like Cº"] = i["main"]["feels_like"]
			i["temp_min Cº"] = i["main"]["temp_min"]
			i["temp_max Cº"] = i["main"]["temp_max"]
			i["wind"] = i["wind"]["speed"]
			i["main"] = i["weather"][0]["main"]
			i["description"] = i["weather"][0]["description"]
			i.pop("weather")
			i["rain"] = None
			i.pop("rain")
			i["clouds"] = i["clouds"]["all"]
			day, time = i["dt_txt"].split(" ")
			i["date"] = day
			i["time"] = time
			i.pop("dt_txt")
