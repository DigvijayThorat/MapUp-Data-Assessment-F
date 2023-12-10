import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
import pandas as pd

def generate_car_matrix(dataset_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(dataset_path)

    # Create a pivot table with id_1 as index, id_2 as columns, and car as values
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    for idx in car_matrix.index:
        car_matrix.loc[idx, idx] = 0

    return car_matrix
    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
import pandas as pd

def get_type_count(dataset_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(dataset_path)

    # Define a function to categorize car values
    def categorize_car(value):
        if value <= 15:
            return 'low'
        elif 15 < value <= 25:
            return 'medium'
        else:
            return 'high'

    # Add a new column 'car_type' based on 'car' values
    df['car_type'] = df['car'].apply(categorize_car)

    # Calculate the count of occurrences for each car_type category
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    type_counts = dict(sorted(type_counts.items()))

    return type_counts
    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
import pandas as pd

def get_bus_indexes(dataset_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(dataset_path)

    # Calculate the mean value of the 'bus' column
    mean_bus_value = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes
    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
import pandas as pd

def filter_routes(dataset_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(dataset_path)

    # Calculate the average value of the 'truck' column for each route
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average truck value is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    selected_routes.sort()

    return selected_routes
    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
import pandas as pd

def multiply_matrix(input_matrix):
    # Create a copy of the input DataFrame to avoid modifying the original
    modified_matrix = input_matrix.copy()

    # Apply the multiplication logic
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix
    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
import pandas as pd
from datetime import datetime, timedelta

def check_time_completeness(df):
    # Convert timestamp columns to datetime objects
    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    # Define a function to check if the time range is complete
    def is_time_complete(group):
        min_datetime = group['start_datetime'].min()
        max_datetime = group['end_datetime'].max()
        expected_min_datetime = datetime.combine(min_datetime.date(), datetime.min.time())
        expected_max_datetime = datetime.combine(max_datetime.date(), datetime.max.time()) - timedelta(microseconds=1)
        return (min_datetime == expected_min_datetime) and (max_datetime == expected_max_datetime)

    # Apply the function to each group of (id, id_2) pairs
    completeness_series = df.groupby(['id', 'id_2']).apply(is_time_complete)

    return completeness_series
    return pd.Series()
