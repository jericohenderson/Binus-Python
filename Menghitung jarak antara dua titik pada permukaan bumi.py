import math

def harvestine(lat1, lon1, lat2, lon2)

#Konvrsi degrees ke radian

lat1= math.radians(lat1)
lon1= math.radians(lon1)
lat2= math.radians(lat2)
lon2= math.radians(lon2)

# Perbedaan

dlat = lat2 -lat1
dlon = lon2 - lon1

# Rumus 

a= (math.sin(dlat / 2) **2 + math.cos (lat1)*math.cos(lat2)*math.sin(dlon/2)**2)

c= 2* math.sin(math.sqet(a))

distance= r*c

print("Jarak(lat1, lat2, lat3, lat4), km")
                   
