import requests


r = requests.get("https://www.youtube.com/watch?v=06I63_p-2A4&t=108s")
print(r.status_code)