import pandas as pd
import pytest
from unittest.mock import patch
from life_expectancy.loading_saving import save_cleaned_data

def test_save_cleaned_data():
    # Criar um DataFrame de exemplo para salvar
    fake_df = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': ['A', 'B', 'C'],
    })
    # Patch pd.DataFrame.to_csv
    with patch.object(fake_df, 'to_csv') as mock_to_csv:
        # Chamar a função que está a ser testada
        save_cleaned_data(fake_df, "fake_path.csv", ',')

        # Assert
        mock_to_csv.assert_called_once_with("fake_path.csv", index=False, sep=',')

        print("Teste 'save_cleaned_data' está OK!")

if __name__ == "__main__":
    pytest.main([__file__])