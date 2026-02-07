# Parkinson's Disease Data Analysis

This project is focused on building a machine learning model to predict Parkinson's disease using voice measurement data.

## Project Structure

- `train_model.py`: The main script for loading data, training a Random Forest model, and evaluating its performance.
- `test_train_model.py`: Unit tests for the data processing functions in `train_model.py`.
- `parkinsons data.csv`: The dataset used by the application, containing various voice measurements.

## Getting Started

### Prerequisites
Install the required dependencies:
```bash
pip install pandas scikit-learn
```

### Running the Model
To train the model and view the results, execute:
```bash
python3 train_model.py
```

### Running Tests
To run the unit tests, execute:
```bash
python3 test_train_model.py
```

## Model Summary

The model uses a **RandomForestClassifier** trained on the first half of the dataset (97 rows) and tested on the second half (98 rows).

### Performance
- **Accuracy:** 78.57%
- **Classification Report:**
  - **Class 1 (Parkinson's):** Precision 0.80, Recall 0.96
  - **Class 0 (Healthy):** Precision 0.67, Recall 0.25

The model shows high sensitivity in detecting Parkinson's disease, making it a potentially useful tool for preliminary screening based on voice data.
