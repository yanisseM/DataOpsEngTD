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
    # Création d'un DataFrame fictif pour les tests
    data = import_data()

    # Appel de la fonction
    echantillon = data_sample(data)

    # Vérification que la taille de l'échantillon est correcte
    assert len(echantillon) == 50, f"La taille de l'échantillon devrait être 50, mais elle est {len(echantillon)}."

    # Vérification que les colonnes sont les mêmes
    assert all(colonne in echantillon.columns for colonne in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'variety']), "Les colonnes ne sont pas correctes."

    print("Les tests ont réussi avec succès.")

# Appel de la fonction de test
test_data_sample()

