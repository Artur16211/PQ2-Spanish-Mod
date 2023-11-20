def insert_n_character(line, interval=43):
    target_position = interval
    if len(line) <= target_position or len(line) <= target_position + 2:
        return line

    left_bracket = line.rfind('[', 0, target_position)
    right_bracket = line.find(']', target_position)

    # check if the target position is inside a bracket
    if left_bracket != -1 and right_bracket != -1 and left_bracket < right_bracket:
        insert_position = right_bracket + 1
    else:
        left_space = line.rfind(' ', 0, target_position)
        right_space = line.find(' ', target_position)

        if left_space == -1 and right_space == -1:
            return line
        if left_space == -1:
            insert_position = right_space
        elif right_space == -1:
            insert_position = left_space + 1
        else:
            if abs(target_position - left_space) <= abs(right_space - target_position):
                insert_position = left_space + 1
            else:
                insert_position = right_space

    line = line[:insert_position] + '[n]' + line[insert_position:]
    return insert_n_character(line, interval=interval + 43)


value = "He estado esperando tu llegada tan fervientemente que mis ojos comenzaron a[f 6 1 3 0 7] golpearme de mi Skull,como aaaaaaaaaaaa[f 6 1 2 0 4] los de nuestro maestro."
value2 = "Si hay alg雨n material que ya hayas vendido aqu胤, ahora a隠adir姻 nuevas acciones hechas de esos."
value = insert_n_character(value)

print(value)

# si
