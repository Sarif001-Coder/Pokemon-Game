import requests

base_url = "https://pokeapi.co/api/v2/"
name = input("Enter the name of the Pokemon: ").lower()

def pokemon_view(name):
    data = f"{base_url}/pokemon/{name}"
    response = requests.get(data)
    # Can be used later if needed to store the full response
    # Full_information = response
    if response.status_code == 200:
        infor = response.json()
        return infor
        # Full_information = oyeah.json()
        # print(message)
    else:
        print("Check your pokemon spelling")
        breakpoint  
        return None

def pokemon():
    pokemon_live = pokemon_view(name)
    if pokemon_live:
        print("---------Pokemon Information----------")
        print("Name:",f"{pokemon_live['name'].upper()}")
        print("ID:  ",f"{pokemon_live['id']}")
        print("Type:",pokemon_live['types'][0]["type"]["name"].upper())
        print("Move:",pokemon_live['moves'][18]["move"]["name"].upper())
        print("------------------End-----------------")
    else:
        print("No data available for the given Pokemon.")
    return pokemon_live

# https://www.dotnetfunda.com/interviews/show/4309/difference-json-arrary-vs-json-object

# main function for calling the pokemon_view function
if __name__ == "__main__":
    pokemon_view(name)
    pokemon()
