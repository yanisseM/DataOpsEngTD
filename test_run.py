"""
Tests
"""
from run import import_data, rename_columns,data_sample

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


def test_data_sample():
    """
    Test de la fonction d'échantillon
    """
    data = import_data()
    echantillon = data_sample(data)
    assert len(echantillon) == 50, f"La taille de l'échantillon devrait être 50, mais elle est {len(echantillon)}."
    print("Les tests ont réussi avec succès.")

