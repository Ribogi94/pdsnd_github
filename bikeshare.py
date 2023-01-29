import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze and checks if input is valid for processing

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = None
    month = None
    day = None
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            input_city = str(input('Please enter the city name to analyse (Chicago, New York City, Washington): ')).lower()
            #check if input is valid for available cities
            if input_city == 'chicago' or input_city == 'new york city' or input_city == 'washington':
                city = input_city
                break
            else:
                #input was not valid
                print('Please check the city you entered. Invalid Input! Try again!')
        except ValueError:
            print('Please check the city you entered. Invalid Input! Try again!')
        except KeyboardInterrupt:
            print('No input taken. Try again!')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            input_month = str(input('Please enter the month to analyse (all, january, february, ... , june): ')).lower()
            #check if input is valid for month
            if input_month == 'all' or input_month == 'january' or input_month == 'february' or input_month == 'march' or input_month == 'april' or input_month == 'may' or input_month == 'june':
                month = input_month
                break
            else:
                #input was not valid
                print('Please check the month you entered. Invalid Input! Try again!')
        except ValueError:
            print('Please check the month you entered. Invalid Input! Try again!')
        except KeyboardInterrupt:
            print('No input taken. Try again!')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            input_day = str(input('Please enter the day to analyse (all, monday, tuesday, ... sunday): ')).lower()
            #check if input is valid for day
            if input_day == 'all' or input_day == 'monday' or input_day == 'tuesday' or input_day == 'wednesday' or input_day == 'thursday' or input_day == 'friday' or input_day == 'saturday' or input_day == 'sunday':
                day = input_day
                break
            else:
                #input was not valid
                print('Please check the day you entered. Invalid Input! Try again!')
        except ValueError:
            print('Please check the day you entered. Invalid Input! Try again!')
        except KeyboardInterrupt:
            print('No input taken. Try again!')

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['month'] = df['Start Time'].dt.month
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['day_of_week']==days.index(day)]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (DataFrame) df - filtered bikeshare DataFrame provided for analysis
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df.groupby(['month']).size().idxmax()
    print(f'\nThe most common month is {calendar.month_name[popular_month]}.')
    # display the most common day of week
    popular_dayofweek = df.groupby(['day_of_week']).size().idxmax()
    print(f'\nThe most common day of week is {calendar.day_name[popular_dayofweek]}.')
    # display the most common start hour
    popular_starthour = df.groupby(['hour']).size().idxmax()
    print(f'\nThe most common start hour is {popular_starthour} o clock.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        (DataFrame) df - filtered bikeshare DataFrame provided for analysis
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df.groupby(['Start Station']).size().idxmax()
    print(f'\nThe most commonly used start station is {popular_start}.')
    # display most commonly used end station
    popular_end = df.groupby(['End Station']).size().idxmax()
    print(f'\nThe most commonly used end station is {popular_end}.')
    # display most frequent combination of start station and end station trip
    popular_start_end = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'\nThe most commonly combination of start and end station is {popular_start_end}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (DataFrame) df - filtered bikeshare DataFrame provided for analysis
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'\nTotal travel duration of all people is {total_travel_time} seconds')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'\nMean travel duration of people is {mean_travel_time} seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    Args:
        (DataFrame) df - filtered bikeshare DataFrame provided for analysis
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts(dropna=False)
    print(f'\nCounts of user types: \n{user_types}\n')

    #Check if Gender is available(not washington)
    if 'Gender' in df:
    # Display counts of gender
        gender = df['Gender'].value_counts(dropna=False)
        print(f'\nCounts of users gender: \n{gender}\n')
    else:
        #case of washington with no data
        print(f'\nCity has no gender information available!\n')

    #Check if birth year is available(not washington)
    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth
        #earliest year of birth
        year_earl = np.nanmin(df['Birth Year'])
        print(f'\nMost earliest year of birth: {int(year_earl)}')
        #most recent year of birth
        year_recent = np.nanmax(df['Birth Year'])
        print(f'\nMost recent year of birth: {int(year_recent)}')
        #most common year of birth
        year_common = df['Birth Year'].value_counts(dropna=True).idxmax()
        print(f'\nMost common year of birth: {int(year_common)}')
    else:
        #case of washington with no data
        print(f'\nCity has no birth year information available!\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_view(df):
    """
    Displays raw data if user wants it. The user gets asked if he wants to see
    the foundation of the provided statistic analysis via input. Invalid input
    gets handled accordingly without crashing the application.

    Args:
        (DataFrame) df - provided filtered DataFrame for analysis
    """
    Looper = True
    while Looper:
        input_raw = str(input('Would you like to see the data used for this statistics (yes/no)?')).lower()
        i=0
        try:
            #check if input is yes - person wants to see data
            if input_raw == 'yes':
                #write first 5 lines of dataframe
                if len(df.index) > 4:
                    print(df.iloc[i:i+5])
                    i+=5
                #if less then 5 lines are in dataframe
                else:
                    print(df.iloc[i:len(df.index)])
                    print('No more raw data available!')
                    break
                #ask if more should be shown
                while Looper:
                    try:
                        input_more = str(input('You want more (yes/no)?')).lower()
                        if input_more == 'yes':
                            #when index of df is not reached
                            if i+5 < len(df.index):
                                print(df.iloc[i:i+5])
                                i+=5
                            #when index of df is reached output the last lines
                            else:
                                print(df.iloc[i:len(df.index)])
                                print('No more raw data available!')
                                #not to enter 1.layer of loop again
                                Looper = False
                                break
                        #no more output is wanted
                        else:
                            print('You are trusting the statistics and you do not want to see more raw data. Thank you!')
                            #not to enter 1.layer of loop again
                            Looper = False
                            break
                    except ValueError:
                            print('Please check what you entered. Invalid Input! Try again!')
                    except KeyboardInterrupt:
                            print('No input taken. Try again!')
            #input was somthing != yes
            else:
                print('You are trusting the statistics and you do not want to see the raw data. Thank you!')
                break
        except ValueError:
            print('Please check what you entered. Invalid Input! Try again!')
        except KeyboardInterrupt:
            print('No input taken. Try again!')

def main():
    """main function for calling all the single functions"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
