import pandas as pd

def demographic_data_analyzer():
    # Load the data
    df = pd.read_csv('adult.data.csv')

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_high_education_rich = round((df[advanced_education]['salary'] == '>50K').mean() * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    percentage_low_education_rich = round((df[~advanced_education]['salary'] == '>50K').mean() * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers_rich_percentage = round((df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / df[df['hours-per-week'] == min_work_hours].shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    countries_over_50k = df[df['salary'] == '>50K']['native-country'].value_counts()
    countries_total = df['native-country'].value_counts()
    highest_earning_country = (countries_over_50k / countries_total * 100).idxmax()
    highest_earning_country_percentage = round((countries_over_50k / countries_total * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_high_education_rich': percentage_high_education_rich,
        'percentage_low_education_rich': percentage_low_education_rich,
        'min_work_hours': min_work_hours,
        'min_workers_rich_percentage': min_workers_rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Example usage
result = demographic_data_analyzer()
for key, value in result.items():
    print(f"{key}: {value}")
