import json
import pandas as pd


# Lecture des données compris dans identifiants.csv
class get_csv:
    def __init__(self):
        super().__init__()
        # identifiantDf = pd.read_csv(csv_file)
        
    def get_data(self, path):
        return pd.read_csv(path)
    
    
if __name__ == '__main__':
    csv_file = "/home/lepas/Documents/passwordManager/src/main/resources/base/save/identifiants.csv"
    A = get_csv()
    id_df = A.get_data(csv_file)
    