import requests

def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()


    for pais in paises:
        #print(f" Nombre Comun: {pais['name']['common']}")
        #print(f" Nombre Oficial: {pais['name']['oficial']}")
        #print(f" Nombre Oficial: {pais['oficial']}")
        print(f" Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f" La capítal es: {pais['capital'] [0]}")
        print(f" Moneda: {pais['curriencies'].keys()}")
        print(f" Codigo Telefonico: {pais['callingCodes'][0]}")

        #print(pais)


url = 'https://restcountries.com/v3.1/independent?status=true&fields=name,callingCodes,curriences'
listar_nombre_paises(url)