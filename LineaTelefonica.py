class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Numero de llamadas realizadas
    numeroLlamadas=0
    
    # Numero de minutos consumidos
    numeroMinutos=0
    
    # Costo total de las llamadas
    costoLlamadas=0
    
    #Estratos 
    estrato=0
    
    #Descuento del 0.0 al 25.5
    descuento=0.25
    
    #Saldo desponible
    saldoDisponible =0
    
    #Almacenar Total de segundos
    totalSegundos=0
    
    #Almacenar costo de llamada
    costoDolares=0
    
    #Cantidad de minutos de llamada a celular
    minutosCelular=0
    
    #Cantidad de minutos de llamadas a celular 
    costoLlamadaCelular=0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        # TODO Parte2 PuntoA: Completar el método según la documentación dada.
        # Aqui va el codigo
        self.numeroLlamadas =0
        self.numeroMinutos= 0
        self.costoLlamadas=0
        self.totalSegundos=0
        self.costoDolares =0
        self.minutosCelular=0
        self.costoLlamadaCelular=0
    
    def darEstrato (self):
        #Aqui va el codigo
        return self.estrato
    

    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        #Aqui va el codigo 
        return self.costoLlamadas
    
    def Consultarminutoscelular(self):
        consultarMinutosCelular = self.minutosCelular
        return consultarMinutosCelular
    
    def ConsultarcostoLlamadaCelular(self):
        consultarcostoLlamadaCelular = self.costoLlamadaCelular
        return consultarcostoLlamadaCelular
        
    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        #Aqui va el codigo
        return self.numeroLlamadas
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.
        return self.numeroMinutos
    
    def darMinutosCelular(self):
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        #Aqui va el codigo 
        return self.minutosCelular
    
    def darCostoLlamadaCelular(self):
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        #Aqui va el codigo 
        return self.costoLlamadaCelular

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        # TODO Parte2 PuntoE: Completar el método según la documentación dada.
        self.numeroLlamadas=0
        self.numeroMinutos=0
        self.costoLlamadas=0
        self.costoDolares=0
        self.totalSegundos=0
        self.minutosCelular=0
        self.costoLlamadaCelular=0
    
    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos):
        
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35

    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
        """

    def agregarLlamadaLargaDistancia(self, pMinutos):
        # TODO Parte2 PuntoF: Completar el método según la documentación dada.

        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += int(pMinutos)
        # Suma el costo (costo por minuto: 380 pesos)
        self.costoLlamadas += int(pMinutos) * 380

    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self):
        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
           
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += self.minutosCelular
        # Suma el costo (costo por minuto: 999 pesos)
        self.costoLlamadaCelular += self.minutosCelular * 999
        # Actualizar el costo total de las llamadas
        self.costoLlamadaCelular+= self.costoLlamadaCelular
        # Resta el costo de la llamada al saldo disponible
        self.saldoDisponible -= self.costoLlamadaCelular
        
    def darDescuentoLineaTelefonica (self):
        return self.descuento

    def darAplicarDescuento(self):
        descuento = (self.darCostoLlamadas() * self.descuento)/100
        return descuento
    
    def SaldoDisponible(self):
        descuentoAplicado = self.darAplicarDescuento()
        saldoDisponible = self.darCostoLlamadas() - descuentoAplicado
        return saldoDisponible
    
    def aumentarSaldo(self, valor):
        self.saldoDisponible += valor
        
    def agregarLlamadaLocal(self, pMinutos):
        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        costoLlamadas += pMinutos * 35
        # Actualizar el costo total de las llamadas
        self.costoLlamadas += costoLlamadas
        # Resta el costo de la llamada al saldo disponible
        self.saldoDisponible -= costoLlamadas
        
    def motivarCliente(self):
        if self.numeroMinutos >=30:
            self.saldoDisponible += 1000
    
    def ConvertirPesosADolares (self):
        convertir = float(self.costoLlamadas/3100)
        self.costoDolares = convertir
        return convertir
        
    def definirEstratoLinea1(self, pEstrato):
        self.linea1(pEstrato)

    def darMinutosPorEstrato(self):
        self.numeroMinutos * self.linea1.estrato
        self.numeroMinutos * self.linea2.estrato
        self.numeroMinutos * self.linea3.estrato
    
    