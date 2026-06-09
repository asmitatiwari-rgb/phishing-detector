import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("Dataset.csv")

# clean
df = df.dropna()

# IMPORTANT: separate label
y = df["label"]

# remove non-numeric + label
X = df.drop(columns=["label", "URL", "Domain", "FILENAME"], errors="ignore")

# keep only numeric features (safe ML training)
X = X.select_dtypes(include=['int64','float64'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    random_state=42
)

model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

joblib.dump(model, "phishing_model.pkl")

print("🔥 Advanced Model trained & saved")