import requests

# URL de la API
url = "http://127.0.0.1:5000/maximo"

# Datos para enviar en la solicitud
# Cambiar esta lista para probar otros casos
datos = {
    "numeros": [1, 2, 3]  
}

# Realizar la solicitud
response = requests.post(url, json=datos)

# Verificar la respuesta
if response.status_code == 200:
    print("Respuesta:", response.json())
else:
    print("Mensaje:", response.json())