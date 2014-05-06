#!/etc/python3
import time
import datetime

startzeit=int(time.time()*1000)
print("startzeit: ",startzeit,"\tjahr: ",time.gmtime().tm_year)
i=0
while(i<10):
	print("zeit: ",time.time()*1000," \tintervall: ",int(time.time()*1000)-startzeit)
	i=i+1
startzeit2=datetime.datetime.now().microsecond
i=0;
print("startzeit2: ",startzeit2)
while(i<10):
	print("zeit2: ",(datetime.datetime.now().microsecond)-startzeit2)
	i=i+1
