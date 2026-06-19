def binary_encoder(X):
    X = X.copy()

    mappings = {
        "gender" : {"Male":1, "Female":0},
        "Partner" : {"Yes" : 1, "No": 0},
        "Dependents" : {"Yes" : 1, "No": 0},
        "PhoneService" : {"Yes" : 1, "No": 0},
        "PaperlessBilling" : {"Yes" : 1, "No": 0}
    }

    for col, mapping in mappings.items():
        X[col] = X[col].map(mapping)

    return X