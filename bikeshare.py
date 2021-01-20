import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

monthes_names = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "all",
]

days_names = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
    'all',
]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # initialaize the variables that will contain user input
    city = ""
    month = ""
    day = ""
    would_you_analyze = ""
    filter_by_month_or_day = ""
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    # while city name is not exists in CITY_DATA keys, then it is invalid input
    # check if user want to analyse data
    while would_you_analyze.lower() not in ['yes', 'no']:
        would_you_analyze = input('Would you like to see data for Chicago, New York, or Washington? (yes/no): ')

    # if no, then exist program.
    if(would_you_analyze == 'no'):
        exit()

    while city.lower() not in CITY_DATA.keys():
        print('Available cities: ')
        # print the existing cities that user can enter
        for c in CITY_DATA.keys():
            print(c)
        # take the input from user
        city = input("Please Enter city's name to analayze: ")
        # check if input is invalid then print descriptive message
        if(city not in CITY_DATA.keys()):
            print("Invalid city name, please try again. \n\n")



    # TO DO: get user input for month (all, january, february, ... , june)
    # check if user wants to filter by month , if not, set default value to 'all'
    while filter_by_month_or_day.lower() not in ['month', 'day', 'no']:
        filter_by_month_or_day = input('Would you like to filter the data by month, day, or not at all? (month/day/no): ')

    if filter_by_month_or_day != 'month':
        month = 'all'
    if filter_by_month_or_day != 'day':
        day = 'all'
    # while month name is not exists in monthes_names, then it is invalid input
    while month.lower() not in monthes_names and filter_by_month_or_day == 'month':
        print('\nWhich month ?:\n')
        # print the existing monthes that user can enter
        for c in monthes_names:
            print(c)
        # take the input from user
        month = input("Please Enter month's name that you will filter by it: ")
        # check if input is invalid, then print descriptive message
        if(month not in monthes_names):
            print("Invalid month name, please try again. \n\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    # while day name is not exists in days_names , then it is invalid input
    while day.lower() not in days_names and filter_by_month_or_day == 'day':
        print('\nWhich day ?:\n')
        # print the existing days that user can enter
        for c in days_names:
            print(c)
        # take the input from user
        day = input("Please Enter day's name that you will filter by it: ")
        # check if input is invalid, then print descriptive message
        if(day not in days_names):
            print("Invalid day name, please try again. \n\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    # we need to convert start time to datetime first,
    # then we can get the monthes, days, hour
    # then we can filter by month, day, hour

    # https://www.interviewqs.com/ddi_code_snippets/extract_month_year_pandas
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # create new columns , month, day, and hour
    # we can get them from 'Start time' column
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    # now we can filter the rows by passed paramters
    # first, by month name
    if month != 'all':
        df = df[df.month == monthes_names.index(month) + 1]
    # and then for day
    if day != 'all':
        df = df[df.day == days_names.index(day) + 1]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # value counts return a series containing counts of unique values
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html

    # idxmax return the row label of the maximum value.
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.idxmax.html

    # mc : is a shortcut for most common

    # TO DO: display the most common month
    mc_month = df.month.value_counts().idxmax()
    print(f"Most common month is: {mc_month}")
    # TO DO: display the most common day of week
    mc_day = df.day.value_counts().idxmax()
    print(f"Most common day is: {mc_day}")
    # TO DO: display the most common start hour
    mc_hour = df.hour.value_counts().idxmax()
    print(f"Most common hour is: {mc_hour}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_start_station = df['Start Station'].value_counts().idxmax()
    print(f"Most common start-station is : {mc_start_station}.")

    # TO DO: display most commonly used end station
    mc_end_station = df['End Station'].value_counts().idxmax()
    print(f"Most common end-station is: {mc_end_station}.")

    # TO DO: display most frequent combination of start station and end station trip
    # group the start and end stations
    # then Compute group sizes.
    # get the largest repeated one
    # get the index that contain the stations names
    mc_comb_start_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1).index[0]
    print(f'Most common start and end stations are: ({mc_comb_start_end_stations[0]}) for start station and ({mc_comb_start_end_stations[1]}) for end station')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Total travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_type = df['User Type'].value_counts()
    for user_type, count in zip(counts_of_user_type.index, counts_of_user_type):
        print(user_type, '->', count)

    # TO DO: Display counts of gender
    if("Gender" in df.columns):
        counts_of_gender = df['Gender'].value_counts()
        for gender_type, count in zip(counts_of_gender.index, counts_of_gender):
            print(gender_type, '->', count)


    # TO DO: Display earliest, most recent, and most common year of birth
    # translate as coding:
    # earliest = oldest = minimum , ex: 1989 is oldest than 1995
    # recent = newest = maximum , ex: 2010 is newset than 1995

    if("Birth Year" in df.columns):
        mc_birth_year = df['Birth Year'].value_counts().idxmax()
        recent_birth_year = df['Birth Year'].max()
        earliest_birth_year = df['Birth Year'].min()
        # display them
        print(f"The earliest birth year is: {earliest_birth_year}")
        print(f"The recent birth year is: {recent_birth_year}")
        print(f"The most common birth year is: {mc_birth_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # set the current index to display from,
        # 0 -> 5
        # 5 -> 10
        # 10 -> 15
        current_index = 0
        # keep asking user if he want to display rows until he say no
        while True:
            print_data = input("Would you like to print 5 rows of data? type y for yes ,n for no ): ")
            if print_data.lower() not in ['y', 'n']:
                print("\n\nPlease enter a valid choice, y or n.\n\n")
            if print_data.lower() == 'y':
                # loop on rows from index current_index to current_index + 5
                for (i, row) in df[current_index:current_index + 5].iterrows():
                    # loop on columns except the Unnamed: 0 column
                    for col_name in df.columns[1:]:
                        print(col_name, '->', row[col_name])
                    print('-' * 40)
                # update current index
                current_index += 5
                print(f"rows from {current_index} to {current_index + 5} successfully displayed.")
            elif print_data.lower() == 'n':
                break

        restart = input('\n Would you like to restart the process again? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
