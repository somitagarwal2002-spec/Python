"""
REVISED SEABORN MASTER PROGRAM 1
Filename: revised_seaborn_master_program.py

Top 5 Charts:
1. sns.lineplot()
2. sns.scatterplot()
3. sns.barplot()
4. sns.countplot()
5. sns.histplot()

Each chart demonstrates:
- figsize, dpi
- title, xlabel, ylabel
- xticks, yticks (where applicable)
- xlim, ylim (where applicable)
- grid
- legend
- annotate
- text
- alpha
- palette / hue
- tight_layout
- savefig
- show
- close
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="deep")

np.random.seed(42)

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"],
    "Sales":[120,140,135,170,165,190,220,210,240,260],
    "Profit":[20,22,18,30,28,35,40,42,45,50],
    "Category":["A","B","A","C","B","A","C","A","B","C"]
})

# ============================================================
# 1. LINEPLOT
# ============================================================
plt.figure(figsize=(10,6), dpi=150)
sns.lineplot(data=df,x="Month",y="Sales",marker="o",linewidth=3,color="royalblue",label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.yticks(range(100,281,20))
plt.ylim(100,280)
plt.grid(True)
plt.annotate("Highest",xy=("Oct",260),xytext=("Jul",245),arrowprops={"arrowstyle":"->"})
plt.text("Feb",250,"Q1")
plt.legend()
plt.tight_layout()
plt.savefig("01_lineplot.png",dpi=300)
plt.show()
plt.close()

# ============================================================
# 2. SCATTERPLOT
# ============================================================
plt.figure(figsize=(10,6), dpi=150)
sns.scatterplot(data=df,x="Sales",y="Profit",hue="Category",style="Category",s=140,alpha=0.8)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.xlim(110,270)
plt.ylim(15,55)
plt.grid(True)
plt.annotate("Best",xy=(260,50),xytext=(220,46),arrowprops={"arrowstyle":"->"})
plt.tight_layout()
plt.savefig("02_scatterplot.png",dpi=300)
plt.show()
plt.close()

# ============================================================
# 3. BARPLOT
# ============================================================
plt.figure(figsize=(10,6), dpi=150)
sns.barplot(data=df,x="Month",y="Sales",hue="Category",errorbar=None)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.legend()
plt.tight_layout()
plt.savefig("03_barplot.png",dpi=300)
plt.show()
plt.close()

# ============================================================
# 4. COUNTPLOT
# ============================================================
plt.figure(figsize=(8,5), dpi=150)
sns.countplot(data=df,x="Category",hue="Category")
plt.title("Category Count")
plt.xlabel("Category")
plt.ylabel("Count")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("04_countplot.png",dpi=300)
plt.show()
plt.close()

# ============================================================
# 5. HISTPLOT
# ============================================================
plt.figure(figsize=(10,6), dpi=150)
sns.histplot(data=df,x="Sales",bins=6,kde=True,color="purple",alpha=0.7)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.savefig("05_histplot.png",dpi=300)
plt.show()
plt.close()

print("REVISED SEABORN MASTER PROGRAM 1 COMPLETED")
