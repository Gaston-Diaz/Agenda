import PySimpleGUI as sg
import json

# Función para guardar los datos en un archivo JSON
def guardar_contactos(contactos):
    with open("contactos.json", "w") as f:
        json.dump(contactos, f)

# Función para cargar los datos desde un archivo JSON
def cargar_contactos():
    try:
        with open("contactos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Función para mostrar la lista de contactos
def mostrar_contactos():
    sg.popup('Lista de Contactos', '\n'.join(contacto['nombre'] + ' - ' + contacto['telefono'] for contacto in contactos))

# Función para agregar un nuevo contacto
def agregar_contacto():
    layout = [
        [sg.Text('Nombre:'), sg.InputText(key='nombre')],
        [sg.Text('Teléfono:'), sg.InputText(key='telefono')],
        [sg.Button('Guardar'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Agregar Contacto', layout)
    event, values = window.read()
    window.close()

    if event == 'Guardar':
        contactos.append({'nombre': values['nombre'], 'telefono': values['telefono']})
        guardar_contactos(contactos)
        sg.popup('Contacto guardado correctamente')

# Cargar los contactos existentes
contactos = cargar_contactos()

# Definir el diseño de la interfaz gráfica
layout = [
    [sg.Button('Ver Contactos')],
    [sg.Button('Agregar Contacto')],
    [sg.Button('Salir')]
]

# Crear la ventana con el diseño
window = sg.Window('Agenda', layout)

# Loop para manejar eventos y actualizaciones de la ventana
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Salir':
        break
    elif event == 'Ver Contactos':
        mostrar_contactos()
    elif event == 'Agregar Contacto':
        agregar_contacto()

# Cerrar la ventana al salir del loop
window.close()
