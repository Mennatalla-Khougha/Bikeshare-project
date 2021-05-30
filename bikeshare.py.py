import pandas as pd
import numpy as np
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month = "all", day = "all"):
    """Loads data for the specified city and filters by month and day if applicable."""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df["Start_Hour"]= df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month) +1
        df = df[df["month"] == month]

    if day != 'all':
        df = df[df["day_of_week"] == day.title()]

    return df
def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    print("Hello! Let's explore some US bikeshare data!")
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?").lower()
        if (city == "chicago"):
            break
        elif (city == "new york"):
            break
        elif (city == "washington" ):
            break
        else:
            print("Yor entered an invalid value, please choose a valid value")
            continue

    while True:
        filter = input("Would you like to filter the data by month, day, or not at all (type no for no filtering)").lower()
        day = "all"
        month = "all"
        if filter =="no":
            break
        elif filter !="no":
            if filter == "month" :
                while True:
                    month = input("Which month - January, February, March, April, May, June or all? ").lower()
                    if (month == "January") or (month == "february") or (month == "March") or (month == "april") or (month =="may") or (month == "june") or (month == "all"):
                        break
                    else:
                        print("Yor entered an invalid value, please choose a valid value")
                        continue

                while True:
                    another_filter = input("Would you like to filter the data by day (press y or n)").lower()
                    if another_filter == "n":
                        break
                    elif another_filter !="y":
                        print("Yor entered an invalid value, please choose a valid value")
                        continue
                    else:
                        while True:
                            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ").lower()
                            if (day == "monday") or (day == "tuesday") or ( day == "wednesday") or (day == "thursday") or (day == "friday") or (day == "saturday") or (day == "sunday") or (day == "all"):
                                break
                            else:
                                print("Yor entered an invalid value, please choose a valid value")
                                continue
                    break
                break
            elif filter == "day":
                while True :
                    day = input("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all").lower()
                    if (day == "monday") or (day == "tuesday") or ( day == "wednesday") or (day == "thursday") or (day == "friday") or (day == "saturday") or (day == "sunday") or (day == "all"):
                        break
                    else:
                        print("Yor entered an invalid value, please choose a valid value")
                        continue
                break
            else:
                print("Yor entered an invalid value, please choose a valid value")
                continue

    return (city, month, day)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_month = df['month'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    popular_hour = df["Start_Hour"].mode()[0]
    print("the most commen month to travel is" + " " + str(popular_month))
    print("the most commen day to travel is" + " " + str(popular_day))
    print("the most commen start hour to travel is" + " " + str(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start = df['Start Station'].mode()[0]
    popular_end = df['End Station'].mode()[0]
    popular_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("the most commonly used start station is" + " " + str(popular_start))
    print("the most commonly used end station is" + " " + str(popular_end))
    print("the most frequent combination of start station and end station is" + " " + str(popular_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel = df["Trip Duration"].sum()
    average_travel = df["Trip Duration"].mean()
    print("The total travel time is " + str(total_travel) +" seconds")
    print("The total travel time is " + str(average_travel) +" seconds")
    print("\nThis took %s seconds." % (time.time() - start_time))

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    try:
        start_time = time.time()
        user_type = df["User Type"].value_counts()
        gender = df["Gender"].value_counts()
        most_common = df["Birth Year"].mode()[0]
        df = df.sort_values(by = ["Birth Year"])
        df = df.fillna(method = 'ffill', axis = 0)
        earliest = df["Birth Year"].iloc[0]
        most_recent = df["Birth Year"].iloc[-1]
        print("The counts of user types is " + str(user_type))
        print("The counts of gender is " + str(gender))
        print("The earliest year of birth is " + str(earliest))
        print("The most recent year of birth is " + str(most_recent))
        print("The most common year of birth is " + str(most_common))
        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print("This values are unavailable for Washington city")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        while True:
            q1 = input("Would you like to see the time statstics?(press Y to view) ").lower()
            if q1 != "y":
                break
            else:
                time_stats(df)
                break

        while True:
            q2 = input("Would you like to see the station statstics?(press Y to view) ").lower()
            if q2 != "y":
                break
            else:
                station_stats(df)
                break

        while True:
            q3 = input("Would you like to see the trip duration statstics?(press Y to view) ").lower()
            if q3 != "y":
                break
            else:
                trip_duration_stats(df)
                break

        while True:
            q4 = input("Would you like to see the user statstics?(press Y to view) ").lower()
            if q4 != "y":
                break
            else:
                user_stats(df)
                break



        while True:
            index1 = 0
            index2 = 5
            see_data = input("Would you like to see the actual data? (press y or n)").lower()
            if see_data == "n":
                break
            elif see_data != "y":
                print("Yor entered an invalid value, please choose a valid value")
                continue
            else:
                print(df.iloc[index1:index2, :])
                index1 += 5
                index2 += 5
                while True:
                    see_more = input("Would you like to see more data? (press y or n)").lower()
                    if see_more == "n":
                        break
                    elif see_more != "y":
                        print("Yor entered an invalid value, please choose a valid value")
                        continue
                    else:
                        print(df.iloc[index1:index2, :])
                        index1 += 5
                        index2 += 5
                        continue
                break



        restart = input('\nWould you like to restart? Enter yes to restart')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
