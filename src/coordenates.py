import requests
from key import key

class Coords:
	def __init__(self, city="Porto", country=None):
		url = "http://api.openweathermap.org/geo/1.0/direct?q={q}&limit={limit}&appid={key}"

		self._json = requests.get(url.format(q=city, limit=5, key=key)).json()
		self.coords = {"lon": None, "lat": None}

		if country:
			for i in self._json:
				if i["country"] == country:
					self.coords["lon"] = i["lon"]
					self.coords["lat"] = i["lat"]
		else:
			self.coords["lon"] = self._json[0]["lon"]
			self.coords["lat"] = self._json[0]["lat"]	

		self.lat = self.coords["lat"]
		self.lon = self.coords["lon"]
			
	def get_lat(self):
		return self.coords["lat"]

	def get_lon(self):
		return self.coords["lon"]

	def __str__(self):
		return f"lat: {self.coords['lat']}\nlon: {self.coords['lon']}"
