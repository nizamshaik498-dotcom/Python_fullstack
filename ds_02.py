#TUPLE

days=('mon','tue','wed','thu','fri')
coords=(13.0827,80.2707)
single=(42,)
rgb=(255,128,0)
print(days[0])
print(days[-1])
print(days[1:3])
print('mon' in days)


lat,lon=coords
print(f"Lat:{lat},Lon:{lon}")
r,g,b=rgb
print(f"Red={r} Green={g} Blue={b}")
def min_max(nums):return min(nums),max(nums)
lo,hi =min_max([3,7,1,9,4])
print(f"Min={lo},Max={hi}")

locations={ (13.08, 80.27): "Dubai",(28.61,77.20): "Abu_dhabi"}
print(locations[(13.08, 80.27)])