

year_of_birth = int(input("ingrese su año de nacimiento: "))


from datetime import date #biblioteca

currente_year = date.today().year #obtiene automaticamente el año actual

age = currente_year - year_of_birth

print(f"Tienes actualmente {age} años")


