import sys
import requests

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = "Hello, {} ".format(who_to_greet)
    return greeting

print(greet('world'))
print(greet("bob"))

r = requests.get("https://www.youtube.com/watch?v=06I63_p-2A4&t=108s")
print(r.status_code)