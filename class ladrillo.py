class Ladrillo:
    def _init_(self, altura, ancho, longitud):
        self.altura = altura
        self.ancho = ancho
        self.longitud = longitud

    def cantidad_ladrillos_por_metro_cuadrado(self):
        # Asumiendo una junta de 1.5 cm (0.015 m) entre ladrillos.
        area_con_junta = (self.longitud + 0.015) * (self.altura + 0.015)
        return 1 / area_con_junta

    def cantidad_ladrillos_en_pared(self, altura_pared, longitud_pared, desperdicio=0.05):
        # Calcula el área total de la pared
        area_pared = altura_pared * longitud_pared
        
        # Calcula la cantidad base de ladrillos
        cantidad_base = area_pared * self.cantidad_ladrillos_por_metro_cuadrado()
        
        # Agrega el porcentaje de desperdicio
        cantidad_total = cantidad_base * (1 + desperdicio)
        
        return int(cantidad_total) + 1  # Se redondea hacia arriba para asegurar suficientes ladrillos

# Solicitar datos del ladrillo al usuario
altura_ladrillo = float(input("Ingrese la altura del ladrillo en metros (ej. 0.07): "))
ancho_ladrillo = float(input("Ingrese el ancho del ladrillo en metros (ej. 1.25): "))
longitud_ladrillo = float(input("Ingrese la longitud del ladrillo en metros (ej. 0.24): "))

# Crear un objeto Ladrillo
ladrillo = Ladrillo(altura_ladrillo, ancho_ladrillo, longitud_ladrillo)

# Solicitar datos de la pared al usuario
altura_pared = float(input("Ingrese la altura de la pared en metros: "))
longitud_pared = float(input("Ingrese la longitud de la pared en metros: "))

# Calcular y mostrar la cantidad de ladrillos necesarios
cantidad_necesaria = ladrillo.cantidad_ladrillos_en_pared(altura_pared, longitud_pared)
print(f"\nPara una pared de {altura_pared}m x {longitud_pared}m, necesitarás aproximadamente {cantidad_necesaria} ladrillos.")
