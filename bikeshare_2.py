import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# These Two Arrays is act as lookups for dataframe filter 
months = ["all","january", "february","march","april","may","june"]
days = ['all','sunday', 'saturday','monday','tuesday','wednesday','thursday','friday']

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter One City (Chicago - New york city - Washington): ")
    while city.lower() not in CITY_DATA:
        city = input("\nInvalid Input , Enter One Of Listed Cities ('chicago' , 'new york city' , 'washington'): ")


    # get user input for month (all, january, february, ... , june)
    month = input("Enter Month ('all','january','february','march','april','may','june'): ")
    while month.lower() not in months:
        month = input("\nInvalid Input , Enter One Of Listed Months ('all','january', 'february','march','april','may','june'): ")    


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Pick Day Of Week To Filter ('all','sunday', 'saturday','monday','tuesday','wednesday','thursday','friday') : ")
    while day.lower() not in days:
     day = input("\nInvalid Input , Enter One Of Listed days ('all','sunday', 'saturday','monday','tuesday','wednesday','thursday','friday'): ")

    # To Make Things Clear And Easy
    city = city.lower()
    month = month.lower()
    day = day.lower()

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
    data = pd.read_csv(CITY_DATA[city])
    df = pd.DataFrame(data)

    #Change dates to make them same data type to be able to filter 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])


    #get month from start time column into new column as names of months
    df['month'] = df['Start Time'].dt.strftime('%B').str.lower()


    #get day from start time column into new column as names of days lower for easy filter
    df['day'] = df['Start Time'].dt.day_name().str.lower()


    if month != 'all':
        df = df[df['month'] == month ]


    if day != 'all':
        df = df[df['day'] == day ]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print(f"The most common month is: {most_common_month}")

    # display the most common day of week
    most_common_day = df['day'].mode()[0]
    print(f"The most common day of the week is: {most_common_day}")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(f"The most common start hour is: {most_common_hour}:00")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {most_common_start_station}")


    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {most_common_end_station}")


    # display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start and end stations is: {most_common_trip[0]} -> {most_common_trip[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is: {total_travel_time} seconds")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Counts of user types:{user_types}")


    # Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print(f"\nCounts of gender:{gender_counts}")


    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = int(df['Birth Year'].min())
    most_recent_birth_year = int(df['Birth Year'].max())
    most_common_birth_year = int(df['Birth Year'].mode()[0])
        
    print("\nEarliest year of birth:", earliest_birth_year)
    print("Most recent year of birth:", most_recent_birth_year)
    print("Most common year of birth:", most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def DisplayRawData(df):

    counter = 5

    answers = ['yes','no']
    answer = input('Do You Want See Raw Data ? Yes Or No \n')

    while answer.lower() not in answers:
        answer = input('Worng Input , Please Choose Yes Or No Only \n')

    if answer.lower() == 'yes':

        while True:
            print(df.head(counter))
            counter = counter + 5
            RawDataAnswer = input('type More if you want to see more data or No to exit \n ')
            while RawDataAnswer.lower() not in ['more','no']:
                    RawDataAnswer = input('Worng Input  Please Choose More Or No Only \n')
            if RawDataAnswer.lower() == 'no':
              break    
    elif answer.lower() == 'no':
        print('ThankYou')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        DisplayRawData(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
