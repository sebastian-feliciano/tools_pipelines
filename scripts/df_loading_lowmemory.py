import pandas as pd

# Load large CSV files with low memory usage
dtype_map = {
    "first_col" : "int16",
    "second_col" : "float16",
    "third_col" : "int16",
    "fourth_col" : "int16",
    "fifth_col" : "float16"
}

with pd.read_csv(
    "data_folder/data_file.csv",
    chunksize=10000,
    dtype=dtype_map
) as reader:
    
    for chunk in reader:
        process(chunk)
