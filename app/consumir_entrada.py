import requests

# URL de la API
url = "http://127.0.0.1:5000/maximo"

# Pedir entrada como input 
entrada = input("""Ingrese una lista de números
Dejar un espacio entre cada número: """)
lista_numeros = [float(i) for i in entrada.split()]

# Datos para enviar en la solicitud
# Cambiar esta lista para probar otros casos
datos = {
    "numeros": lista_numeros
}

# Realizar la solicitud
response = requests.post(url, json=datos)

# Verificar la respuesta
if response.status_code == 200:
    print("Respuesta:", response.json())
else:
    print("Mensaje:", response.json())