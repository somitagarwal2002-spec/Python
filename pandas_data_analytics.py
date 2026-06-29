"""
MASTER PROGRAM 3 - Pandas Data Analysis (Industry Standard)

NOTE:
This assumes the following files exist in the same folder:
    data.csv
    department_info.csv

The goal is to demonstrate the most commonly used Pandas analysis
functions used by Data Analysts.
"""

import pandas as pd

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data.csv")
dept_df = pd.read_csv("department_info.csv")

# =====================================================
# BASIC INSPECTION
# =====================================================

print(df.head())
print(df.info())

# =====================================================
# GROUPBY
# =====================================================

print(df.groupby("Department"))
print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].sum())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())
print(df.groupby("Department")["Salary"].count())
print(df.groupby("Department")["Salary"].median())

# =====================================================
# MULTIPLE GROUPBY
# =====================================================

print(df.groupby(["Department", "Gender"])["Salary"].mean())
print(df.groupby(["Department", "City"])["Sales"].sum())

# =====================================================
# AGGREGATION
# =====================================================

print(
    df.groupby("Department").agg(
        {
            "Salary": ["min", "max", "mean", "sum"],
            "Sales": ["sum", "mean"],
            "Experience": ["min", "max"],
        }
    )
)

# Named aggregation
print(
    df.groupby("Department").agg(
        Avg_Salary=("Salary", "mean"),
        Max_Salary=("Salary", "max"),
        Employees=("Employee_ID", "count"),
        Total_Sales=("Sales", "sum"),
    )
)

# =====================================================
# TRANSFORM
# =====================================================

df["Department_Avg_Salary"] = (
    df.groupby("Department")["Salary"].transform("mean")
)

df["Salary_Difference"] = (
    df["Salary"] - df["Department_Avg_Salary"]
)

# =====================================================
# FILTER
# =====================================================

print(
    df.groupby("Department").filter(
        lambda x: len(x) >= 3
    )
)

# =====================================================
# VALUE COUNTS / FREQUENCY
# =====================================================

print(df["Department"].value_counts())
print(df["City"].value_counts())
print(df["Department"].nunique())

# =====================================================
# CROSSTAB
# =====================================================

print(pd.crosstab(df["Department"], df["Gender"]))
print(pd.crosstab(df["City"], df["Work_Mode"], margins=True))

# =====================================================
# MERGE
# =====================================================

inner_merge = pd.merge(
    df,
    dept_df,
    on="Department",
    how="inner"
)

left_merge = pd.merge(
    df,
    dept_df,
    on="Department",
    how="left"
)

right_merge = pd.merge(
    df,
    dept_df,
    on="Department",
    how="right"
)

outer_merge = pd.merge(
    df,
    dept_df,
    on="Department",
    how="outer"
)

# =====================================================
# CONCAT
# =====================================================

concat_rows = pd.concat([df, df], ignore_index=True)
concat_cols = pd.concat([df, dept_df], axis=1)

# =====================================================
# JOIN
# =====================================================

left = df.set_index("Department")
right = dept_df.set_index("Department")

joined = left.join(right, how="left")

# =====================================================
# PIVOT
# =====================================================

pivot = df.pivot(
    index="Department",
    columns="Gender",
    values="Salary"
)

print(pivot)

# =====================================================
# PIVOT TABLE
# =====================================================

pivot_table = pd.pivot_table(
    df,
    index="Department",
    columns="Gender",
    values="Salary",
    aggfunc="mean",
    fill_value=0
)

print(pivot_table)

# =====================================================
# MELT
# =====================================================

melted = pd.melt(
    df,
    id_vars=["Employee_ID", "Name"],
    value_vars=["Salary", "Bonus"],
    var_name="Type",
    value_name="Amount"
)

print(melted.head())

# =====================================================
# EXPLODE
# =====================================================

temp = df.copy()
temp["Skills"] = temp["Skills"].str.split(",")
print(temp.explode("Skills").head())

# =====================================================
# STACK / UNSTACK
# =====================================================

multi = (
    df.groupby(["Department", "Gender"])["Salary"]
    .mean()
)

print(multi)
print(multi.unstack())

# =====================================================
# SORTING
# =====================================================

print(df.nlargest(10, "Salary"))
print(df.nsmallest(10, "Salary"))

# =====================================================
# CORRELATION
# =====================================================

numeric = df.select_dtypes(include="number")

print(numeric.corr())
print(numeric.cov())

# =====================================================
# ROLLING
# =====================================================

df["Rolling_Sales"] = (
    df["Sales"]
    .rolling(3)
    .mean()
)

# =====================================================
# EXPANDING
# =====================================================

df["Running_Total"] = (
    df["Sales"]
    .expanding()
    .sum()
)

# =====================================================
# SHIFT
# =====================================================

df["Previous_Sales"] = df["Sales"].shift(1)

# =====================================================
# DIFF
# =====================================================

df["Sales_Difference"] = df["Sales"].diff()

# =====================================================
# PERCENT CHANGE
# =====================================================

df["Sales_Growth"] = (
    df["Sales"]
    .pct_change()
)

# =====================================================
# RANK
# =====================================================

df["Salary_Rank"] = (
    df["Salary"]
    .rank(ascending=False)
)

# =====================================================
# MEMORY OPTIMIZATION
# =====================================================

df["Department"] = df["Department"].astype("category")
df["Gender"] = df["Gender"].astype("category")

# =====================================================
# BUSINESS KPI EXAMPLES
# =====================================================

print("Total Sales:", df["Sales"].sum())
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print("Average Performance:", df["Performance_Rating"].mean())

department_kpi = (
    df.groupby("Department")
    .agg(
        Employees=("Employee_ID", "count"),
        Avg_Salary=("Salary", "mean"),
        Total_Sales=("Sales", "sum"),
        Avg_Performance=("Performance_Rating", "mean"),
    )
    .sort_values("Total_Sales", ascending=False)
)

print(department_kpi)

# =====================================================
# METHOD CHAINING
# =====================================================

summary = (
    df
    .query("Salary > 30000")
    .groupby("Department")
    .agg(
        Avg_Salary=("Salary", "mean"),
        Total_Sales=("Sales", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print(summary)

# =====================================================
# EXPORT
# =====================================================

department_kpi.to_csv("department_kpi.csv")
summary.to_csv("summary.csv")
df.to_csv("analysis_output.csv", index=False)

print("Master Program 3 Completed Successfully.")
