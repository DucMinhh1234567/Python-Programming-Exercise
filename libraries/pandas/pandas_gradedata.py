import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read CSV file
def ex1():
    df = pd.read_csv('gradedata.csv')
    return df


# Display first 10 rows
def ex2():
    df = pd.read_csv('gradedata.csv')
    return df.head(10)


# Display last 5 rows
def ex3():
    df = pd.read_csv('gradedata.csv')
    return df.tail(5)


# Get DataFrame info
def ex4():
    df = pd.read_csv('gradedata.csv')
    return df.info()


# Get basic statistics
def ex5():
    df = pd.read_csv('gradedata.csv')
    return df.describe()


# Get number of rows and columns
def ex6():
    df = pd.read_csv('gradedata.csv')
    return df.shape


# Get column names
def ex7():
    df = pd.read_csv('gradedata.csv')
    return df.columns.tolist()


# Get data types
def ex8():
    df = pd.read_csv('gradedata.csv')
    return df.dtypes


# Access specific column
def ex9():
    df = pd.read_csv('gradedata.csv')
    return df['grade'].head(10)


# Access multiple columns
def ex10():
    df = pd.read_csv('gradedata.csv')
    return df[['fname', 'lname', 'grade']].head(10)


# Filter students with grade > certain value (ex: 90)
def ex11():
    df = pd.read_csv('gradedata.csv')
    return df[df['grade'] > 90][['fname', 'lname', 'grade']]


# Multiple conditions - female students with grade > certain value (ex: 85)
def ex12():
    df = pd.read_csv('gradedata.csv')
    return df[(df['gender'] == 'female') & (df['grade'] > 85)][['fname', 'lname', 'grade']].head(10)


# Sort by grade descending
def ex13():
    df = pd.read_csv('gradedata.csv')
    return df.sort_values('grade', ascending=False)[['fname', 'lname', 'grade']].head(10)


# Sort by multiple columns
def ex14():
    df = pd.read_csv('gradedata.csv')
    return df.sort_values(['gender', 'grade'], ascending=[True, False])[['fname', 'lname', 'gender', 'grade']].head(10)


# Count by gender
def ex15():
    df = pd.read_csv('gradedata.csv')
    return df['gender'].value_counts()


# Average grade
def ex16():
    df = pd.read_csv('gradedata.csv')
    return df['grade'].mean()


# Statistics by gender
def ex17():
    df = pd.read_csv('gradedata.csv')
    return df.groupby('gender')['grade'].agg(['count', 'mean', 'min', 'max'])


# Top n students
def ex18():
    df = pd.read_csv('gradedata.csv')
    return df.nlargest(10, 'grade')[['fname', 'lname', 'grade', 'hours']]


# Check for missing values
def ex19():
    df = pd.read_csv('gradedata.csv')
    return df.isnull().sum()


# Check for duplicates
def ex20():
    df = pd.read_csv('gradedata.csv')
    return df.duplicated().sum()


# Most common first names
def ex21():
    df = pd.read_csv('gradedata.csv')
    return df['fname'].value_counts().head(10)


# Grade distribution by bins
def ex22():
    df = pd.read_csv('gradedata.csv')
    bins = [0, 60, 70, 80, 90, 100]
    labels = ['F', 'D', 'C', 'B', 'A']
    df['grade_letter'] = pd.cut(df['grade'], bins=bins, labels=labels)
    return df['grade_letter'].value_counts().sort_index()


# Correlation matrix
def ex23():
    df = pd.read_csv('gradedata.csv')
    return df[['age', 'exercise', 'hours', 'grade']].corr()


# Add full name column
def ex24():
    df = pd.read_csv('gradedata.csv')
    df['full_name'] = df['fname'] + ' ' + df['lname']
    return df[['full_name', 'grade']].head(10)


