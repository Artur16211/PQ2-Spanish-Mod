import struct

def find_and_read_coordinates(file_path):
    coordinates = []
    with open(file_path, 'rb') as file:
        data = file.read()
        start_index = data.find(b'\x01\x00\x01\x00')
        
        if start_index == -1:
            print("No se encontraron coordenadas en el archivo.")
            return coordinates

        # Leer bloques de 8 bytes después de encontrar la primera coordenada
        index = start_index
        while index < len(data):
            # Verificar si hay al menos 8 bytes restantes
            if index + 8 > len(data):
                break

            # Extraer las coordenadas en formato little-endian
            X1 = struct.unpack('<H', data[index:index+2])[0]
            Y1 = struct.unpack('<H', data[index+2:index+4])[0]
            X2 = struct.unpack('<H', data[index+4:index+6])[0]
            Y2 = struct.unpack('<H', data[index+6:index+8])[0]

            # Almacenar las coordenadas en la lista
            coordinates.append((X1, Y1, X2, Y2))
            
            # Avanzar al siguiente bloque de 8 bytes
            index += 8
            
            break
    
    return coordinates

# Ejemplo de uso
file_path = 'Ticket.gtx'
coordinates = find_and_read_coordinates(file_path)

# Imprimir todas las coordenadas
for i, (X1, Y1, X2, Y2) in enumerate(coordinates):
    print(f'Coordenadas {i+1}:')
    print(f'  X1 = {X1}')
    print(f'  Y1 = {Y1}')
    print(f'  X2 = {X2}')
    print(f'  Y2 = {Y2}')
