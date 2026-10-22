# NumPy Data Filtering

## Overview

This project demonstrates how to filter numerical values using NumPy Boolean conditions and Boolean indexing.

## Objectives

- Filter values above, below, or equal to a threshold.
- Understand Boolean arrays.
- Compare results across multiple thresholds.
- Accept a custom threshold from the user.

## Technologies Used

- Python 3
- NumPy
- Visual Studio Code

## Installation

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## Run the Project

```bash
python numpy_filtering.py
```

Enter a threshold when prompted or press Enter to use the default value of 50.

## Sample Dataset

`[35, 48, 50, 56, 62, 70, 75, 82, 90, 95]`

## Sample Results

For threshold 50:

- Above 50: `[56, 62, 70, 75, 82, 90, 95]`
- Below 50: `[35, 48]`
- Equal to 50: `[50]`

## Project Files

- `numpy_filtering.py` — Main Python program
- `requirements.txt` — Dependency information
- `analysis_report.md` — Results and analysis
- `project_report.pdf` — Formatted project report
- `screenshots/` — Project evidence

## Conclusion

This project illustrates how Boolean indexing makes it easy to select specific values from numerical arrays.
