import json
import urllib.request as request
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)
alist = data["result"]["results"]
# print(alist)
with open("data.csv","w",encoding="utf-8") as file:
    for place in alist:
        img=place["file"].split('https:')
        # print(img)
        # print(place["stitle"],place["address"][5:8],place["longitude"],place["latitude"],"https:",img[1])
        file.write(place["stitle"]+","+place["address"][5:8]+","+place["longitude"]+","+place["latitude"]+","+"https:"+img[1]+"\n")
        


