from pathlib import Path
import pandas as pd
import pytest
from life_expectancy.loading_saving import load_dataset

def test_load_dataset():
    result = load_dataset(Path(__file__).parents[1] / "data" / "eu_life_expectancy_raw.tsv", '\t')

    # Verificar se o resultado é o esperado
    assert isinstance(result, pd.DataFrame), "A função deve retornar um DataFrame"
    assert len(result) > 0, "O DataFrame resultante não deve estar vazio"

    print("Teste 'load_dataset' contém um daframe com dados!")

if __name__ == "__main__":
    pytest.main([__file__])
