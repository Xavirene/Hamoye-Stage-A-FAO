import pandas as pd

# Data
df = pd.read_csv("file.csv")

# =========== Question 11 =======================
# Get a list of all rows where "Item" == "Animal fats"
animalFat = df.loc[df['Item']=='Animal fats']

# Calculate total for every column
TotalAnimalFat = animalFat.sum()

# Extract the total for year 2014 and 2017
TotalAnimalFat2014 = TotalAnimalFat['Y2014']
TotalAnimalFat2017 = TotalAnimalFat['Y2017']

print("Question 11")
print("Total sum of Animal Fat produced in 2014 is", TotalAnimalFat2014)
print("Total sum of Animal Fat produced in 2017 is", TotalAnimalFat2017)


# =========== Question 12 =======================
# Calculate mean deviation and standard deviation for year 2015
md2015 = df['Y2015'].mad()
sd2015 = df['Y2015'].std()

print("\nQuestion 12")
print("Mean deviation for year 2015 is:", round(md2015, 3))
print("Standard deviation for year 2015 is:", round(sd2015, 3))

# =========== Question 13 =======================
# Calculate total number of missing data
totalMissing = len(df[lambda df: pd.isna(df['Y2016'])])
# Calculate overall total
total = len(df)
# Percentage
percentageOfMissingData = (totalMissing/total)*100

print("\nQuestion 13")
print("Total number of missing data: ", totalMissing)
print("Percentage of missing data: ", round(percentageOfMissingData, 2))

# =========== Question 14 =======================
# Get correlation index for all columns
correlations = df.corr(method="pearson")

# Filter correlation indexes for only Element code
corrWithElementCode = correlations['Element Code']

# Drop all columns that do not represent a year
corrWithElementCode = corrWithElementCode[['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']]

# Get The column with the highest correlation
highestCorrWithElementCode = corrWithElementCode[lambda corr: corr == corrWithElementCode.max()]
highestCorrWithElementCodeName = corrWithElementCode.index[0]

print("\nQuestion 14")
print(f"\"{highestCorrWithElementCodeName}\" has the highest correlation with \"Element Code\"")


# =========== Question 15 =======================
sumOfImportQuantities = df[df['Element'] == "Import Quantity"].sum()
sumOfImportQuantities = sumOfImportQuantities[['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']]
highestSumOfImportQuantities = sumOfImportQuantities[lambda qty: qty == sumOfImportQuantities.max()]
highestSumOfImportQuantitiesName = highestSumOfImportQuantities.index[0]


print("\nQuestion 15")
print(f'"{highestSumOfImportQuantitiesName}" has the highest sum of import quantity')


# =========== Question 16 =======================
sumOfProduction = df[df['Element'] == "Production"].sum()
totalSumOfProduction = sumOfProduction['Y2014'].sum()


print("\nQuestion 16")
print(f"Total sum of production in year 2014:", totalSumOfProduction)


# =========== Question 17 =======================
elementSum2018 = df.groupby('Element')['Y2018'].sum()
# maxElementSum2018 = elementsSum['Y2018'].max()

maxElementSum = elementSum2018[lambda sum: sum == elementSum2018.max()]
maxElementSumName = maxElementSum.index[0]

print("\nQuestion 17")
print("Element with the highest sum:", maxElementSumName)



# =========== Question 18 =======================
elementSum2018 = df.groupby('Element')['Y2018'].sum()

thirdLowestElementSum = elementSum2018[lambda sum: sum == elementSum2018.sort_values()[2]]
thirdLowestElementSumName = thirdLowestElementSum.index[0]

print("\nQuestion 18")
print("Element with the third lowest sum:", thirdLowestElementSumName)


# =========== Question 19 =======================
totalIQAlgeria2018 = df[(df["Area"] == "Algeria") & (df["Element"] == "Import Quantity")]['Y2018'].sum()

print("\nQuestion 19")
print("Total Import quantity in algeria 2018", totalIQAlgeria2018)


# =========== Question 20 =======================
totalUniqueCountries = df["Area"].nunique()

print("\nQuestion 20")
print("Total number of unique countries:", totalUniqueCountries)