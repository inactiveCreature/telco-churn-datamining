"""
Unit tests for src/utils.py.

Run with: pytest tests/
"""

import sys
import os
import pandas as pd
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from utils import (
    gini_impurity,
    entropy,
    information_gain,
    bucket_tenure,
    clean_total_charges,
    support,
    confidence,
)


class TestGiniImpurity:
    def test_pure_set_is_zero(self):
        assert gini_impurity([1, 1, 1, 1]) == 0.0

    def test_balanced_binary_is_half(self):
        assert gini_impurity([0, 0, 1, 1]) == pytest.approx(0.5)

    def test_known_example(self):
        # 2 "Yes" out of 3, 1 "No" out of 3 -> 1 - (2/3)^2 - (1/3)^2
        labels = ["Yes", "Yes", "No"]
        expected = 1 - (2 / 3) ** 2 - (1 / 3) ** 2
        assert gini_impurity(labels) == pytest.approx(expected)

    def test_empty_input(self):
        assert gini_impurity([]) == 0.0


class TestEntropy:
    def test_pure_set_is_zero(self):
        assert entropy([1, 1, 1]) == 0.0

    def test_balanced_binary_is_one(self):
        assert entropy([0, 0, 1, 1]) == pytest.approx(1.0)

    def test_empty_input(self):
        assert entropy([]) == 0.0


class TestInformationGain:
    def test_perfect_split_gives_max_gain(self):
        # Parent: 50/50 mixed. Split perfectly separates the classes.
        parent = [0, 0, 1, 1]
        left = [0, 0]
        right = [1, 1]
        gain = information_gain(parent, left, right, impurity_fn=gini_impurity)
        # Parent gini = 0.5, children are pure (gini=0) -> gain = 0.5
        assert gain == pytest.approx(0.5)

    def test_useless_split_gives_zero_gain(self):
        # Split doesn't change the class proportions at all
        parent = [0, 0, 1, 1]
        left = [0, 1]
        right = [0, 1]
        gain = information_gain(parent, left, right, impurity_fn=gini_impurity)
        assert gain == pytest.approx(0.0)


class TestBucketTenure:
    def test_buckets_assigned_correctly(self):
        s = pd.Series([0, 5, 12, 13, 30, 50, 70])
        result = bucket_tenure(s)
        expected = ["0-12", "0-12", "0-12", "13-24", "25-48", "49-60", "61-72"]
        assert list(result.astype(str)) == expected


class TestCleanTotalCharges:
    def test_blank_strings_become_zero(self):
        df = pd.DataFrame({"TotalCharges": ["29.85", " ", "108.15"]})
        cleaned = clean_total_charges(df)
        assert cleaned["TotalCharges"].tolist() == [29.85, 0.0, 108.15]

    def test_does_not_mutate_original(self):
        df = pd.DataFrame({"TotalCharges": ["29.85", " "]})
        clean_total_charges(df)
        # original column should still be the raw string dtype
        assert df["TotalCharges"].dtype == object


class TestSupportConfidence:
    def test_support_basic(self):
        mask = [True, True, False, False]
        assert support(mask) == pytest.approx(0.5)

    def test_support_empty(self):
        assert support([]) == 0.0

    def test_confidence_basic(self):
        # antecedent occurs in txns 0,1,2; both antecedent+consequent occur in 0,1
        antecedent = [True, True, True, False]
        both = [True, True, False, False]
        assert confidence(antecedent, both) == pytest.approx(2 / 3)

    def test_confidence_zero_antecedent_support(self):
        antecedent = [False, False]
        both = [False, False]
        assert confidence(antecedent, both) == 0.0
