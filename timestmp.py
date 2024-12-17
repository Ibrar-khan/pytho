import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hours = time.strftime('%H')
print(hours)
minutes = time.strftime('%M')
print(minutes)
seconds = time.strftime('%S')
print(seconds)

if(hours>0 and hours<12):
     print("Good Mornin Sir!")

elif(hours>12 and hours<17):
      "Good afternoon Sir"
if(hours>=17 and hours<=0):
     print("Good evening Sir!")