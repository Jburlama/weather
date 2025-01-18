from . import coordenates
from key import key
import requests

class Current(coordenates.Coords):
	def __init__(self, city="Porto", country=None):
		super().__init__(city, country)

		url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"
		url = url.format(lat=self.get_lat(), lon=self.get_lon(), key=key)
		self.r = requests.get(url).json()

		self.description = self.r["weather"][0]["description"]
		self.temp = self.r["main"]["temp"]
		self.feels_like = self.r["main"]["feels_like"]
		self.min = self.r["main"]["temp_min"]
		self.max = self.r["main"]["temp_max"]
		self.pressure = self.r["main"]["pressure"]
		self.humidity = self.r["main"]["humidity"]
		self.wind_speed = self.r["wind"]["speed"]
		self.clouds = self.r["clouds"]["all"]

	def __str__(self):
		s = "lat:{lat}\nlon: {lon}\ndescription: {description}\ntemp: {temp}\nfeels_like: {feels}\nmin: {mi}\nmax: {ma}\npresure: {pressure}\nhumidity: {humidity}\nwind_speed: {wind_speed}\nclouds: {clouds}"
		return s.format(
					lat=self.lat,
					lon=self.lon,
					description=self.description,
					temp=self.temp,
					feels=self.feels_like,
					mi=self.min,
					ma=self.max,
					pressure=self.pressure,
					humidity=self.humidity,
					wind_speed=self.wind_speed,
					clouds=self.clouds
				)
