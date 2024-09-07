usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'} 


try: 
    print(usuarios['004']) 

except KeyError: 
    print("Error: Debes ingresar una clave correcta") 

except Exception as e: 
    print(f"Ha ocurrido un error", e) 

print("continua el codigo")    