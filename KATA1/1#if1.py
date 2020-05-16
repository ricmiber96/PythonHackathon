password_guardada = "1234"

password_usuario = input("Introduce la contraseña:")
password_usuario = password_usuario.lower()



if password_usuario == password_guardada:
     print("El password es correcto")
else:
     print("El password no coincide")
