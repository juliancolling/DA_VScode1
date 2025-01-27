# DataSummary - receive a dataframe and perform several common analyses on it and return dataframe of the results.
def DataSummary(dfTest):

    NonObject = dfTest.select_dtypes(exclude=['object', 'string', 'datetime64']).columns
    summary_df = pd.DataFrame({
        'DataType': dfTest.dtypes,
        'UniqueValues': dfTest.nunique(),
        'RowsWithData': len(dfTest)-dfTest.isnull().sum(),
        'NullValues':dfTest.isnull().sum(),
        'SkewScore':dfTest[NonObject].skew(),
        'Kurtosis':dfTest[NonObject].kurtosis()
    }).reset_index().rename(columns={'index': 'Column'})
    return summary_df


# Call using DataSummary([DATAFRAMENAME])
# print(DataSummary(df))