# data pre-processing

# import libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # nicer plots

# 1. load the data using script folder path
script_dir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(script_dir, 'fish_data.csv')
df = pd.read_csv(csv_path)

# strip column names (remove spaces, if any)
df.columns = df.columns.str.strip()

# 2. initial exploration
print("First 5 rows:")
print(df.head())

print("\ndata info:")
print(df.info())

print("\nmissing values per column:")
print(df.isnull().sum())

# 3. clean / preprocess

# drop duplicates
n_before = df.shape[0]
df = df.drop_duplicates()
n_after = df.shape[0]
print(f"\ndropped {n_before - n_after} duplicate rows.")

# drop rows with weight <= 0
df = df[df['weight'] > 0]

# convert numeric columns to proper type
df['length'] = pd.to_numeric(df['length'], errors='coerce')
df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
df['w_l_ratio'] = pd.to_numeric(df['w_l_ratio'], errors='coerce')
df = df.dropna(subset=['length', 'weight', 'w_l_ratio'])

# 4. use all species
df_filtered = df.copy()
print(f"\nDataset shape (all species): {df_filtered.shape}")

# 5. descriptive statistics

desc_stats = df_filtered.describe()
print("\nDescriptive statistics (numeric):")
print(desc_stats)

species_counts = df_filtered['species'].value_counts()
print("\nspecies counts:")
print(species_counts)

grouped = df_filtered.groupby('species').agg({
    'weight': ['mean', 'std', 'min', 'max'],
    'length': ['mean', 'std'],
    'w_l_ratio': ['mean', 'std']
})
print("\ngrouped statistics by species:")
print(grouped)

# 6. charts / visualizations

# bar chart: count of each species
plt.figure(figsize=(10, 6))
sns.countplot(data=df_filtered, x='species', order=species_counts.index)
plt.title('count of fish by species')
plt.xlabel('species')
plt.ylabel('count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# pie chart: species proportion
plt.figure(figsize=(6, 6))
species_counts.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('species distribution')
plt.ylabel('')
plt.show()

# scatter plot: length vs weight by species
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_filtered, x='length', y='weight', hue='species', s=100, alpha=0.7)
plt.title('length vs weight by species')
plt.xlabel('length')
plt.ylabel('weight')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)  # move legend outside
plt.tight_layout()
plt.show()

# scatter plot: w_l_ratio vs weight
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_filtered, x='w_l_ratio', y='weight', hue='species', s=100, alpha=0.7)
plt.title('w/l Ratio vs Weight by Species')
plt.xlabel('w/l Ratio')
plt.ylabel('weight')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.tight_layout()
plt.show()

# heatmap: correlation matrix
plt.figure(figsize=(8, 6))
corr = df_filtered.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('correlation matrix')
plt.show()

# boxplot: weight distribution by species
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_filtered, x='species', y='weight')
plt.title('distribution of fish weight by species')
plt.xlabel('species')
plt.ylabel('weight')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
