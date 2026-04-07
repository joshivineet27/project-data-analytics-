# ===============================
# Nainital Tourism Analytics Project
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# 1. Load Dataset
# ===============================

df = pd.read_csv(r"C:\Users\jvine\OneDrive\Pictures\Documents\projects\nenital project\Nainital_Tourism_2020_2025_5000_Rows.csv")

print("First 20 rows:")
print(df.head(20))

print("\nShape of dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ===============================
# 2. Year Wise Tourism Analysis
# ===============================

yearly = df.groupby("Year")["Tourist_Count"].mean()
print("\nYearly Tourism Trend:")
print(yearly)

yearly.plot(kind="bar")
plt.title("Yearly Tourist Trend")
plt.xlabel("Year")
plt.ylabel("Average Tourist Count")
plt.show()


# ===============================
# 3. Monthly Tourism Pattern
# ===============================

monthly = df.groupby("Month")["Tourist_Count"].mean()
print("\nMonthly Tourism Pattern:")
print(monthly)

monthly.plot(kind="bar")
plt.title("Monthly Tourism Pattern")
plt.xlabel("Month")
plt.ylabel("Average Tourist Count")
plt.show()


# ===============================
# 4. Weekend vs Weekday Tourism
# ===============================

weekend = df.groupby("Weekend")["Tourist_Count"].mean()
print("\nWeekend Tourism:")
print(weekend)

weekend.plot(kind="bar")
plt.title("Weekend vs Weekday Tourism")
plt.show()


# ===============================
# 5. Weather Impact
# ===============================

plt.scatter(df["Temperature"], df["Tourist_Count"])
plt.xlabel("Temperature")
plt.ylabel("Tourist Count")
plt.title("Temperature vs Tourism")
plt.show()

plt.scatter(df["Rainfall"], df["Tourist_Count"])
plt.xlabel("Rainfall")
plt.ylabel("Tourist Count")
plt.title("Rainfall vs Tourism")
plt.show()


# ===============================
# 6. Festival Impact
# ===============================

festival = df.groupby("Festival")["Tourist_Count"].mean()
print("\nFestival Impact:")
print(festival)

festival.plot(kind="bar")
plt.title("Festival Impact on Tourism")
plt.show()


# ===============================
# 7. Hotel Occupancy Analysis
# ===============================

plt.scatter(df["Tourist_Count"], df["Hotel_Occupancy_Rate"])
plt.xlabel("Tourist Count")
plt.ylabel("Hotel Occupancy Rate")
plt.title("Tourist vs Hotel Occupancy")
plt.show()


# ===============================
# 8. Correlation Analysis
# ===============================

corr = df.corr(numeric_only=True)

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.show()

print("\nFactors affecting Tourism:")
print(corr["Tourist_Count"].sort_values(ascending=False))


# ===============================
# 9. Top Tourism Locations
# ===============================

location = df.groupby("Location")["Tourist_Count"].sum().sort_values(ascending=False)

print("\nTop Locations:")
print(location)

location.plot(kind="bar")
plt.title("Top Tourism Locations")
plt.xlabel("Location")
plt.ylabel("Total Tourist Count")
plt.show()


# ===============================
# 10. Holiday Impact
# ===============================

holiday = df.groupby("Holiday")["Tourist_Count"].mean()

print("\nHoliday Impact:")
print(holiday)

holiday.plot(kind="bar")
plt.title("Holiday Impact on Tourism")
plt.show()


# ===============================
# 11. Google Search vs Tourism
# ===============================

plt.scatter(df["Google_Search_Index"], df["Tourist_Count"])
plt.xlabel("Google Search Index")
plt.ylabel("Tourist Count")
plt.title("Google Search vs Tourism")
plt.show()


# ===============================
# 12. Marketing Spend
# ===============================

plt.scatter(df["Marketing_Spend"], df["Tourist_Count"])
plt.xlabel("Marketing Spend")
plt.ylabel("Tourist Count")
plt.title("Marketing vs Tourism")
plt.show()


# ===============================
# 13. Safety Impact
# ===============================

plt.scatter(df["Safety_Index"], df["Tourist_Count"])
plt.xlabel("Safety Index")
plt.ylabel("Tourist Count")
plt.title("Safety vs Tourism")
plt.show()


# ===============================
# 14. Covid Impact
# ===============================

plt.scatter(df["Covid_Cases"], df["Tourist_Count"])
plt.xlabel("Covid Cases")
plt.ylabel("Tourist Count")
plt.title("Covid Impact on Tourism")
plt.show()


# ===============================
# 15. Tourist Stay Pattern
# ===============================

plt.scatter(df["Tourist_Count"], df["Avg_Stay_Days"])
plt.xlabel("Tourist Count")
plt.ylabel("Average Stay Days")
plt.title("Tourist Stay Pattern")
plt.show()


# ===============================
# 16. Distribution Analysis
# ===============================

sns.boxplot(x=df["Tourist_Count"])
plt.title("Tourist Count Distribution")
plt.show()

plt.hist(df["Tourist_Count"], bins=30)
plt.title("Tourist Count Distribution")
plt.xlabel("Tourist Count")
plt.ylabel("Frequency")
plt.show()


# ===============================
# 17. Linear Regression Model
# ===============================

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = df[[
"Temperature",
"Rainfall",
"Festival",
"Holiday",
"Marketing_Spend",
"Google_Search_Index"
]]

y = df["Tourist_Count"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nLinear Regression Accuracy:", r2_score(y_test, pred))


# ===============================
# 18. Advanced ML Model
# ===============================

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

X = df[[
"Temperature",
"Rainfall",
"Festival",
"Holiday",
"Weekend",
"Fuel_Price",
"Google_Search_Index",
"Traffic_Index",
"Marketing_Spend",
"Event_Count",
"Transport_Cost_Index",
"Inflation_Rate",
"Safety_Index"
]]

y = df["Tourist_Count"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestRegressor(n_estimators=200, random_state=42)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nRandom Forest Results")
print("R2 Score:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))
print("MSE:", mean_squared_error(y_test, pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))


# ===============================
# 19. Save Clean Dataset
# ===============================

df.to_csv("Nainital_Tourism_Cleaned.csv", index=False)

print("\nClean dataset saved successfully.")

# import pandas as pd 
# import numpy as np 
# df = pd.read_csv("nenital project\Nainital_Tourism_2020_2025_5000_Rows.csv")
# print(df.head(20))
# print(df.shape)
# print(df.columns) # all colomn 
# print(df.info()) #no. of row and colomn 
# print(df.describe())# statics summury 
# print(df.isnull().sum()) # handel mising value 

# print(df.duplicated().sum()) 

# #Year wise tourism analysis
# yearly = df.groupby("Year")["Tourist_Count"].mean()
# print(yearly)

# import matplotlib.pyplot as plt

# yearly.plot(kind="bar")
# plt.title("Yearly Tourist Trend")
# plt.xlabel("Year")
# plt.ylabel("Average Tourist Count")
# plt.show()

# #Month wise tourism
# monthly = df.groupby("Month")["Tourist_Count"].mean()
# print(monthly)

# monthly.plot(kind="bar")
# plt.title("Monthly Tourism Pattern")
# plt.xlabel("Month")
# plt.ylabel("Average Tourist Count")
# plt.show()

# #Weekend vs Weekday
# weekend = df.groupby("Weekend")["Tourist_Count"].mean()
# print(weekend)

# weekend.plot(kind="bar")
# plt.title("Weekend vs Weekday Tourism")
# plt.show()

# #Temperature vs Tourism
# plt.scatter(df["Temperature"], df["Tourist_Count"])
# plt.xlabel("Temperature")
# plt.ylabel("Tourist Count")
# plt.title("Temperature vs Tourism")
# plt.show()


# #Rainfall Impact
# plt.scatter(df["Rainfall"], df["Tourist_Count"])
# plt.xlabel("Rainfall")
# plt.ylabel("Tourist Count")
# plt.title("Rainfall vs Tourism")
# plt.show()

# #Festival Impact
# festival = df.groupby("Festival")["Tourist_Count"].mean()
# print(festival)

# festival.plot(kind="bar")
# plt.title("Festival Impact on Tourism")
# plt.show()

# #Hotel Occupancy Analysis
# plt.scatter(df["Tourist_Count"], df["Hotel_Occupancy_Rate"])
# plt.xlabel("Tourist Count")
# plt.ylabel("Hotel Occupancy Rate")
# plt.show()

# #Correlation Analysis (VERY IMPORTANT)
# corr = df.corr(numeric_only=True)

# import seaborn as sns

# sns.heatmap(corr)
# plt.title("Correlation Matrix")
# plt.show()

# #Tourism ko sabse zyada kya affect karta hai
# print(corr["Tourist_Count"].sort_values(ascending=False))

# #Top 5 Tourism Locations
# location = df.groupby("Location")["Tourist_Count"].sum().sort_values(ascending=False)

# print(location)

# location.plot(kind="bar")
# plt.title("Top Tourism Locations")
# plt.xlabel("Location")
# plt.ylabel("Total Tourist Count")
# plt.show()

# #Holiday Impact
# holiday = df.groupby("Holiday")["Tourist_Count"].mean()
# print(holiday)

# holiday.plot(kind="bar")
# plt.title("Holiday Impact on Tourism")
# plt.show()

# # Google Search vs Tourism
# plt.scatter(df["Google_Search_Index"], df["Tourist_Count"])
# plt.xlabel("Google Search Index")
# plt.ylabel("Tourist Count")
# plt.title("Google Search vs Tourism")
# plt.show()

# # Marketing Spend Analysis
# plt.scatter(df["Marketing_Spend"], df["Tourist_Count"])
# plt.xlabel("Marketing Spend")
# plt.ylabel("Tourist Count")
# plt.title("Marketing vs Tourism")
# plt.show()

# # Safety Impact
# plt.scatter(df["Safety_Index"], df["Tourist_Count"])
# plt.xlabel("Safety Index")
# plt.ylabel("Tourist Count")
# plt.title("Safety vs Tourism")
# plt.show()

# # Covid Impact
# plt.scatter(df["Covid_Cases"], df["Tourist_Count"])
# plt.xlabel("Covid Cases")
# plt.ylabel("Tourist Count")
# plt.title("Covid Impact on Tourism")
# plt.show()

# # Average Stay Analysis
# plt.scatter(df["Tourist_Count"], df["Avg_Stay_Days"])
# plt.xlabel("Tourist Count")
# plt.ylabel("Average Stay Days")
# plt.title("Tourist Stay Pattern")
# plt.show()

# # Top Factors Affecting Tourism
# print(corr["Tourist_Count"].sort_values(ascending=False).head(10))

# # Important Insights Extract karo
# top_factors = corr["Tourist_Count"].sort_values(ascending=False)
# print("Top factors affecting tourism:\n")
# print(top_factors)

# # Tourist Trend Line Graph
# df_sorted = df.sort_values("Date")

# plt.figure(figsize=(10,5))
# plt.plot(df_sorted["Tourist_Count"])
# plt.title("Tourism Trend Over Time")
# plt.xlabel("Time")
# plt.ylabel("Tourist Count")
# plt.show()


# # Average Tourism by Location
# location_avg = df.groupby("Location")["Tourist_Count"].mean().sort_values(ascending=False)

# print(location_avg)

# location_avg.plot(kind="bar")
# plt.title("Average Tourism by Location")
# plt.xlabel("Location")
# plt.ylabel("Average Tourist Count")
# plt.show()

# # Box Plot
# sns.boxplot(x=df["Tourist_Count"])
# plt.title("Tourist Count Distribution")
# plt.show()

# # Histogram
# plt.hist(df["Tourist_Count"], bins=30)
# plt.title("Tourist Count Distribution")
# plt.xlabel("Tourist Count")
# plt.ylabel("Frequency")
# plt.show()

# # Tourism Prediction (Optional ML)

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# X = df[["Temperature","Rainfall","Festival","Holiday","Marketing_Spend","Google_Search_Index"]]

# y = df["Tourist_Count"]

# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# model = LinearRegression()

# model.fit(X_train,y_train)

# pred = model.predict(X_test)

# from sklearn.metrics import r2_score

# print("Model Accuracy:", r2_score(y_test,pred))


# # ===============================
# # Machine Learning Model Improve
# # ===============================

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# # ===============================
# # 1. Features Select karna
# # ===============================

# # yeh sab factors tourism ko affect kar sakte hain
# X = df[[
# "Temperature",
# "Rainfall",
# "Festival",
# "Holiday",
# "Weekend",
# "Fuel_Price",
# "Google_Search_Index",
# "Traffic_Index",
# "Marketing_Spend",
# "Event_Count",
# "Transport_Cost_Index",
# "Inflation_Rate",
# "Safety_Index"
# ]]

# # Target variable
# y = df["Tourist_Count"]


# # ===============================
# # 2. Train Test Split
# # ===============================

# X_train, X_test, y_train, y_test = train_test_split(
# X, y, test_size=0.2, random_state=42
# )


# # ===============================
# # 3. Feature Scaling
# # ===============================

# scaler = StandardScaler()

# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)


# # ===============================
# # 4. Random Forest Model
# # ===============================

# model = RandomForestRegressor(n_estimators=200, random_state=42)

# model.fit(X_train, y_train)


# # ===============================
# # 5. Prediction
# # ===============================

# pred = model.predict(X_test)


# # ===============================
# # 6. Model Evaluation
# # ===============================

# print("R2 Score:", r2_score(y_test, pred))

# print("MAE:", mean_absolute_error(y_test, pred))

# print("MSE:", mean_squared_error(y_test, pred))

# print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))

# df.to_csv("Nainital_Tourism_Cleaned.csv", index=False)


