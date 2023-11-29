"""
Tests
"""
from run import import_data, rename_columns

def test_import_data():
    """
    Test
    """
    data = import_data()
    assert data.shape[0] > 0


def test_rename_columns():
    """
    Doc
    """
    data = import_data()
    data_renamed = rename_columns(data)
    assert "sepal_length" in data_renamed.columns

import pandas as pd

def test_data_sample():
    """
    Test de la fonction d'échantillon
    """
    data = import_data()
    echantillon = data_sample(data)
    assert len(echantillon) == 50, f"La taille de l'échantillon devrait être 50, mais elle est {len(echantillon)}."
    assert all(colonne in echantillon.columns for colonne in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'variety']), "Les colonnes ne sont pas correctes."

    print("Les tests ont réussi avec succès.")

# Appel de la fonction de test
test_data_sample()

