import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

"""
class PCAclass():
    
    def __init__(self):
        
        for i in range(0,50,1):
            
            self.dati = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione\\dati_allenamento\\osservazioni\\x" + str(i) + ".txt", delim_whitespace=True, header=None)
            
            self.file_out_componenti =open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione\\dati_allenamento\\componenti principali\\pc'+ str(i) +'.txt','w')
            self.file_out_varianza = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione\\dati_allenamento\\varianza componenti principali\\lambda'+ str(i) +'.txt','w')
            
            self.pca = PCA()
            self.pca.fit_transform(self.dati)
            
            self.componentiMatrice = np.transpose(self.pca.components_)
            
            for i in range(0,15,1):
                print(*self.componentiMatrice[i], file = self.file_out_componenti)
            
            print(*self.pca.explained_variance_ratio_, file = self.file_out_varianza)
            
            self.file_out_componenti.close()
            self.file_out_varianza.close()
            
"""       


class PCAclass():
    
    def __init__(self):
        
        for i in range(0,50,1):
            
            self.x = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione 2\\dati_allenamento\\osservazioni\\x" + str(i) + ".txt", delim_whitespace=True, header=None)
            self.y = pd.read_csv("C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione 2\\dati_allenamento\\classi\\y" + str(i) + ".txt", delim_whitespace=True, header=None)
            
            
            self.file_out_componenti_classe1 =open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione 2\\dati_allenamento\\componenti principali\\pc_classe1_'+ str(i) +'.txt','w')
            self.file_out_componenti_classe0 =open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione 2\\dati_allenamento\\componenti principali\\pc_classe0_'+ str(i) +'.txt','w')
            
            self.file_out_varianza_classe1 = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione 2\\dati_allenamento\\varianza componenti principali\\lambda_classe1_'+ str(i) +'.txt','w')
            self.file_out_varianza_classe0 = open('C:\\Users\\UTENTE\\OneDrive\\Tesi Magistrale Riccardo Allegri\\tesi magistrale modello\\multivariato\\modello robusto\\multivariato\\distributionally robust\\modello senza normalizazione 2\\dati_allenamento\\varianza componenti principali\\lambda_classe0_'+ str(i) +'.txt','w')
            
            self.x_classe_1 = pd.DataFrame()
            self.x_classe_0 = pd.DataFrame()
            
            for k in range(0,147,1):
                
                if(self.y.iloc[k,0] == 1):
                    
                    self.x_classe_1 = self.x_classe_1.append(self.x.iloc[k])
                    
                else:
                    
                    self.x_classe_0 = self.x_classe_0.append(self.x.iloc[k])
            
            self.pca_classe1 = PCA()
            self.pca_classe1.fit_transform(self.x_classe_1)
            
            self.pca_classe0 = PCA()
            self.pca_classe0.fit_transform(self.x_classe_0)
            
            self.componentiMatrice_classe1 = np.transpose(self.pca_classe1.components_)
            self.componentiMatrice_classe0 = np.transpose(self.pca_classe0.components_)
            
            for i in range(0,15,1):
                print(*self.componentiMatrice_classe1[i], file = self.file_out_componenti_classe1)
                print(*self.componentiMatrice_classe0[i], file = self.file_out_componenti_classe0)
            
            print(*self.pca_classe1.explained_variance_ratio_, file = self.file_out_varianza_classe1)
            print(*self.pca_classe0.explained_variance_ratio_, file = self.file_out_varianza_classe0)
            
            self.file_out_componenti_classe1.close()
            self.file_out_componenti_classe0.close()
            self.file_out_varianza_classe1.close()
            self.file_out_varianza_classe0.close()
            
             