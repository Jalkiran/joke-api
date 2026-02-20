import requests
joke2_url="https://official-joke-api.appspot.com/random_joke"
while True:
    choice=input("Press Enter for a joke OR q for quit:").strip().lower()
    if choice=='q':
        print("goodbye")
        break
    
    response=requests.get(joke2_url)
    data=response.json()

    print(data["setup"])
    print(data["punchline" ])
    print()
