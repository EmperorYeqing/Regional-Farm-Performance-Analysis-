# %% [markdown]
# # Project 02: Regional Agricultural Performance Analysis
# 
# ## Business Scenario
# 
# Aim: Understand Business problem, hired by a national agricultural board 
# 
# Objectives: They want to understand:
# 1. Which Region performs best ?
# 2. which region use land most efficiently?
# 3. Which crop generated the most revenue?
# 4. which region should receive additional investment?
# 5. which region need intervention?

# %% [markdown]
# ## STEP 01: Import

# %%
#Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %% [markdown]
# ## STEP 02: Load the dataset

# %%
df = pd.read_csv(r"regional_farm_data.csv")
df

# %% [markdown]
# ## STEP 03: Understand the dataset

# %%
df.head()
df.info()
df.describe()

# %% [markdown]
# The dataset have 5 columns and 8 rows of data with each row describing farm data (crop, farm size,Yield per kg and revenue)of each region.there are 2 columns with string value and 3 columns with integers. 
# from the observation of the dataset, no missing values were detected and no obvious inconsistencies were observed.

# %% [markdown]
# ## STEP 04: Create KPIs - Feature Engineering

# %% [markdown]
# ### KPI 1: Yield per Hectare
# Yield Per Hectare = Yield_Kg / Farm_Size_Ha

# %%
df["Yield_per_Ha"] = df["Yield_Kg"] / df["Farm_Size_Ha"]
df

# %% [markdown]
# created my first KPI which is Yield_per_Ha to determine the Yield Per hectare of Land on each region

# %% [markdown]
# ### KPI 2: Revenue per Hectare
# Revenue Per Hectare = Revenue/ Farm_Size_Ha

# %%
df["Revenue_per_Ha"] = df["Revenue"] / df["Farm_Size_Ha"]
df

# %% [markdown]
# created my second KPI which is Revenue_per_Ha to determine the Revenue generated Per hectare of Land on each region

# %% [markdown]
# ## STEP 05: Exploratory Data Analysis (EDA)

# %% [markdown]
# ### First Analysis: Regional Performance
# Questions
# 1. Which region generated the highest revenue?
# 2. Which region generated the least revenue?

# %%
df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

# %% [markdown]
# Answers:
# 
# 1. South region generated the highest revenue of 12500000
# 2. West region generated the least revenue of 8700000

# %% [markdown]
# ### Second Analysis: Regional Efficiency
# 
# Questions
# 1. Which region has the highest land-use efficiency?
# 2. Which region has the lowest land-use efficiency?

# %%
df.groupby("Region")["Revenue_per_Ha"].mean().sort_values(ascending=False)

# %% [markdown]
# Answers:
# 1. South region has the highest land-use efficiency
# 2. East region has the lowest land-use efficiency

# %% [markdown]
# ### Third Analysis: Crop Performance
# 
# Questions
# 1. most Profitable crop?
# 2. Least Profitable crop?

# %%
df.groupby("Crop")["Revenue"].sum().sort_values(ascending=False)

# %% [markdown]
# Answers:
# 1. Rice is the most profitable crop with highest revenue generation of 11800000
# 2. Soybean is the least profitable crop with the lowest revenue generation of 7700000

# %% [markdown]
# ## STEP 07: Corellative Analysis -  Farm Productivity

# %%
df[["Farm_Size_Ha", "Yield_per_Ha"]].corr()

# %% [markdown]
# correlation = 1 - Perfect positive relationship
# 
# correlation = -0.31 weak negative relationship

# %% [markdown]
# Correlation Analysis to determine relationship between Farm_Size_Ha and Yield_per_Ha:
# 
#         Answer: From the analysis result, it's clear that there is a weak or no relationship between Farm_Size_Ha and Yield_per_Ha

# %% [markdown]
# ## STEP 07: Visualization

# %% [markdown]
# ### Revenue by Region

# %%
df.groupby("Region")["Revenue"].sum().plot(kind="bar")
plt.title("Total Revenue by Region")
plt.show()

# %% [markdown]
# ### Efficiency by Region

# %%
df.groupby("Region")["Revenue_per_Ha"].mean().plot(kind="bar")
plt.title("Average Revenue per Hectare by Region")
plt.show()

# %% [markdown]
# ## STEP 08: Key Insights
# 1. South Region Performs the best in revenue generation and land-use efficiency, despite having the same total Farm_Size as the North region
# 2. North Region performance is the second-best in revenue generation and land-use efficiency, just behind the South region
# 3. West region generated the least revenue
# 4. East region has the lowest land-use efficiency
# 5. Although the West region generated the least revenue, it land-use efficiency is higher than the East region
# 6. Rice is the most profitable crop with highest revenue generation
# 7. Soybean is the least profitable crop having the least revenue generation
# 8. Maize performs better than Cassava in terms of revenue generation
# 9. distribution of planted crop varies from North-south to West-East 

# %% [markdown]
# ## STEP 09: Executive Recommendation

# %% [markdown]
# Based on the Analysis done within the limit of available dataset, i would like to make the following recommendation:
# 1. South Region deserve the most investment among all region, especially in rice and maize Cultivation
# 2. more investment should also be made in the North region  especially in maize and rice cultivation
# 3. both South and North region especially South region should be studied to determine what drives the success of cultivated crops  in the region and also if such practices can be replicated in other region and crop types.
# 4. Rice and Maize should be promoted as they have the highest revenue generation and land-use efficiency.
# 5. both West and East region especially the West needs improvement especially what factors is affecting their performance. experiment with other crop type like rice and maize can also be done to see if there will be improvement.


