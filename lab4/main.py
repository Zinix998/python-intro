import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.weights import entropy_weights
from pymcdm.helpers import rankdata
from pymcdm import normalizations

def main():

    alternatives = ["Samsung S23", "iPhone 15", "Xiaomi 14", "Google Pixel 8"]
    

    matrix = np.array([
        [3900, 8,  3900, 168], # Samsung
        [4500, 6,  3349, 171], # iPhone
        [3200, 12, 4610, 193], # Xiaomi
        [3500, 8,  4575, 187]  # Pixel
    ])
    

    types = np.array([-1, 1, 1, -1])

    criteria_names = ["Cena", "RAM", "Bateria", "Waga"]

    print("--- 1. Macierz decyzyjna ---")
    df_data = pd.DataFrame(matrix, index=alternatives, columns=criteria_names)
    print(df_data)
    print("\n")


    weights = entropy_weights(matrix)
    print("--- 2. Wagi kryteriów (Entropia) ---")
    for name, w in zip(criteria_names, weights):
        print(f"{name}: {w:.4f}")
    print("\n")


    topsis = TOPSIS(normalizations.minmax_normalization)
    pref_topsis = topsis(matrix, weights, types)
    rank_topsis = rankdata(pref_topsis, reverse=True) # Im większa preferencja, tym lepiej


    bounds = np.vstack((
        np.min(matrix, axis=0),
        np.max(matrix, axis=0)
    )).T
    
    spotis = SPOTIS(bounds)
    pref_spotis = spotis(matrix, weights, types)
    rank_spotis = rankdata(pref_spotis, reverse=False) 

    # --- 5. WYNIKI I PORÓWNANIE ---
    df_results = pd.DataFrame({
        'TOPSIS Pref': pref_topsis,
        'TOPSIS Rank': rank_topsis,
        'SPOTIS Pref': pref_spotis,
        'SPOTIS Rank': rank_spotis
    }, index=alternatives)
    
    print("--- 3. Wyniki końcowe ---")
    print(df_results.sort_values(by="TOPSIS Rank"))
    


if __name__ == "__main__":
    main()