"""
==============================================================
REVISED SEABORN MASTER PROGRAM 2
Filename: revised_seaborn_master_program_2.py

Top 5 Remaining Charts for Data Analysts
----------------------------------------
1. sns.boxplot()
2. sns.violinplot()
3. sns.boxenplot()
4. sns.heatmap()
5. sns.pairplot()

Every chart demonstrates (where applicable):
- figsize & dpi
- title
- xlabel / ylabel
- hue / palette
- grid
- annotate / text
- tight_layout()
- savefig()
- show()
- close()
==============================================================
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="deep", context="notebook")
np.random.seed(42)

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"],
    "Sales":[120,140,135,170,165,190,220,210,240,260],
    "Profit":[20,22,18,30,28,35,40,42,45,50],
    "Category":["A","B","A","C","B","A","C","A","B","C"]
})

# ============================================================
# 1. BOXPLOT
# ============================================================
plt.figure(figsize=(10,6), dpi=150)
sns.boxplot(data=df, x="Category", y="Sales", hue="Category")
plt.title("Sales Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.grid(True)
plt.annotate("Highest", xy=(2,220), xytext=(1.5,245),
             arrowprops=dict(arrowstyle="->"))
plt.text(0,250,"Outliers & Spread")
plt.tight_layout()
plt.savefig("06_boxplot.png", dpi=300)
plt.show()
plt.close()

# ============================================================
# 2. VIOLINPLOT
# ============================================================
plt.figure(figsize=(10,6), dpi=150)
sns.violinplot(data=df, x="Category", y="Sales", hue="Category", inner="quart")
plt.title("Violin Plot")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("07_violinplot.png", dpi=300)
plt.show()
plt.close()

# ============================================================
# 3. BOXENPLOT
# ============================================================
plt.figure(figsize=(10,6), dpi=150)
sns.boxenplot(data=df, x="Category", y="Sales", hue="Category")
plt.title("Boxen Plot")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("08_boxenplot.png", dpi=300)
plt.show()
plt.close()

# ============================================================
# 4. HEATMAP
# ============================================================
corr = df[["Sales","Profit"]].corr()

plt.figure(figsize=(8,6), dpi=150)
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=1,
    fmt=".2f",
    cbar=True
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("09_heatmap.png", dpi=300)
plt.show()
plt.close()

# ============================================================
# 5. PAIRPLOT
# ============================================================
pair = sns.pairplot(
    data=df,
    vars=["Sales","Profit"],
    hue="Category",
    diag_kind="hist"
)
pair.fig.suptitle("Pair Plot", y=1.02)
pair.savefig("10_pairplot.png", dpi=300)
plt.show()
plt.close('all')

print("="*60)
print("REVISED SEABORN MASTER PROGRAM 2 COMPLETED")
print("""
Charts Covered
--------------
1. sns.boxplot()
2. sns.violinplot()
3. sns.boxenplot()
4. sns.heatmap()
5. sns.pairplot()

Industry Tips
-------------
* boxplot  -> Detect outliers
* violinplot -> Distribution + density
* boxenplot -> Large datasets
* heatmap -> Correlation analysis
* pairplot -> Exploratory Data Analysis (EDA)
""")
print("="*60)
