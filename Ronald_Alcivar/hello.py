import hashlib
mensaje = "Hola Mundo"
cifrado = hashlib.sha256(mensaje.encode()).hexdigest()
print("Mensaje cifrado:", cifrado)
