"""
=========================================================
REVISED MATPLOTLIB MASTER PROGRAM 1
Filename : revised_matplotlib_master_program.py

Topics Covered
--------------
1. Line Plot
2. Scatter Plot
3. Bar Chart
4. Horizontal Bar Chart
5. Histogram

Goal:
Each chart demonstrates the most commonly used parameters
that a Data Analyst should know.
=========================================================
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# ---------------------------------------------------------
# Sample Data
# ---------------------------------------------------------
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
x = np.arange(len(months))

sales = np.array([120,140,135,170,165,190,220,210,240,260])
profit = np.array([20,22,18,30,28,35,40,42,45,50])

# =========================================================
# 1. LINE PLOT
# =========================================================
plt.figure(figsize=(10,6), dpi=150)

plt.plot(
    x,
    sales,
    color="blue",
    linestyle="--",
    linewidth=3,
    marker="o",
    markersize=10,
    markerfacecolor="yellow",
    markeredgecolor="black",
    alpha=0.8,
    label="Sales"
)

plt.title("Monthly Sales", fontsize=18)
plt.xlabel("Months", fontsize=14)
plt.ylabel("Sales", fontsize=14)

plt.xticks(x, months, rotation=45)
plt.yticks(range(100,281,20))

plt.xlim(-0.5,9.5)
plt.ylim(100,280)

plt.grid(True)

plt.annotate(
    "Highest Sales",
    xy=(9,260),
    xytext=(6.5,245),
    arrowprops={"arrowstyle":"->"}
)

plt.text(1,250,"Q1")

plt.legend()

plt.tight_layout()
plt.savefig("01_line_plot.png", dpi=300)
plt.show()
plt.close()

# =========================================================
# 2. SCATTER PLOT
# =========================================================
plt.figure(figsize=(10,6), dpi=150)

plt.scatter(
    sales,
    profit,
    color="red",
    marker="o",
    s=120,
    alpha=0.7,
    label="Products"
)

plt.title("Sales vs Profit", fontsize=18)
plt.xlabel("Sales", fontsize=14)
plt.ylabel("Profit", fontsize=14)

plt.xticks(range(120,281,20))
plt.yticks(range(15,56,5))

plt.xlim(110,270)
plt.ylim(15,55)

plt.grid(True)

idx = np.argmax(profit)
plt.annotate(
    "Best Profit",
    xy=(sales[idx], profit[idx]),
    xytext=(220,47),
    arrowprops={"arrowstyle":"->"}
)

plt.text(130,50,"Growth")

plt.legend()

plt.tight_layout()
plt.savefig("02_scatter_plot.png", dpi=300)
plt.show()
plt.close()

# =========================================================
# 3. BAR CHART
# =========================================================
plt.figure(figsize=(10,6), dpi=150)

bars = plt.bar(
    months,
    sales,
    color="skyblue",
    edgecolor="black",
    linewidth=1.5,
    alpha=0.8,
    label="Sales"
)

plt.title("Sales by Month", fontsize=18)
plt.xlabel("Months", fontsize=14)
plt.ylabel("Sales", fontsize=14)

plt.xticks(rotation=45)
plt.yticks(range(100,281,20))
plt.ylim(100,280)
plt.grid(axis="y")

plt.annotate(
    "Highest",
    xy=(9,260),
    xytext=(7.3,245),
    arrowprops={"arrowstyle":"->"}
)

plt.text(0,255,"Q1")

plt.legend()

plt.tight_layout()
plt.savefig("03_bar_chart.png", dpi=300)
plt.show()
plt.close()

# =========================================================
# 4. HORIZONTAL BAR CHART
# =========================================================
plt.figure(figsize=(10,6), dpi=150)

plt.barh(
    months,
    profit,
    color="orange",
    edgecolor="black",
    alpha=0.8,
    label="Profit"
)

plt.title("Profit by Month", fontsize=18)
plt.xlabel("Profit", fontsize=14)
plt.ylabel("Months", fontsize=14)

plt.xticks(range(15,56,5))
plt.xlim(15,55)
plt.grid(axis="x")

plt.annotate(
    "Highest",
    xy=(50,"Oct"),
    xytext=(42,8),
    arrowprops={"arrowstyle":"->"}
)

plt.text(18,0,"Start")

plt.legend()

plt.tight_layout()
plt.savefig("04_barh_chart.png", dpi=300)
plt.show()
plt.close()

# =========================================================
# 5. HISTOGRAM
# =========================================================
data = np.random.normal(50,10,500)

plt.figure(figsize=(10,6), dpi=150)

plt.hist(
    data,
    bins=20,
    color="purple",
    edgecolor="black",
    alpha=0.75,
    label="Distribution"
)

plt.title("Histogram", fontsize=18)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Frequency", fontsize=14)

plt.grid(True)

plt.annotate(
    "Mean Area",
    xy=(50,40),
    xytext=(60,50),
    arrowprops={"arrowstyle":"->"}
)

plt.text(30,55,"Normal Distribution")

plt.legend()

plt.tight_layout()
plt.savefig("05_histogram.png", dpi=300)
plt.show()
plt.close()

print("="*60)
print("REVISED MATPLOTLIB MASTER PROGRAM 1 COMPLETED")
print("Charts Covered:")
print("1. Line Plot")
print("2. Scatter Plot")
print("3. Bar Chart")
print("4. Horizontal Bar Chart")
print("5. Histogram")
print("="*60)
