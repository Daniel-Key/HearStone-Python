import requests

class API:

    url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/"
    headers = {
            'x-rapidapi-host': "omgvamp-hearthstone-v1.p.rapidapi.com",
            'x-rapidapi-key': "GrLtRslXk3msh2IIAusU2J31rw2ep1l2YdWjsnAK9sbBMYKzEA"
        }

    def requestCardInfo(self, id):
        response = requests.request("GET", self.url + id, headers=self.headers)
        # print(id)
        # print(self.url + str(id))
        print(response.text)