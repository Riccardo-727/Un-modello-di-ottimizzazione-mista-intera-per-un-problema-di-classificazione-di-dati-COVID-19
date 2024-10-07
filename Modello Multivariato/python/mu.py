import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

class Mu():
    
    def __init__(self):
        
        for i in range(0,30,1):
            
            self.dati = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione mu-std\\dati_allenamento\\osservazioni\\x" + str(i) + ".txt", delim_whitespace=True, header=None)
            
            self.file_out_mu = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\\modello con normalizzazione mu-std\\dati_allenamento\\media\\mu_'+ str(i) +'.txt','w')
            
            self.mu_vettore = np.mean(self.dati)
            
            print( *self.mu_vettore, file = self.file_out_mu)
            
        self.file_out_mu.close()
        
  
    """
    def __init__(self):
        
        self.dati = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione mu-std\\cross-validation con k=5\\x.txt", delim_whitespace=True, header=None)
        
        self.file_out_mu = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\\modello con normalizzazione mu-std\\mu.txt','w')
        
        self.file_out_std = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\\modello con normalizzazione mu-std\\std.txt','w')
        
        self.mu_vettore = np.mean(self.dati)
        
        self.std_vettore = np.std(self.dati)
        
        print( *self.mu_vettore, file = self.file_out_mu)
        
        print( *self.std_vettore, file = self.file_out_std)
        
        self.file_out_mu.close()
        
        self.file_out_std.close()
        
        """
        