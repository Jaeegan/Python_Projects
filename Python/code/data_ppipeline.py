# -*- coding: utf-8 -*-
"""
    A Data Preprocessing pipeline to handle missing values, standardize numeric features,
    remove outliners, and ensure easy replication of preprocessing steps on new datasets.
    
    Credits to resources by Aman Kharwal.
    Url: https://thecleverprogrammer.com/2023/06/19/data-preprocessing-pipeline-using-python/

Usage:
    ./data_preprocessing.py

Author:
    Joshua Gan - 26.06.2023
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def data_preprocessing_pipeline(df):
    # Identify numeric and categorical features
    num_features = df.select_dtypes(["float", "int"]).columns
    cat_features = df.select_dtypes(["object"]).columns

    print(
        f"This dataset contains {len(num_features)} numerical features with column names: {num_features}."
    )
    print(
        f"And {len(cat_features)} categorical features with column names: {cat_features}."
    )

    # Visualize missing values in the dataset
    print(df.head())
    df.isna().sum().plot(kind="bar")
    plt.title("Barplot of Missing Values")
    plt.xlabel("Features")
    plt.ylabel("Number of Missing Values")
    plt.xticks(rotation=45)
    plt.show()

    # Dealing with missing data:
    # 1. Drop missing values if they account for a small proportion, typically 5 percent of the dataset
    #
    #    threshold = len(df) * 0.05
    #    cols_to_drop = df.columns[df.isna().sum <= threshold]
    #    df.dropna(subset=cols_to_drop, inplace=True)
    #
    # 2. Impute with mean or median for numeric features and mode for categorical features
    #
    #    When feature has no specific groupings;
    #    df['numeric_feature'] = df['numeric_feature'] \
    #       .fillna(df['numeric_feature'].mean())
    #
    #    When feature has specifc groupings;
    #    grp_means = df.groupby('grouping')['numeric_feature'].mean()
    #    grp_means_dict = grp_means.to_dict()
    #    df['numeric_feature'] = df['numeric_feature'] \
    #       .fillna(df['numeric_feature']).map(grp_means_dict))

    # Handle missing values in numeric features
    df[num_features] = df[num_features].fillna(df[num_features].mean())

    # Detect and handle outliers in the numeric features using IQR
    for feature in num_features:
        Q1 = df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        df[feature] = np.where(
            (df[feature] < lower_bound) | (df[feature] > upper_bound),
            df[feature].mean(),
            df[feature],
        )

    # Normalize numeric features
    scaler = StandardScaler()
    scaler.fit_transform(df[num_features])
    df[num_features] = scaler.transform(df[num_features])

    # Handle missing values in categorical features
    df[cat_features] = df[cat_features].fillna(df[cat_features].mode().iloc[0])

    return df


# df = pd.read_csv("/Users/JG/Developer/data/statsio_data_preprocessing.csv")

# cleaned_df = data_preprocessing_pipeline(df)
# print(cleaned_df)
