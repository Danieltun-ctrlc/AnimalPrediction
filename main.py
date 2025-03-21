import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

## data sheets

# elephants data
elephants_df = pd.read_excel("animal_anal.xlsx", sheet_name="Sheet1", engine="openpyxl")


# turtle data
turtles_df = pd.read_excel("animal_anal.xlsx", sheet_name="Sheet2", engine="openpyxl")


# butterfly
butter_df = pd.read_excel("animal_anal.xlsx", sheet_name="Sheet3", engine="openpyxl")


# rhino
rhino_df = pd.read_excel("animal_anal.xlsx", sheet_name="Sheet5", engine="openpyxl")

animal = ''



print("""
Hello Welcome to the Animal Population Prediction !\n
You can choose the  Elephant, Turtle, Butterfly and Rhino

""")
while True:
    user_animal = input("Choose the animal that you want to know:").lower()
    if user_animal == 'elephant':
        animal = elephants_df
        break
    elif user_animal == 'turtle':
        animal = turtles_df
        break
    elif user_animal == 'butterfly':
        animal = butter_df
        break
    elif user_animal == "rhino":
        animal = rhino_df
        break
    else:
        print("Type the only specify animals.")

while True:
    try:
        user_year = int(input("until which future year you would like to know the population( eg 2035 ):"))

    except ValueError:
        print("please only put in the integers format")

    else:
        if user_year <= 2024:
            print("please type the future years only.")
        else:
            break

print(animal)


def calculation(year, animal):
    year_ = animal.loc[:, 'Year']
    listed_year = year_.tolist()

    np_array_year = np.array(listed_year)

    population = animal.loc[:, 'population']
    listed_p = population.tolist()

    np_array_population = np.array(listed_p)

    # Calculate decay rate (k)
    t = np_array_year[-1] - np_array_year[0]
    y0 = np_array_population[0]
    yt = np_array_population[-1]
    k = (1 / t) * np.log(y0 / yt)

    time_d = year - 2000
    return y0 * np.exp(-k * time_d)


users_future_year = [2024 + i for i in range(1, (user_year - 2024) + 1)]
print(users_future_year)
users_future_pop = np.array([calculation(2024 + i, animal) for i in range(1, (user_year - 2024) + 1)],
                            dtype='int').tolist()
print(users_future_pop)

# Create bar chart
plt.bar(users_future_year, users_future_pop, color='blue')

# Labels and title
plt.xlabel("Year")
plt.ylabel(f"{user_animal.capitalize()} Population")
plt.title(f" Estimated {user_animal.capitalize()} Population Decline Over Time")

# Show the chart
plt.show()
