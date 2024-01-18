import datetime

import pandas as pd

from pandas_datareader import data as pdr

import yfinance as yf

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

NOW = datetime.datetime.today().date()
YESTERDAY = NOW - datetime.timedelta(days=1)


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API.
    """
    # Activate pdr monkey-patch to use download directly to pandas dataframe
    yf.pdr_override() 

    # download dataframe using pandas_datareader
    data = pdr.get_data_yahoo("MSFT", start=YESTERDAY, end=str(NOW))

    return data.reset_index() 


@test
def test_output(data, *args) -> None:
    """
    Test output
    """
    assert isinstance(data, pd.DataFrame), 'The output is not a pandas dataframe.'
