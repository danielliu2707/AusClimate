import pandas as pd

def update_suburbs(df:pd.DataFrame) -> pd.DataFrame:
    """
    This function updates a pandas dataframe with suburb and state attributes
    to set suburbs that border multiple states to be one particular state and 
    removes suburbs in other Australian territories.

    Args:
        df (pd.DataFrame): A dataframe with suburb and state attributes.

    Returns:
        pd.DataFrame: A dataframe with the above updates applied.
    """
    # Define a mapping to group the states and territories
    mapping = {
        'Queensland': 'Queensland',
        'New South Wales': 'New South Wales',
        'Western Australia': 'Western Australia',
        'South Australia': 'South Australia',
        'Victoria': 'Victoria',
        'Northern Territory': 'Northern Territory',
        'Tasmania': 'Tasmania',
        'New South Wales,Queensland': 'New South Wales',
        'New South Wales,Victoria': 'New South Wales',
        'Northern Territory,Western Australia': 'Western Australia',
        'Northern Territory,Queensland': 'Queensland',
        'New South Wales,South Australia': 'New South Wales',
        'Australian Capital Territory': 'Australian Capital Territory',
        'South Australia,Victoria': 'South Australia',
        'Northern Territory,South Australia,Western Australia': 'South Australia',
        'South Australia,Western Australia': 'South Australia',
        'Other Territories': 'Other Territories'
    }
    
    # Apply the mapping
    df['officialnamestate'] = df['officialnamestate'].map(mapping)

    # Set Mungindi to Queensland:
    condition = df['officialnamesuburb'] == 'Mungindi (Qld)'
    df.loc[condition, 'officialnamestate'] = 'Queensland'

    # Set Lake Mackay to Northern Territory:
    condition = df['officialnamesuburb'] == 'Lake Mackay'
    df.loc[condition, 'officialnamestate'] = 'Northern Territory'

    # Drop other terriorities outside of main Australian land mass:
    df = df[(df['officialnamestate'] != "Other Territories") & (df['officialnamesuburb'] != "Lord Howe Island")]
    
    return df