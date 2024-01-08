from pathlib import Path
import pandas as pd
import pytest
from life_expectancy.loading_saving import TsvFileStrategy, JsonFileStrategy

def test_tsv_file_strategy():
    strategy = TsvFileStrategy()
    result = strategy.read(Path(__file__).parents[1] / "data" / "eu_life_expectancy_raw.tsv")

    # Verificar se o resultado é o esperado
    assert isinstance(result, pd.DataFrame), "A função deve retornar um DataFrame"
    assert len(result) > 0, "O DataFrame resultante não deve estar vazio"

    print("Teste 'TsvFileStrategy' passou!")

def test_json_file_strategy():
    strategy = JsonFileStrategy()
    result = strategy.read(Path(__file__).parents[1] / "data" / "eurostat_life_expect.json")

    # Verificar se o resultado é o esperado
    assert isinstance(result, pd.DataFrame), "A função deve retornar um DataFrame"
    assert len(result) > 0, "O DataFrame resultante não deve estar vazio"

    print("Teste 'JsonFileStrategy' passou!")

if __name__ == "__main__":
    pytest.main([__file__])
