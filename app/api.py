from flask import Flask, request, jsonify
from funcion import encontrar_maximo

app = Flask(__name__)

@app.route('/maximo', methods=['POST'])
def obtener_maximo():
    """
    Encuentra el valor máximo en una lista de números.

    Parameters
    ----------
    datos: JSON
        Debe contener una clave "numeros" con una lista de números
    
    Returns
    -------
    JSON
        Devuelve la clave "maximo" que contiene el valor máximo de la lista.
        En caso de error, devuelve la clave "error"
    """
    try:
        # Obtener los datos de la solicitud
        datos = request.get_json()
        lista_de_numeros = datos.get("numeros", [])
        
        # Llamar a la función para encontrar el máximo
        resultado = encontrar_maximo(lista_de_numeros)
        
        # Devolver el resultado
        return jsonify({"maximo": resultado})
    
    # Manejar errores
    except ValueError:
        return jsonify({"error": "Todos los elementos de la lista deben ser números int o float"})
    except Exception:
        return jsonify({"error": "Error del servidor"})

if __name__ == '__main__':
    app.run(debug=True)