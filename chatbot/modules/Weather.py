import requests
def reply():
    key = "2bb753668384a160e76ef2d7bbd3a61e"
    url = "https://api.openweathermap.org/data/2.5/weather?q="
    city="delhi"
    finalurl=url+city+"&appid="+key
    response=requests.get(finalurl)
    data=response.json()
    k=data["main"]["temp"]
    c=k-273.15
    return ("Weather in "+city+" : "+data["weather"][0]["main"]+"And Temperature : "+str(c))