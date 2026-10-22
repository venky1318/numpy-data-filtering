# NumPy Data Filtering — Analysis Report

## 1. Project Overview

This project demonstrates numerical data filtering using NumPy. It identifies values that are greater than, less than, equal to, greater than or equal to, and less than or equal to a selected threshold.

## 2. Objective

- Create a NumPy array containing numerical values.
- Apply Boolean conditions to identify matching values.
- Use Boolean indexing to extract filtered results.
- Compare results across different thresholds.

## 3. Dataset

The sample dataset represents student marks out of 100.

`[35, 48, 50, 56, 62, 70, 75, 82, 90, 95]`

The array contains 10 numerical values.

## 4. Methodology

The program creates a NumPy array and accepts a numerical threshold from the user. If no value is entered, the program uses 50 as the default threshold.

NumPy comparison operators generate Boolean arrays. Boolean indexing then selects the values that satisfy each condition.

The program also repeats the greater-than filtering operation using thresholds 40, 50, 70, and 80.

## 5. Results

For a threshold of 50:

| Condition | Filtered values |
|---|---|
| Greater than 50 | [56, 62, 70, 75, 82, 90, 95] |
| Less than 50 | [35, 48] |
| Equal to 50 | [50] |
| Greater than or equal to 50 | [50, 56, 62, 70, 75, 82, 90, 95] |
| Less than or equal to 50 | [35, 48, 50] |

## 6. Boolean Indexing

Boolean indexing selects array elements according to a Boolean condition.

For example, `data > 50` creates a Boolean array in which each element indicates whether the corresponding mark exceeds 50. Using `data[data > 50]` returns only the matching values.

## 7. Threshold Comparison

Increasing the threshold generally reduces the number of values that satisfy a greater-than condition. This helps users examine different subsets of numerical data.

## 8. Applications

NumPy filtering can be used to identify students who pass a specified mark threshold, sales that exceed a target, measurements outside a specified range, or numerical records meeting business criteria.

## 9. Conclusion

The project demonstrates how NumPy Boolean conditions and Boolean indexing can filter numerical datasets efficiently. It also shows how changing a threshold changes the selected values.
