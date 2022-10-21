import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city do you want to analyze data for?: ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("City not found, please enter either of the following chicago, new york city or washington: ").lower()
     

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month do you want to analyze data for?: ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input ("Month not found, please enter either january, february, march, april, may, june or all: ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day do you want to analyze data for?: ').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input ("Day not found, please try again: ").lower()
        


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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].mode()[0])


    # TO DO: display the most common day of week
    print("The most common day of the week is: ", df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ", df['hour'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])



    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])



    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is:")
    most_frequent_start_and_end_station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_frequent_start_and_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/60
    print("Total travel time in minutes is:", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('The mean travel time in minutes is:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types:\n', user_types)


    # TO DO: Display counts of gender
    try:
     gender = df['Gender'].value_counts()
     print('The counts of gender:\n', gender)
    except KeyError:
     print("No data available for this month.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year = df['Birth Year'].min()
      print('The earliest year is:', earliest_year)
    except KeyError:
      print("No data is found.")

    try:
      most_recent_year = df['Birth Year'].max()
      print('The most recent year is:', most_recent_year)
    except KeyError:
      print("No data is found.")

    try:
      most_common_year = df['Birth Year'].mode()[0]
      print('The most common year is:', most_common_year)
    except KeyError:
      print("No data is found.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data != 'yes':
           print(df.iloc[start_loc:start_loc+5])
        
        start_loc += 5
        while True:
            view_data = input("Would you like to see the next 5 rows?: Enter yes or no ").lower()
            if view_data != 'yes':
                return
            print(df.iloc[start_loc:start_loc+5])
        
    
            
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
#WEBSITES USED ARE:
#UDACITY classroom and suggested websites for more detailed information 
#https://www.geeksforgeeks.org/python-pandas-series-dt-hour/#:~:text=dt%20can%20be%20used%20to,of%20the%20given%20series%20object.
#https://www.statology.org/idxmax-pandas/
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html
#https://stackoverflow.com/questions/63229237/finding-the-most-frequent-combination-in-dataframe
#I used mostly stackoverflow and geeksforgeeks 
