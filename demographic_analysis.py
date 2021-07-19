import pandas as pd


def calculate_demographic_data(print_data=True):
    
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"]=="Male"]["age"].mean().round(1)


    # What is the percentage of people who have a Bachelor's degree?
    total_bachelors = len(df[df["education"]=="Bachelors"])
    total_people = len(df)
    percentage_bachelors = round(total_bachelors/total_people*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors","Doctorate","Masters"])]
    lower_education = df[~df["education"].isin(["Bachelors","Doctorate","Masters"])]

    # percentage with salary >50K
    higher_education_salary = len(higher_education[higher_education.salary ==">50K"])
    higher_education_rich = round(higher_education_salary/len(higher_education)*100,1)
    lower_education_salary = len(lower_education[lower_education.salary == ">50K"])
    lower_education_rich = round(lower_education_salary/len(lower_education)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"]==min_work_hours]

    rich_percentage = round(len(num_min_workers[num_min_workers.salary == ">50K"]) / len(num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    country_total = df["native-country"].value_counts()
    country_rich = df[df.salary == ">50K"]["native-country"].value_counts()
    highest_earning_country = (country_rich/country_total*100).idxmax()
    highest_earning_country_percentage = round(country_rich/country_total*100,1).max()

    # Identify the most popular occupation for those who earn >50K in India.
    indian_rich = df[(df["native-country"]=="India") & (df["salary"] == ">50K")]
    top_IN_occupation = indian_rich["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
 #Here are the results:
 
 #Number of each race:
 #White                 27816
 #Black                  3124
 #Asian-Pac-Islander     1039
 #Amer-Indian-Eskimo      311
 #Other                   271
 #Name: race, dtype: int64
 #Average age of men: 39.4
 #Percentage with Bachelors degrees: 16.4%
 #Percentage with higher education that earn >50K: 46.5%
 #Percentage without higher education that earn >50K: 17.4%
 #Min work time: 1 hours/week
 #Percentage of rich among those who work fewest hours: 10.0%
 #Country with highest percentage of rich: Iran
 #Highest percentage of rich people in country: 41.9%
 #Top occupations in India: Prof-specialty
