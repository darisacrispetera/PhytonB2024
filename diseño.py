arreglos = [[50,40,"estándar"],[25,200,"express"],[5,70,"prioritario"]]
for envios in arreglos:

    if envios[2] == "estándar":
        if envios[0] <= 12:
            envios[0] *= 4    
        elif 30>= envios[0] >12:
            envios[0] *= 7
        elif envios[0] >30:
            envios[0] *= 10
        if envios[1] <=90:
            envios[1] *= 2
        elif envios[1] >90:
            envios[1] *= 1.25
        valor = envios[1]+envios[0]
        print("el valor del envío 1 es: ",valor)
    elif envios[2] == "express":
        if envios[0] <= 12:
            envios[0] *= 4*1.2
        elif 30>= envios[0] >12:
            envios[0] *= 7*1.2
        elif envios[0] >30:
            envios[0] *= 10*1.2
        if envios[1] <=90:
            envios[1] *= 2*1.6
        elif envios[1] >90:
            envios[1] *= 1.25*1.6
        valor = envios[1]+envios[0]
        print("el valor del envío 2 es: ",valor)
    elif envios[2] == "prioritario":
        if envios[0] <= 12:
            envios[0] *= 4*1.5
        elif 30>= envios[0] >12:
            envios[0] *= 7*1.5
        elif envios[0] >30:
            envios[0] *= 10*1.5
        if envios[1] <=90:
            envios[1] *= 2*2
        elif envios[1] >90:
            envios[1] *= 1.25*2
        valor = envios[1]+envios[0]
        print("el valor del envío 3 es: ",valor)