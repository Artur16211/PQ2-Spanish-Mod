import tkinter as tk
from tkinter import ttk
import mmap
import struct


class GTXEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor GTX")

        self.entries = [ttk.Entry(root, width=5, state="readonly")
                        for _ in range(8)]

        for i in range(8):
            label = ttk.Label(root, text=f"Valor {i + 1}:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

            entry = self.entries[i]
            entry.grid(row=i, column=1, padx=5, pady=5)

        load_button = ttk.Button(
            root, text="Cargar desde archivo", command=self.load_values)
        load_button.grid(row=8, column=0, columnspan=2, pady=10)

    def load_values(self):
        try:
            with open(r'C:\Users\Arthu\OneDrive\Documentos\PQ2-Spanish-Mod\GTX\Ticket.gtx', 'rb') as file:
                with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_file:
                    offset = 0x40 + 0x0C
                    mmapped_file.seek(offset)

                    for i in range(8):
                        # Leer 2 bytes y decodificarlos como little-endian
                        value = struct.unpack('<H', mmapped_file.read(2))[0]
                        # Formatear como cadena "01 00"
                        formatted_value = "{:02X} {:02X}".format(
                            value & 0xFF, (value >> 8) & 0xFF)
                        self.entries[i].config(state="normal")
                        self.entries[i].delete(0, tk.END)
                        self.entries[i].insert(0, formatted_value)
                        self.entries[i].config(state="readonly")

        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Error al cargar los valores: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    editor = GTXEditor(root)
    root.mainloop()
