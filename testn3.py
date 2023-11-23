def insert_n_character(line, interval=43):
    target_position = interval

    # obtener el numero de intervalo que es actualmente, ejemplo 1, 2, 3
    intervalo_div = int(target_position / 43)
    # print('El intervalo es: ' + str(intervalo_div))

    # si ya no es el primer intervalo, sumar 3 al target position por el intervalo_div
    if intervalo_div != 1:
        target_position += 3 * intervalo_div
        # print('La primera mas intervalo_div posicion es: ' +
        # str(target_position))  # v2

    # if intervalo_div == 2:
    #     target_position += 3
    #     print('La primera mas intervalo_div posicion es: ' + str(target_position))
    # if intervalo_div == 3:
    #     target_position += 6
    #     print('La primera mas intervalo_div posicion es: ' + str(target_position))
    # if intervalo_div == 4:
    #     target_position += 9
    #     print('La primera mas intervalo_div posicion es: ' + str(target_position))
    # if intervalo_div == 5:
    #     target_position += 12
    #     print('La primera mas intervalo_div posicion es: ' + str(target_position)) # V2_2

    if len(line) <= target_position or len(line) <= target_position + 2:
        return line

    left_bracket = line.rfind('[', 0, target_position)
    right_bracket = line.find(']', target_position)

    # print('La primera posicion es: ' + str(target_position))

    # checar si en ese intervalo, hay brakets y si estan antes del target position
    if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:
        # si hay brakets, sumar los caracteres brakets y su contenido al target position
        sum_brackets = line[left_bracket:right_bracket + 1]
        target_position += len(sum_brackets)
        # print('La segunda posicion es: ' + str(target_position))

    # obtener el ultimo espacio antes del target position de value
    last_space_position = line.rfind(' ', 0, target_position)

    # si target position no es un espacio, colocar target position en el ultimo espacio antes de target position remplazando el espacio
    if last_space_position == -1:
        return line
    else:
        target_position = last_space_position

    # Reemplazar el carácter en la posición objetivo con '[n]'
    line = line[:target_position] + '[n]' + line[target_position + 1:]

    return insert_n_character(line, interval=interval + 43)


value = "He estado esperando tu llegada tan[f 6 1 3 0 7] fervientemente que mis ojos comenzaron a[f 6 1 3 0 7] golpearme de mi Skull,como aaaaaaaaaaaa[f 6 1 2 0 4] los de nuestro maestro."
value2 = "Si hay alg雨n material que ya hayas vendido aqu胤, ahora a隠adir姻 nuevas acciones hechas de esos."
value = insert_n_character(value)

print(value)
