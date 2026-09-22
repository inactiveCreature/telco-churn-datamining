"""
Reusable helper functions for the Telco churn analysis.

Kept separate from the notebook so the core logic is testable (see tests/test_utils.py)
and reusable if this analysis is ever extended or reused on a different dataset.
"""

import numpy as np
import pandas as pd


def gini_impurity(labels):
    """
    Compute the Gini impurity of a set of class labels.

    Gini = 1 - sum(p_i^2), where p_i is the proportion of class i.
    A pure set (all one class) has Gini = 0. A perfectly balanced binary
    set has Gini = 0.5.

    Parameters
    ----------
    labels : array-like
        A sequence of class labels (e.g. a pandas Series or list of 0/1, or strings).

    Returns
    -------
    float
        The Gini impurity, between 0 and (1 - 1/n_classes).
    """
    labels = pd.Series(labels)
    if len(labels) == 0:
        return 0.0
    proportions = labels.value_counts(normalize=True)
    return 1 - np.sum(proportions ** 2)


def entropy(labels):
    """
    Compute the Shannon entropy of a set of class labels.

    Entropy = -sum(p_i * log2(p_i)), where p_i is the proportion of class i.
    A pure set has entropy 0. A balanced binary set has entropy 1.

    Parameters
    ----------
    labels : array-like
        A sequence of class labels.

    Returns
    -------
    float
        The entropy in bits.
    """
    labels = pd.Series(labels)
    if len(labels) == 0:
        return 0.0
    proportions = labels.value_counts(normalize=True)
    proportions = proportions[proportions > 0]  # avoid log2(0)
    return -np.sum(proportions * np.log2(proportions))


def information_gain(parent_labels, left_labels, right_labels, impurity_fn=gini_impurity):
    """
    Compute the information gain of a binary split.

    Gain = impurity(parent) - weighted_average(impurity(left), impurity(right))

    Parameters
    ----------
    parent_labels : array-like
        Labels before the split.
    left_labels, right_labels : array-like
        Labels in each branch after the split.
    impurity_fn : callable, default gini_impurity
        Either gini_impurity or entropy.

    Returns
    -------
    float
        The information gain. Higher is better (the split reduced impurity more).
    """
    n = len(parent_labels)
    n_left, n_right = len(left_labels), len(right_labels)
    if n == 0:
        return 0.0

    parent_impurity = impurity_fn(parent_labels)
    weighted_child_impurity = (
        (n_left / n) * impurity_fn(left_labels) +
        (n_right / n) * impurity_fn(right_labels)
    )
    return parent_impurity - weighted_child_impurity


def bucket_tenure(tenure_series):
    """
    Bucket a numeric tenure-in-months column into labelled groups.

    Bins: 0-12, 13-24, 25-48, 49-60, 61-72 months.

    Parameters
    ----------
    tenure_series : pandas.Series
        Numeric tenure values (months).

    Returns
    -------
    pandas.Series
        Categorical series with the bucket labels.
    """
    bins = [0, 12, 24, 48, 60, 72]
    labels = ["0-12", "13-24", "25-48", "49-60", "61-72"]
    return pd.cut(tenure_series, bins=bins, labels=labels, include_lowest=True)


def clean_total_charges(df, column="TotalCharges"):
    """
    Fix the well-known TotalCharges data quality issue in the Telco dataset:
    the column is read as a string/object because a handful of new customers
    (tenure = 0) have blank values instead of 0.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe containing the column.
    column : str, default "TotalCharges"
        Name of the column to clean.

    Returns
    -------
    pandas.DataFrame
        A copy of df with the column converted to numeric and missing values
        filled with 0.
    """
    df = df.copy()
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df[column] = df[column].fillna(0)
    return df


def support(itemset_mask):
    """
    Compute the support of an itemset: the fraction of transactions containing it.

    Parameters
    ----------
    itemset_mask : array-like of bool
        Boolean mask, one entry per transaction, True if the transaction contains the itemset.

    Returns
    -------
    float
        Support value between 0 and 1.
    """
    itemset_mask = np.asarray(itemset_mask)
    if len(itemset_mask) == 0:
        return 0.0
    return itemset_mask.mean()


def confidence(antecedent_mask, both_mask):
    """
    Compute the confidence of a rule antecedent -> consequent.

    Confidence = support(antecedent AND consequent) / support(antecedent)

    Parameters
    ----------
    antecedent_mask : array-like of bool
        True where the transaction contains the antecedent.
    both_mask : array-like of bool
        True where the transaction contains both antecedent and consequent.

    Returns
    -------
    float
        Confidence value between 0 and 1. Returns 0 if the antecedent never occurs.
    """
    antecedent_support = support(antecedent_mask)
    if antecedent_support == 0:
        return 0.0
    return support(both_mask) / antecedent_support
