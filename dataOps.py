"""This file for data comparison or misillinious operations.
As an example, 'istanbul bahçelievler şirinevler mah 27.02.2022 13.01.14.csv' and 'istanbul bakırköy ataköy 2 kısım 26.02.2022 23.03.37.csv' files will be used."""

#import required libraries
import pandas as pd
from YemekSepeti import YemekSepeti
# to get information about using this class, write this commend:
# 'help(YemekSepeti)'


help(YemekSepeti)


# Read and concatinate csv files

df1 = pd.read_csv("istanbul bakırköy ataköy 2 kısım 26.02.2022 23.03.37.csv", sep=",", index_col=False)
df2 = pd.read_csv("istanbul bahçelievler şirinevler mah 27.02.2022 13.01.14.csv", sep=",", index_col=False)


# Review these  Datasets

df1.info
df1.describe()
df1.isnull().sum()
df1.head(7)
df1.tail(7)


df2.info
df2.describe()
df2.isnull().sum()
df2.head(7)
df2.tail(7)

# We do not fill empty lines since they refere Yemek Sepeti curriers


# Compare these datasets
# Concatinate
df_full = pd.concat([df1,df2], axis=0)

# Group
df_group = df_full.groupby('location')

df_group.describe(include="all")

df_group.min()
df_group.max()

