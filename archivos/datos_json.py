import requests

def mis_datos(nombre_a_buscar):
    # URL de la API
    url = "https://jsonplaceholder.typicode.com/users"

    # Realizamos la solicitud GET
    respuesta = requests.get(url)

    # Verificamos que la respuesta fue exitosa (código 200)
    if respuesta.status_code == 200:
        usuarios = respuesta.json()  # Convertimos a lista de diccionarios (JSON)
        # Procesamos los datos: por ejemplo, mostrar nombre y correo de cada usuario
        encontrado = []
        for datos in usuarios:
            user = datos['name']
            if datos['name'].lower().startswith(nombre_a_buscar.lower()):
                encontrado.append(user)
        if encontrado:
            for usuario in encontrado:
                print(usuario)
                #print(f"ID: {usuario['id']}, nombre: {usuario['name']} vive en: {usuario['address']['city']}")
        else:
            print("No existe el usuario")
    else:
        print("Error al conectarse a la API", respuesta.status_code)


mis_datos("e")