
"""
Filter numerical values using NumPy Boolean conditions
and Boolean indexing.
"""

import numpy as np


def filter_values(data, threshold):
    """Return values above, below, and equal to a threshold."""

    return {
        "Above threshold": data[data > threshold],
        "Below threshold": data[data < threshold],
        "Equal to threshold": data[data == threshold],
        "Greater than or equal": data[data >= threshold],
        "Less than or equal": data[data <= threshold],
    }


def display_results(data, threshold, results):
    """Display the original data and filtered results."""

    print("=" * 60)
    print("                 NUMPY DATA FILTERING")
    print("=" * 60)

    print("\nOriginal NumPy array:", data)
    print("Array shape:", data.shape)
    print("Data type:", data.dtype)
    print("Selected threshold:", threshold)

    print("\nFILTERED RESULTS")
    print("-" * 60)

    for label, values in results.items():
        print(f"{label:<24}: {values}")

    print("\nBOOLEAN CONDITION EXAMPLE")
    print("-" * 60)
    print(f"Condition (data > {threshold}):")
    print(data > threshold)

    print("\nThe Boolean condition creates a Boolean array.")
    print("Boolean indexing returns the values that match it.")
    print("\nAnalysis completed successfully.")


def main():
    # Sample data: student marks out of 100.
    data = np.array(
        [35, 48, 50, 56, 62, 70, 75, 82, 90, 95],
        dtype=int
    )

    print("Available thresholds:", [40, 50, 70, 80])

    try:
        user_input = input(
            "\nEnter a threshold (press Enter for 50): "
        ).strip()

        threshold = 50 if not user_input else float(user_input)

        if not np.isfinite(threshold):
            raise ValueError("Threshold must be a finite number.")

    except ValueError:
        print("Invalid input. Please enter a valid numerical threshold.")
        return

    results = filter_values(data, threshold)
    display_results(data, threshold, results)

    # Demonstrate filtering at multiple thresholds.
    print("\nCOMPARISON ACROSS DIFFERENT THRESHOLDS")
    print("-" * 60)

    for value in [40, 50, 70, 80]:
        filtered = data[data > value]
        print(f"Values greater than {value:<3}: {filtered}")


if __name__ == "__main__":
    main()
