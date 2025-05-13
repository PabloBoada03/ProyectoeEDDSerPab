import json

class JsonManager:
    @staticmethod
    def cargar_json(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)

    @staticmethod
    def guardar_json(archivo, data):
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
