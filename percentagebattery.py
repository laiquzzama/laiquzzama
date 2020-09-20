from pynotifier import Notification
import psutil
battery = psutil.sensors_battery()
percent = battery.percent
Notification("Batter Percentage", str(percent)+ "%Percent Remaining", duration=10).send()

