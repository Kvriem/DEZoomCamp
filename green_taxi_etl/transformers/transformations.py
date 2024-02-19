if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import datetime
import pandas as pd

def camel_to_snake(column_name):
    snake_case_name = ''.join(['_'+c.lower() if c.isupper() else c for c in column_name]).lstrip('_')
    return snake_case_name

@transformer
def transform(data, *args, **kwargs):
 
    #Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
    indices_to_delete = data[ data['passenger_count'] == 0].index.tolist()
    indices_to_delete.extend(data[data['trip_distance']==0].index.tolist())
    data.drop(indices_to_delete,inplace=True)
    
    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    data['lpep_pickup_date']=pd.to_datetime(data['lpep_pickup_datetime']).dt.date

    #Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    data.columns = [camel_to_snake(col) for col in data.columns]

    return data


@test
def test_output(output, *args) -> None:

    assert (output['passenger_count'] > 0).any() , 'The passenger count is zero'
    assert (output['trip_distance'] > 0).any(), 'The trip distance is zero'