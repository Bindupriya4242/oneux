import pandas as pd
from test_pandas import rank_columns

def test_rank_columns():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 5, 4, 7],
        'B': [5, 3, 6, 4, 8],
        'C': [7, 8, 2, 3, 1]
    }
    index = ['D1', 'D2', 'A1', 'D3', 'B1']
    df = pd.DataFrame(data, index=index)

    # Call the function
    result = rank_columns(df)

    # Expected result DataFrame
    expected_data = {
        'A': [1.0, 2.0, 3.0],  # ranks within the filtered data
        'B': [3.0, 1.0, 2.0],  # corrected ranks for B
        'C': [2.0, 3.0, 1.0]
    }
    expected_index = ['D1', 'D2', 'D3']
    expected_df = pd.DataFrame(expected_data, index=expected_index)

    # Print outputs for debugging
    print("Result DataFrame:")
    print(result)
    print("\nExpected DataFrame:")
    print(expected_df)

    # Assert that the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result, expected_df)
