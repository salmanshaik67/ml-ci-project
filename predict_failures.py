import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    'test_name': ['test_login', 'test_api_status', 'test_ui_render'] * 10,
    'prev_failures': [1, 0, 2, 0, 1, 3, 0, 0, 1] * 3 + [2],
    'time_of_day': [0, 1, 0, 1, 1, 0, 0, 1, 0] * 3 + [1],
    'flaky': [0, 0, 1, 0, 1, 1, 0, 0, 1] * 3 + [1],
    'failed': [0, 0, 1, 0, 1, 1, 0, 0, 1] * 3 + [1],
}

df = pd.DataFrame(data)
X = df[['prev_failures', 'time_of_day', 'flaky']]
y = df['failed']

model = RandomForestClassifier()
model.fit(X, y)

with open("failure_predictor.pkl", "wb") as f:
    pickle.dump(model, f)
