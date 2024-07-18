import os
import sys
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
######################################

print ("\033[31m")

os.system("figlet Hallo TO Moaz Mohamed Script ")
time.sleep(3)
os.system("clear")

print ("\033[1;34m")

os.system("figlet INFO Phone Number")

print ("\033[1;31m")

print ("x" * 60)

print ("\033[1;37m")

print ("\033[36m")

print ("BY:Moaz Mohamed")
print ("Github : https://github.com/MoazMohamed891")
print ("Linkedin : https://www.linkedin.com/in/moaz-mohamed-10b807318")



print ("\033[1;37m")

d = input("Enter Your Number :\033[1;32m ")

#Create PhoneNumber object
#None = code +20 a +1

print ("\033[35m")

a = phonenumbers.parse(d, None)
print (a)

print ("\033[2;31m")

r = geocoder.description_for_number(a, "en")
print (r)

print ("\033[32m")

k = carrier.name_for_number(a, "en")
print (k)

print ("\033[34m")

e = timezone.time_zones_for_number(a)
print (e)
