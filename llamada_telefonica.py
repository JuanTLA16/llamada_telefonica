


print("----------------------------------------")
print("-----------LLAMADA TELEFONICA-----------")
print("----------------------------------------")



dl = int(input( " Digite la duracion de la llamada: " ))


if dl<=3:
    CL= 300
else:
    CL = 300+50*(dl-3)


print(" El costo de la llamada es:  " + str( CL))
