from numpy import arange
from pandas import Series


def find_cohort_period(dataframe, column_name="cohort_period"):

    dataframe[column_name] = arange(len(dataframe)) + 1
    
    return dataframe


def add_cohort_period_colum(dataframe, column_name="cohort_period"):
    
    dataframe = dataframe.groupby(level=0).apply(find_cohort_period)

    return dataframe


def add_cohort_group_column(dataframe, user_id_column, date_column, cohort_group_column):

    dataframe.set_index(user_id_column, inplace=True)

    dataframe[cohort_group_column] = dataframe.groupby(level=0)[date_column].min()
    dataframe.reset_index(inplace=True)

    return dataframe


def build_cohort_dataframe(dataframe, user_id_column, cohort_group_column, date_column):

    grouped = dataframe.groupby([cohort_group_column, date_column])

    cohorts = grouped.agg({user_id_column: Series.nunique})

    new_column_name = "total_" + user_id_column

    cohorts.rename(columns={user_id_column: new_column_name}, inplace=True)

    return cohorts


def build_cohort_matrix(dataframe, cohort_group_column, cohort_period_column, total_user_column):

    dataframe.reset_index(inplace=True)
    dataframe.set_index([cohort_group_column, cohort_period_column], inplace=True)

    cohort_group_size = dataframe[total_user_column].groupby(level=0).first()

    cohort_matrix = dataframe[total_user_column].unstack(0).divide(cohort_group_size, axis=1)

    return cohort_matrix.T
