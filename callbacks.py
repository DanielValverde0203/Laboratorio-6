import time
import random
import threading
from eventos import EventManager  

class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()
        self.terminate_flag = False #condicion para terminar el programa

    def start_real_time_updates(self):
        while not self.terminate_flag: #Se modifico el bucle para que el programa termine
            time.sleep(3)
            self.generate_real_time_data()
            self.event_manager.notify("datos_actualizados", self.data)

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)


if __name__ == "__main__":
    # Crear una instancia de RealTimeDataManager
    real_time_data_manager = RealTimeDataManager()

    # Suscribir un callback al EventManager que imprime los datos actualizados
    def print_updated_data(data):
        print(f"Datos actualizados: {data}")

    real_time_data_manager.event_manager.subscribe("datos_actualizados", print_updated_data)

    # Actualizaciones en tiempo real en segundo plano
    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.daemon = True  
    update_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        real_time_data_manager.terminate_flag = True 
        print("\nPrograma terminado.")
