from smiles import smiles


def test_smile():
    assert smiles.smile() == ":)"
