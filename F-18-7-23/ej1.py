def mi_deposito(envios):
    # incio la lista de las plataformas
    plataformas = []
    # por cada envio en envios
    for envio in envios:
        # i indica la plataforma en la que debo cargar la caja actual
        for i in range(len(envio)):
            # si la plataforma nro "i" no existia
            # entonces la creo y cargo el envio correspondiente
            # sino, reviso si no aplasta las cajas de abajo
            if(len(plataformas) <= i):
                plataformas += [[envio[i]]]
            else:
                # creo una lista para el nuevo estado de la plataforma "i"
                nuevo_estado = []
                # uso j para acceder a las cajas que ya tenia en la plataforma "i"
                for j in range(len(plataformas[i])):
                    # si la caja nro "j" en la plataforma nro "i" es menos pesada que la que quiero poner
                    # entonces todas las que estan por encima de la "j" tambien van a ser menos pesadas
                    # por lo tanto salgo del ciclo para cargar la nueva caja
                    if(plataformas[i][j] < envio[i]):
                        break
                    # si la caja nro "j" es mas pesada
                    # entonces permanece donde esta
                    else:
                        nuevo_estado += [plataformas[i][j]]
                # inserto la nueva caja
                nuevo_estado += [envio[i]]
                # actualizo el estado de la plataforma "i"
                plataformas[i] = nuevo_estado

    # retorno el estado final de las plataformas
    return plataformas

# Ejemplo 1
envio_1 = [5, 2, 3]
envio_2 = [2, 4]
envios = [envio_1, envio_2]

#print(envios)
plataformas = mi_deposito(envios)
print(plataformas)

# Ejemplo 2
envio_1 = [5, 3, 2]
envio_2 = [2, 4]
envio_3 = [1, 3, 6]
envios = [envio_1, envio_2, envio_3]

plataformas = mi_deposito(envios)
print(plataformas)