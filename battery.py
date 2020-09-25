# pip install psutil
import psutil
# pip install plyer and import notification from plyer 
from plyer import notification 
import time   

battery = psutil.sensors_battery()  

while(True): 
    percent = battery.percent       
    notification.notify( 
        title="Battery Percentage", 
        message=str(percent)+"% Battery remaining", 
        timeout=10
    )
    # after every 60 mins it will show the 
    # battery percentage 
    time.sleep(60*60)