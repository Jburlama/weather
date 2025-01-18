from src import weather
from tabulate import tabulate
from datetime import date
import sys

today = date.isoformat(date.today())
w = weather.Weather()

if len(sys.argv) == 1:
	t = tabulate(w.weather, headers="keys", tablefmt="fancy_grid")
	print(t)
	sys.exit()
elif sys.argv[1] == "today":
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
		day = i["date"].lstrip("2025-0")
		if i["date"] == sys.argv[1] or day == sys.argv[1]:
			table.append(i)
	t = tabulate(table, headers="keys", tablefmt="fancy_grid")
	print(t)
	sys.exit()

print("no data")
