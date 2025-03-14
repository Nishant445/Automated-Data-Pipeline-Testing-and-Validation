import pytest
import pandas as pd
from pipeline import load_data, clean_data

# load the sample test data
@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "order_id": [1,2,3,4,5],
        "customer_name":["Alice", "Bob" , "Charlie", None, "Eve"], #One missing value
        "amount":[100,200,300,400,None] #One missing value


    })

# Test if data is loading correctly

def test_load_data():
    df = load_data("data/orders.csv")
    assert not df.empty, "Data should not be empty!"

# Test if missing values are removed

def test_clean_data(sample_data):
    df_clean = clean_data(sample_data)
    assert df_clean.isnull().sum().sum()  ==0, "There should be no missing value"