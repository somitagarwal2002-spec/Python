"""
=========================================================
REVISED MATPLOTLIB MASTER PROGRAM 2
Filename : revised_matplotlib_master_program_2.py

Topics Covered
--------------
1. Pie Chart
2. Box Plot
3. Stem Plot
4. Step Plot
5. Error Bar
6. Stack Plot
7. Fill Between
8. Subplots
9. Multiple Line Plot
10. Best Practices Summary
=========================================================
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
x = np.arange(len(months))
sales = np.array([120,140,135,170,165,190,220,210,240,260])
profit = np.array([20,22,18,30,28,35,40,42,45,50])

# 1. PIE CHART
plt.figure(figsize=(8,8), dpi=150)
sizes=[35,25,20,20]
labels=["Python","SQL","Power BI","Excel"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90,
        colors=["gold","skyblue","lightgreen","salmon"])
plt.title("Skill Distribution", fontsize=18)
plt.tight_layout()
plt.savefig("06_pie_chart.png", dpi=300)
plt.show()
plt.close()

# 2. BOX PLOT
plt.figure(figsize=(10,6), dpi=150)
plt.boxplot(sales, patch_artist=True)
plt.title("Sales Box Plot", fontsize=18)
plt.ylabel("Sales")
plt.grid(True)
plt.text(1.05,220,"Median & Quartiles")
plt.tight_layout()
plt.savefig("07_boxplot.png", dpi=300)
plt.show()
plt.close()

# 3. STEM PLOT
plt.figure(figsize=(10,6), dpi=150)
plt.stem(x, sales, linefmt="b-", markerfmt="bo", basefmt="k-")
plt.title("Stem Plot", fontsize=18)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(x, months, rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("08_stem.png", dpi=300)
plt.show()
plt.close()

# 4. STEP PLOT
plt.figure(figsize=(10,6), dpi=150)
plt.step(x, sales, where="mid", color="green", linewidth=2, label="Sales")
plt.title("Step Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(x, months, rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("09_step.png", dpi=300)
plt.show()
plt.close()

# 5. ERROR BAR
err=np.random.randint(3,8,len(sales))
plt.figure(figsize=(10,6), dpi=150)
plt.errorbar(x, sales, yerr=err, fmt="o--", capsize=5,
             color="red", linewidth=2, label="Sales")
plt.title("Error Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(x, months, rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("10_errorbar.png", dpi=300)
plt.show()
plt.close()

# 6. STACK PLOT
plt.figure(figsize=(10,6), dpi=150)
a=[1,2,3,4,5]
b=[2,2,2,2,2]
c=[1,1,2,2,3]
plt.stackplot(range(1,6), a,b,c, labels=["A","B","C"], alpha=0.8)
plt.title("Stack Plot")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("11_stackplot.png", dpi=300)
plt.show()
plt.close()

# 7. FILL BETWEEN
xx=np.linspace(0,10,200)
yy=np.sin(xx)
plt.figure(figsize=(10,6), dpi=150)
plt.plot(xx,yy,color="blue",linewidth=2,label="sin(x)")
plt.fill_between(xx,yy,alpha=0.3,color="cyan")
plt.title("Fill Between")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("12_fill_between.png", dpi=300)
plt.show()
plt.close()

# 8. SUBPLOTS
fig,ax=plt.subplots(1,2,figsize=(12,5),dpi=150)
ax[0].plot(x,sales,marker="o")
ax[0].set_title("Sales")
ax[0].grid(True)
ax[0].set_xticks(x)
ax[0].set_xticklabels(months,rotation=45)
ax[1].bar(months,profit,color="orange")
ax[1].set_title("Profit")
ax[1].grid(axis="y")
plt.tight_layout()
plt.savefig("13_subplots.png",dpi=300)
plt.show()
plt.close()

# 9. MULTIPLE LINE PLOT
plt.figure(figsize=(10,6),dpi=150)
plt.plot(x,sales,marker="o",linewidth=2,label="Sales")
plt.plot(x,profit,marker="s",linewidth=2,label="Profit")
plt.title("Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Values")
plt.xticks(x,months,rotation=45)
plt.annotate("Peak",xy=(9,260),xytext=(7,240),
             arrowprops=dict(arrowstyle="->"))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("14_multiple_lines.png",dpi=300)
plt.show()
plt.close()

print("="*60)
print("REVISED MATPLOTLIB MASTER PROGRAM 2 COMPLETED")
print("""
Charts Covered
--------------
1. Pie Chart
2. Box Plot
3. Stem Plot
4. Step Plot
5. Error Bar
6. Stack Plot
7. Fill Between
8. Subplots
9. Multiple Line Plot

Best Practices
--------------
* Use figsize and dpi for clarity.
* Always label axes and add a title.
* Prefer legends when multiple datasets exist.
* Use grid() to improve readability.
* Save figures with savefig() before show().
* Use tight_layout() to avoid clipping.
* Call close() after each figure in long scripts.
""")
print("="*60)
