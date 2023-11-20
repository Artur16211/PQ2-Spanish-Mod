import re

value_original = "He estado esperando tu llegada tan fervientemente que mis ojos comenzaron a[f 6 1 3 0 7] golpearme de mi Skull,como aaaaaaaaaaaa[f 6 1 2 0 4] los de nuestro maestro."

# Encuentra todas las ocurrencias de contenido dentro de corchetes que comienzan con [f y guarda la posición
brace_positions = [(m.start(), m.end(), m.group())
                   for m in re.finditer(r'\[f[^\]]*?\]', value_original)]

# Remueve el contenido dentro de corchetes que comienzan con [f
value_woutb = re.sub(r'\[f[^\]]*?\]', '', value_original)

# inserta los corchetes y el contenido en sus posiciones originales
reconstructed_value = value_woutb
for brace_position in brace_positions:
    reconstructed_value = reconstructed_value[:brace_position[0]] + \
        brace_position[2] + reconstructed_value[brace_position[0]:]

print(value_original)
print(value_woutb)
print(reconstructed_value)

# inserta [n] en un intervalo de 43 caracteres, en el value_woutb


def insert_n_character(line, interval=43):
    target_position = interval

    # Comprueba si la posición objetivo está dentro de la longitud de la línea
    if target_position < len(line):
        # Inserta [n] en la posición objetivo
        if line[target_position] == ' ':
            line = line[:target_position] + '[n]' + line[target_position:]
        else:
            # Encuentra el último espacio antes de la posición objetivo
            last_space_position = line.rfind(' ', 0, target_position)
            if last_space_position == -1:
                return line
            else:
                line = line[:last_space_position] + \
                    '[n]' + line[last_space_position:]

        # Llama recursivamente a la función con un intervalo incrementado
        return insert_n_character(line, interval=interval + 43)
    else:
        return line


value_woutb_n = insert_n_character(value_woutb)
print(value_woutb_n)

# Vuelve a insertar los corchetes y el contenido en sus posiciones originales

# En caso de que en su ubicacion original, haya un [, n o ], se colocara despues del ], para evitar errores o que se pierda informacion
reconstructed_value = value_woutb_n

for brace_position in brace_positions:
    # si en la posicion original hay un [, n o ], se coloca despues del ]
    if reconstructed_value[brace_position[0]] == '[' or reconstructed_value[brace_position[0]] == 'n' or reconstructed_value[brace_position[0]] == ']':
        reconstructed_value = reconstructed_value[:brace_position[0] + 1] + \
            brace_position[2] + reconstructed_value[brace_position[0] + 1:]
    # si la posición original no es un espacio, se colocara en el siguiente espacio
    elif reconstructed_value[brace_position[0]] != ' ':
        next_space_position = reconstructed_value.find(' ', brace_position[0])
        reconstructed_value = reconstructed_value[:next_space_position] + \
            brace_position[2] + reconstructed_value[next_space_position:]


print(reconstructed_value)