# Calculate pass/fail status
def ex25():
    df = pd.read_csv('gradedata.csv')
    df['pass_fail'] = df['grade'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
    return df[['fname', 'lname', 'grade', 'pass_fail']].head(10)


# Pivot table - average grade by age and gender
def ex26():
    df = pd.read_csv('gradedata.csv')
    return df.pivot_table(values='grade', index='age', columns='gender', aggfunc='mean').round(2)


# Statistics by exercise level
def ex27():
    df = pd.read_csv('gradedata.csv')
    return df.groupby('exercise')['grade'].agg(['count', 'mean', 'min', 'max']).round(2)


# Compare male vs female performance
def ex28():
    df = pd.read_csv('gradedata.csv')
    comparison = df.groupby('gender').agg({
        'grade': ['count', 'mean', 'median', 'std'],
        'hours': ['mean'],
        'exercise': ['mean']
    }).round(2)
    return comparison


# Extract state from address
def ex29():
    df = pd.read_csv('gradedata.csv')
    df['state'] = df['address'].str.extract(r', ([A-Z]{2}) \d')
    return df.groupby('state')['grade'].agg(['count', 'mean']).round(2).sort_values('mean', ascending=False).head(10)


# Age group analysis
def ex30():
    df = pd.read_csv('gradedata.csv')
    bins = [13, 15, 17, 20]
    labels = ['13-15', '16-17', '18-20']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
    return df.groupby('age_group')['grade'].agg(['count', 'mean']).round(2)


# Cleaning Empty Cells
def ex31():
    df = pd.read_csv('gradedata.csv')
    print("Missing values per column:")
    print(df.isnull().sum())
    
    df['grade'] = df['grade'].fillna(df['grade'].mean())
    df['hours'] = df['hours'].fillna(df['hours'].mean())
    df['gender'] = df['gender'].fillna(df['gender'].mode()[0])
    
    return df.head(10)


# Cleaning Wrong Format
def ex32():
    df = pd.read_csv('gradedata.csv')
    df['age'] = df['age'].astype(int)
    df['grade'] = df['grade'].astype(float)
    
    df['fname'] = df['fname'].str.strip().str.title()
    df['lname'] = df['lname'].str.strip().str.title()
    df['gender'] = df['gender'].str.lower()
    
    return df[['fname', 'lname', 'gender', 'age', 'grade']].head(10)


# Cleaning Wrong Data
def ex33():
    df = pd.read_csv('gradedata.csv')
    Q1 = df['grade'].quantile(0.25)
    Q3 = df['grade'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    print(f"Outlier bounds: {lower_bound:.2f} - {upper_bound:.2f}")
    
    df['grade'] = df['grade'].clip(lower=0, upper=100)
    
    return df[['fname', 'lname', 'grade']].head(10)


# Removing Duplicates
def ex34():
    df = pd.read_csv('gradedata.csv')
    print(f"Total rows: {len(df)}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    
    df_unique = df.drop_duplicates()
    print(f"After removing duplicates: {len(df_unique)}")
    
    return df_unique.head(10)


# Pandas Correlations
def ex35():
    df = pd.read_csv('gradedata.csv')
    correlation = df[['age', 'exercise', 'hours', 'grade']].corr()
    print("\nCorrelation Matrix:")
    print(correlation)
    
    print("\n\nCorrelation with Grade:")
    print(correlation['grade'].sort_values(ascending=False))
    
    return correlation


# Plotting - Histogram
def ex36():
    df = pd.read_csv('gradedata.csv')
    df['grade'].plot(kind='hist', bins=20, edgecolor='black', alpha=0.7)
    plt.title('Grade Distribution (Histogram)')
    plt.xlabel('Grade')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.3)
    plt.show()


if __name__ == '__main__':
    print("Pandas Gradedata Analysis")
    
    print("BÀI 1: Read CSV file")
    print(ex1())

    print("\nBÀI 2: Display first 10 rows")
    print(ex2())
    
    print("\nBÀI 3: Display last 5 rows")
    print(ex3())
    
    print("\nBÀI 4: Get DataFrame info")
    ex4()
    
    print("\nBÀI 5: Get basic statistics")
    print(ex5())
    
    print("\nBÀI 6: Get number of rows and columns")
    shape = ex6()
    print(f"Rows: {shape[0]}, Columns: {shape[1]}")
    
    print("\nBÀI 7: Get column names")
    print(ex7())
    
    print("\nBÀI 8: Get data types")
    print(ex8())
    
    print("\nBÀI 9: Access specific column (grade)")
    print(ex9())
    
    print("\nBÀI 10: Access multiple columns")
    print(ex10())
    
    print("\nBÀI 11: Filter students with grade > 90")
    print(ex11())
    
    print("\nBÀI 12: Multiple conditions - female students with grade > 85")
    print(ex12())
    
    print("\nBÀI 13: Sort by grade descending")
    print(ex13())
    
    print("\nBÀI 14: Sort by multiple columns")
    print(ex14())
    
    print("\nBÀI 15: Count by gender")
    print(ex15())
    
    print("\nBÀI 16: Average grade")
    print(f"Overall Average: {ex16():.2f}")
    
    print("\nBÀI 17: Statistics by gender")
    print(ex17())
    
    print("\nBÀI 18: Top 10 students")
    print(ex18())
    
    print("\nBÀI 19: Check for missing values")
    print(ex19())
    
    print("\nBÀI 20: Check for duplicates")
    print(f"Number of duplicates: {ex20()}")
    
    print("\nBÀI 21: Most common first names")
    print(ex21())
    
    print("\nBÀI 22: Grade distribution by bins")
    print(ex22())
    
    print("\nBÀI 23: Correlation matrix")
    print(ex23())
    
    print("\nBÀI 24: Add full name column")
    print(ex24())
    
    print("\nBÀI 25: Calculate pass/fail status")
    print(ex25())
    
    print("\nBÀI 26: Pivot table - average grade by age and gender")
    print(ex26())
    
    print("\nBÀI 27: Statistics by exercise level")
    print(ex27())
    
    print("\nBÀI 28: Compare male vs female performance")
    print(ex28())
    
    print("\nBÀI 29: Extract state from address")
    print(ex29())
    
    print("\nBÀI 30: Age group analysis")
    print(ex30())

    print("\nPHẦN CLEANING DATA")
    
    print("\nBÀI 31: Cleaning Empty Cells")
    print(ex31())
    
    print("\nBÀI 32: Cleaning Wrong Format")
    print(ex32())
    
    print("\nBÀI 33: Cleaning Wrong Data")
    print(ex33())
    
    print("\nBÀI 34: Removing Duplicates")
    print(ex34())
    
    print("\nBÀI 35: Pandas Correlations")
    print(ex35())
    
    print("\nBÀI 36: Plotting - Histogram")
    ex36()