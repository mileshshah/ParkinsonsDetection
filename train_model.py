import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)
    df = df.drop(columns=['name'])
    X = df.drop(columns=['status'])
    y = df['status']
    return X, y

def split_data(X, y):
    split_index = len(X) // 2
    X_train = X.iloc[:split_index]
    y_train = y.iloc[:split_index]
    X_test = X.iloc[split_index:]
    y_test = y.iloc[split_index:]
    return X_train, y_train, X_test, y_test

def train_and_evaluate(X_train, y_train, X_test, y_test):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, zero_division=0)
    return accuracy, report, len(X_train), len(X_test)

if __name__ == "__main__":
    X, y = load_and_preprocess('parkinsons data.csv')
    X_train, y_train, X_test, y_test = split_data(X, y)
    accuracy, report, train_len, test_len = train_and_evaluate(X_train, y_train, X_test, y_test)

    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(report)
    print(f"\nTraining on {train_len} rows, Testing on {test_len} rows.")
