import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score


# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("datasets/kidney.csv")

# ==========================
# CLEAN DATA
# ==========================

df.replace(
    ["?", "\t?", "nan", "None", ""],
    np.nan,
    inplace=True
)

# ==========================
# TARGET
# ==========================

df["classification"] = (
    df["classification"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["classification"] = df["classification"].replace({
    "ckd": 1,
    "ckd\t": 1,
    "notckd": 0,
    "not ckd": 0
})

df = df[df["classification"].isin([0, 1])]
df["classification"] = df["classification"].astype(int)

# ==========================
# KEEP ONLY UI FEATURES
# ==========================

columns_needed = [
    "age",
    "bp",
    "sg",
    "al",
    "su",
    "bgr",
    "bu",
    "sc",
    "sod",
    "pot",
    "hemo",
    "pcv",
    "wc",
    "rc",
    "classification"
]

df = df[columns_needed]

# ==========================
# NUMERIC CONVERSION
# ==========================

for col in df.columns:
    if col != "classification":
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# ==========================
# IMPUTE MISSING
# ==========================

imputer = SimpleImputer(
    strategy="median"
)

X = df.drop("classification", axis=1)

X = pd.DataFrame(
    imputer.fit_transform(X),
    columns=X.columns
)

y = df["classification"]

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# TRAIN MODEL
# ==========================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# ACCURACY
# ==========================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n==============================")
print("Kidney Accuracy:", round(accuracy, 4))
print("==============================")

# ==========================
# SAVE
# ==========================

joblib.dump(
    model,
    "backend/ml_models/disease_prediction/kidney_model.pkl"
)

print("✅ Kidney model saved")