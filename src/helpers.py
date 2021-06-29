"""
helper functions
"""

def aggregate_data_sources(data_source):
    """
    Function aggregates data_source vals into 'tmas' or 'toll' 
    values.
    """
    
    if "TMAS" in data_source:
        agg_source = 'tmas'
        
    elif "Tolls" in data_source:
        agg_source = 'toll'
        
    return agg_source  
    
def assign_volume_range_wide(aadt):
    """
    Function maps continuous aadt values to discrete "wide" bins
    (4 total) and returns bins label.
    """
    
    assert isinstance(aadt, (int, float)), "aadt is non-numeric"
    assert aadt >= 0, "aadt is negative"
    
    if aadt < 500:
        aadt_lbl = '<500 \n(very low)'
    elif 500 <= aadt < 5000:
        aadt_lbl = '500-\n4,999 \n(low)'
    elif 5000 <= aadt < 55000:
        aadt_lbl = '5,000-\n54,999 \n(med)'
    elif aadt >= 55000:
        aadt_lbl = '55,000+ \n(high)'
        
    return aadt_lbl

def assign_volume_range_narrow(aadt):
    """
    Function maps continuous aadt values to discrete "narrow" bins
    (10 total) and returns bins label.
    """
    
    assert isinstance(aadt, (int, float)), "aadt is non-numeric"
    assert aadt >= 0, "aadt is negative"
    
    if aadt < 500:
        aadt_lbl = '<500'
    elif 500 <= aadt < 2000:
        aadt_lbl = '500-\n1,999'
    elif 2000 <= aadt < 5000:
        aadt_lbl = '2,000-\n4,999'
    elif 5000 <= aadt < 10000:
        aadt_lbl = '5,000-\n9,999'
    elif 10000 <= aadt < 20000:
        aadt_lbl = '10,000-\n19,999'
    elif 20000 <= aadt < 35000:
        aadt_lbl = '20,000-\n34,999'
    elif 35000 <= aadt < 55000:
        aadt_lbl = '35,000-\n54,999'
    elif 55000 <= aadt < 85000:
        aadt_lbl = '55,000-\n84,999'
    elif 85000 <= aadt < 125000:
        aadt_lbl = '85,000-\n124,999'
    elif aadt >= 125000:
        aadt_lbl = '125,000+'
        
    return aadt_lbl

def create_state_color_palette(aadt_valid_df):
    state_comparisons_df = aadt_valid_df['state'].value_counts().reset_index()
    state_comparisons_df.rename(columns={'state': 'n',
                                         'index': 'state'}, inplace=True)
    
    return state_comparisons_df