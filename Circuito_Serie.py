class Componente:
    def __init__(self, nombre, valor, corriente=0.0, voltaje=0.0, unidad=""):
        self.nombre = nombre
        self.valor = valor
        self.unidad = unidad
        self.corriente = corriente
        self.voltaje = voltaje

    def __str__(self):
        return f"""
        -----------------------------------
        Nombre: {self.nombre}
        Valor: {self.valor}
        Unidad: {self.unidad}
        Voltaje: {self.voltaje}
        Corriente: {self.corriente}
        -----------------------------------
        """

class Resistor(Componente):
    def __init__(self, nombre, valor):
        super().__init__(nombre, valor, unidad="Ω")

    def __str__(self):
        return f"{super().__str__()}"

class FuenteVoltaje(Componente):
    def __init__(self, nombre, valor):
        super().__init__(nombre, valor, unidad="V")
        self.voltaje = self.valor

    def __str__(self):
        return f"{super().__str__()}"

class Circuito:
    def __init__(self, componentes):
        self.componentes = componentes
        self.resistencia_total = 0.0
        self.corriente = 0.0

    def calcular_resistencia_total(self):
        for componente in self.componentes:
            if componente.unidad == "Ω":
                self.resistencia_total += componente.valor

    def calcular_corriente(self):

        for componente in self.componentes:
            if isinstance(componente, FuenteVoltaje):
                self.corriente = componente.valor / self.resistencia_total
                break 
        for componente in self.componentes:
            componente.corriente = round(self.corriente,5)

    def calcular_voltaje_componentes(self):
        for componente in self.componentes:
            if isinstance(componente, Resistor):
                componente.voltaje = self.corriente * componente.valor
                componente.voltaje = round(componente.voltaje,5)

    def mostrar_info_componentes(self):
        self.calcular_resistencia_total()
        self.calcular_corriente()
        self.calcular_voltaje_componentes()
        
        print(f"Resistencia total = {self.resistencia_total}")
        for componente in self.componentes:
            print(componente)

resistor1 = Resistor("r1", 100)
resistor2 = Resistor("r2", 1000)
fuente_v = FuenteVoltaje("E1", 5)

circuito1 = Circuito([fuente_v, resistor1, resistor2])

circuito1.mostrar_info_componentes()
