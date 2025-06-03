""" from reportlab.pdfgen import canvas

# Crear un objeto Canvas y definir el nombre del archivo
c = canvas.Canvas("ejemplo.pdf")
# Escribir texto en coordenadas (x, y)
c.drawString(100, 750, "Hola, este es un PDF creado con ReportLab.")
# Guardar el PDF
c.save() """


import requests
# URL de la API
url = "https://jsonplaceholder.typicode.com/posts/1"
# Hacer la solicitud GET
respuesta = requests.get(url)
# Verificar si la respuesta fue exitosa (código 200)
if respuesta.status_code == 200:
    datos = respuesta.json()  # Convertir a diccionario
    print("Título del post:", datos["title"])
    print("El contenido de post: ", datos['body'])
else:
    print("Error al hacer la solicitud:", respuesta.status_code)
