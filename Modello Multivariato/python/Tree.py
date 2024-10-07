import numpy as np
import pandas as pd
from math import floor
import math


class Tree():
    
    def __init__(self, D):
         
         self.D = D
         self.features = 15
         self.osservazioni = 150
         self.mu = 0.00005
         self.total_nodes = 2**(D + 1)-1
         self.branch_nodes = floor(self.total_nodes/2)
         #self.a = np.zeros(self.features * self.branch_nodes).reshape(self.features, self.branch_nodes)
         #self.b = np.zeros(self.branch_nodes)
         self.dati = pd.read_csv("C:\\Users\\UTENTE\\Desktop\\Tesi magistrale modello\\python\\dati.txt", delimiter=';')
         self.x = self.dati[ ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'] ].to_numpy()
         self.convert_to_float()
         self.normalizzazione()
         self.y = self.dati['15'].to_numpy()
         self.a = np.loadtxt("C:\\Users\\UTENTE\\Desktop\\Tesi magistrale modello\\python\\a.txt")
         self.b = np.loadtxt("C:\\Users\\UTENTE\\Desktop\\Tesi magistrale modello\\python\\b.txt")
         self.c_kt = np.loadtxt("C:\\Users\\UTENTE\\Desktop\\Tesi magistrale modello\\python\\c_kt.txt")
         self.nodo_foglia_calcolato = np.zeros(self.osservazioni)         
         self.classe_calcolata = np.zeros(self.osservazioni)    
         self.falsi_positivi = 0
         self.falsi_negativi = 0
         self.veri_positivi = 0
         self.veri_negativi = 0
         self.accuratezza = 0
         self.richiamo = 0
         self.precisione = 0
         
         
     
    def convert_to_float(self):
            
        for i in range(0, self.osservazioni, 1):
             
            for p in range(0, self.features, 1):
                
                if(isinstance(self.x[i,p], str)):
                        self.x[i,p] = self.x[i,p].replace(',' , '.')
                    
                self.x[i,p] = float(self.x[i,p])
    
    
    
    def normalizzazione(self):
        
        for i in range(0, self.osservazioni, 1):
             
            for p in range(0, self.features, 1):
                
                if(self.x[:,p].min() != self.x[:,p].max()):
                    self.x[i,p] = ( self.x[i,p] - self.x[:,p].min() )/ (self.x[:,p].max() - self.x[:,p].min() )
     
        
     
        
    def validazione(self):
        
    #calcolo in nodo foglia in cui cade un x(i)
        
        for i in range(0, self.osservazioni, 1):
            
            t = 1
            
            while t <= self.branch_nodes:
            
                temp = float(0)    
            
                for p in range(0, self.features, 1):
                  
                    temp += self.a[p,t-1] * self.x[i,p]
                
                #importante è l'arrotondamento. intanto 5 cifre decimali sembra essere quello giusto.ricorda che i solutori tipo cplex considerano una variabile integrale se è >= a 1e-05, altrimenti l'arrotondano
                if( round(temp, 5) + self.mu <= round(self.b[t-1], 5) ):
                    
                    self.nodo_foglia_calcolato[i] = t*2
                    t = t*2
                
                else:
                    
                    self.nodo_foglia_calcolato[i] = t*2 + 1
                    t = t*2 + 1
                    
                    
    #assegno una classe al x(i)
    
        for i in range(0, self.osservazioni, 1):
            
            #range del numero totale di foglie
            for l in range( 0, 2**(self.D + 1), 1):
                
                if( self.c_kt[l, 0] == 0 and  self.c_kt[l, 2] == 1 ):
                    
                    if(self.nodo_foglia_calcolato[i] == self.c_kt[l, 1]):
                    
                        self.classe_calcolata[i] = 0
                
                if( self.c_kt[l, 0] == 1 and  self.c_kt[l, 2] == 1 ):
                    
                    if(self.nodo_foglia_calcolato[i] == self.c_kt[l, 1]):
                    
                        self.classe_calcolata[i] = 1
                      
            
        #calcolo o falsi positivi, negativi ecc.
        #classe zero pazienti sopravvissuti, 1 deceduti
        for i in range(0, self.osservazioni, 1):
            
            if( self.classe_calcolata[i] == 0 and self.y[i] == 0):
                
                self.veri_negativi += 1
            
            if( self.classe_calcolata[i] == 1 and self.y[i] == 1):
                
                self.veri_positivi += 1
                
            if( self.classe_calcolata[i] == 0 and self.y[i] == 1):
                
                self.falsi_negativi += 1
                
            if( self.classe_calcolata[i] == 1 and self.y[i] == 0):
                
                self.falsi_positivi += 1
                
            
        self.accuratezza = (self.veri_positivi + self.veri_negativi) / ( self.veri_positivi + self.veri_negativi + self.falsi_negativi + self.falsi_positivi )
        self.richiamo =   self.veri_positivi  / ( self.veri_positivi + self.falsi_negativi  )
        self.precisione = self.veri_positivi  / ( self.veri_positivi  + self.falsi_positivi )
        print('accuratezza: ' + str(self.accuratezza))
        print('richiamo: ' + str(self.richiamo))
        print('precisione: ' + str(self.precisione))
        
        


    def print_valori_foglia(self):
        
        dict = {}
        
        for l in  range(floor(self.total_nodes/2)+1, self.total_nodes + 1, 1):
            
            temp = 0;
            
            for i in range(0, self.osservazioni, 1):
            
                if(self.nodo_foglia_calcolato[i] == l):
                    
                    temp += 1
            
            dict[l] = temp
                                    
        print(dict)
                
                    
                    
                    
                    
                    
                    
                    
                    
                    