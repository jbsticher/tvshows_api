import requests, json, pprint, sys

url = "https://api.tvmaze.com/singlesearch/shows"
while True:
    show = input("Please input a tv show name: ")
    params = {"q":show}

    response = requests.get(url, params)

    if response.status_code == 200: 
        data = json.loads(response.text)
        # pprint.pprint(data)
        name = data['name']
        premiered = data['premiered']
        summary = data['summary']
        ended = data['ended']


        print(f"{name} premiered on {premiered}.")
        print(summary)
        print(f"{name} ended on {ended}.")
        print('Would you like to look up another tv show? ')
        if not input('> ').lower().startswith('y'):
            sys.exit("Thanks for stopping by!!!")
    else:
        print(f"Error: {response.status_code}")

        


