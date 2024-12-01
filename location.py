import phonenumbers 
from phonenumbers import timezone,geocoder,carrier


number = input("enter your number with country code like indian can use +91 :- ")

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_geographical_number(phone)
car = carrier.name_for_number(phone , "en")

reg = geocoder.description_for_number(phone,"en")


print(phone)
print(time)
print(car)
print(reg)