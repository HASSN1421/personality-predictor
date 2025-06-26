def convert_yes_no_columns(X):
    X = X.copy()
    yes_no_cols = ['Stage_fear', 'Drained_after_socializing']
    for col in yes_no_cols:
        if col in X.columns:
            X[col] = X[col].replace({'yes': 1, 'no': 0})
    return X