import requests

cardUrl = "https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/"
headers = {
        'x-rapidapi-host': "omgvamp-hearthstone-v1.p.rapidapi.com",
        'x-rapidapi-key': "GrLtRslXk3msh2IIAusU2J31rw2ep1l2YdWjsnAK9sbBMYKzEA"
    }

def requestCardInfo(id):
    response = requests.request("GET", cardUrl + id, headers=headers)
    # print(response.text)
    return response.text