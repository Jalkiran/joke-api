import requests
joke2_url="https://official-joke-api.appspot.com/random_joke"
while True:
    choice=input("Press Enter for a joke OR q for quit:").strip().lower()
    if choice=='q':
        print("goodbye")
        break
    
    response1=requests.get(joke2_url)
    data=response1.json()

    print(data["setup"])
    print(data["punchline" ])

    print()


print("Thanks for using the joke app!")
print("Have a great day!")
print("Goodbye!")
print("Hello")
