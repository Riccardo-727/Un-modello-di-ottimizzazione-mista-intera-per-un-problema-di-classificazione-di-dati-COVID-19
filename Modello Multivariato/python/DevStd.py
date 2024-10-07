import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

"""
class DevStd():
    
    def __init__(self):
        
        for i in range(0,30,1):
            
            self.dati = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=5\\dati_allenamento\\osservazioni normalizzate\\x" + str(i) + ".txt", delim_whitespace=True, header=None)
            
            self.file_out_deviazione_standard = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\\modello con normalizzazione min-max\\cross-validation k=5\\dati_allenamento\\deviazione standard\\std_'+ str(i) +'.txt','w')
            
            self.deviazione_standard_vettore = np.std(self.dati, ddof=1)
            
            print( *self.deviazione_standard_vettore, file = self.file_out_deviazione_standard)
            
        self.file_out_deviazione_standard.close()
        
"""

class DevStd():
    
    def __init__(self):
        
        for i in range(0,50,1):
            
            #self.x = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=3\\dati_allenamento\\osservazioni normalizzate\\x" + str(i) + ".txt", delim_whitespace=True, header=None)
            
            self.x = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\ellipsoidal robust\\modello senza normalizazione\\dati non normalizzati\\dati_allenamento\\osservazioni\\x" + str(i) + ".txt", delim_whitespace=True, header=None)
            
            self.y = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\ellipsoidal robust\\modello senza normalizazione\\dati non normalizzati\\dati_allenamento\\classi\\y" + str(i) + ".txt", delim_whitespace=True, header=None)
            
            self.file_out_deviazione_standard_classe_1 = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione 2\\dati_allenamento\\deviazione standard\\std_x_classe1_'+ str(i) +'.txt','w')
            
            self.file_out_deviazione_standard_classe_0 = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione 2\\dati_allenamento\\deviazione standard\\std_x_classe0_'+ str(i) +'.txt','w')
            
            self.x_classe_1 = pd.DataFrame()
            
            self.x_classe_0 = pd.DataFrame()
            
           
            for k in range(0,147,1):
                
                if(self.y.iloc[k,0] == 1):
                    
                    self.x_classe_1 = self.x_classe_1.append(self.x.iloc[k])
                    
                else:
                    
                    self.x_classe_0 = self.x_classe_0.append(self.x.iloc[k])
            
            
            self.std_classe1 = np.std(self.x_classe_1, ddof=1)
            
            self.std_classe0 = np.std(self.x_classe_0, ddof=1)
            
            print( *self.std_classe1, file = self.file_out_deviazione_standard_classe_1)
            
            print( *self.std_classe0, file = self.file_out_deviazione_standard_classe_0)
            
            self.file_out_deviazione_standard_classe_1.close()
            
            self.file_out_deviazione_standard_classe_0.close()
    
    