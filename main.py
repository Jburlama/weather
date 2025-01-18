from src import weather
from tabulate import tabulate
from datetime import date
import sys

city = "Porto"
country = "PT"
day = "all"

try:
	for i in range(len(sys.argv))[1:]:
		arg1, arg2 = sys.argv[i].split("=")
		match arg1:
			case "city":
				city = arg2
			case "country":
				country = arg2
			case "day":
				day = arg2
	
	today = date.isoformat(date.today())
	w = weather.Weather(city=city, country=country)
	if day == "all":
		t = tabulate(w.weather, headers="keys", tablefmt="fancy_grid")
		print(t)
		sys.exit()
	elif day == "today":
		table = []
		for i in w.weather:
			if i["date"] == today:
				table.append(i)
		t = tabulate(table, headers="keys", tablefmt="fancy_grid")
		print(t)
		sys.exit()
	else:
		table = []
		for i in w.weather:
			tday = i["date"].lstrip("2025-0")
			if i["date"] == day or tday == day:
				table.append(i)
		t = tabulate(table, headers="keys", tablefmt="fancy_grid")
		print(t)
		sys.exit()
	
	print("no data")
except ValueError:
	print(
		"Usage: 'python3 main.py day=day city=city country=county'\n\n" +
		"By defaut, eg: 'python3 main.py', city=Porto, country=PT, and day will show the following 5 days from today.")
