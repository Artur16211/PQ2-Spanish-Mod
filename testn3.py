def insert_n_character(line, interval=33):
    target_position = interval

    if len(line) <= target_position + 3:
        return line

    space_before = line.rfind(' ', 0, target_position)
    space_after = line.find(' ', target_position)

    if space_before == -1 and space_after == -1:
        return line

    if space_before == -1:
        insert_position = space_after
    elif space_after == -1:
        insert_position = space_before
    else:
        # Encuentra el espacio más cercano hacia atrás
        space_before_distance = target_position - space_before

        # Encuentra el espacio más cercano hacia adelante
        space_after_distance = space_after - target_position

        # Compara los caracteres antes del espacio y selecciona el espacio más cercano
        if space_before_distance <= space_after_distance:
            insert_position = space_before
        else:
            insert_position = space_after

    line = line[:insert_position] + '[n]' + line[insert_position+1:]

    return insert_n_character(line, interval=interval + 43)


# Ejemplo de uso
input_line = 'Sinopsis: La Kamociudad, liberada del r姻gimen de su tirano, todav胤a lucha contra una niebla de maldad que est茨 corrompiendo las mentes de la gente en todo el pa胤s. 斡Gritan por una verdadera paz!'
result_line = insert_n_character(input_line, interval=38)
print(result_line)
