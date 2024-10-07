import numpy as np
import pandas as pd

class File():
    
    
    def __init__(self):
        
        for i in range(0,30,1):
            
            #osservazioni
            self.file_in_X = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=5\\x.txt','r').readlines()
            self.file_out_X_allenamento = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=5\\dati_allenamento\\osservazioni\\x'+ str(i) +'.txt','w')
            self.file_out_X_validazione = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=5\\dati_validazione\\osservazioni\\x'+str(i) +'.txt','w')
            
            
            #classi
            self.file_in_Y = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=5\\y.txt','r').readlines()
            self.file_out_Y_allenamento = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=5\\dati_allenamento\\classi\\y'+ str(i) +'.txt','w')
            self.file_out_Y_validazione = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=5\\dati_validazione\\classi\\y'+ str(i) +'.txt','w')


            for j in range(0,150,1):
                
                if(j != i*3 and j != i*3+1 and j != i*3+2 and j != i*3+3 and j != i*3+4): 
                    
                    self.file_out_X_allenamento.writelines(self.file_in_X[j])
                    self.file_out_Y_allenamento.writelines(self.file_in_Y[j])
                
                else:
                    self.file_out_X_validazione.writelines(self.file_in_X[j])
                    self.file_out_Y_validazione.writelines(self.file_in_Y[j])
         
            
            #self.file_in_X.close()
            self.file_out_X_allenamento.close()
            self.file_out_X_validazione.close()
            #self.file_in_Y.close()
            self.file_out_Y_allenamento.close()
            self.file_out_Y_validazione.close()
       
         
      
    """
    def __init__(self):
        
        
        self.dati = pd.read_csv('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\150 dati\\x.txt', delim_whitespace=True, header=None)
        
        self.max = np.max(self.dati)
        
        self.min = np.min(self.dati)
        
        for k in range(0,150,1):
            for kk in range(0,15,1):
                self.dati.loc[k,kk] = (self.dati.loc[k,kk] - self.min[kk]) / ( self.max[kk] - self.min[kk])
        
        
        for i in range(0,30,1):
            
            self.file_out = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\box robust\\modello con normalizzazione min-max\\cross-validation k=5\\dati_allenamento\\osservazioni normalizzate\\x' + str(i) +'.txt', 'w')
            

            for j in range(0,150,1):
                
                if(j != i*3 and j != i*3+1 and j != i*3+2 and j != i*3+3 and j != i*3+4):
                    
                    print( *self.dati.loc[j,:], file = self.file_out)
                    
                

        self.file_out.close()
        
       """
       
       
 