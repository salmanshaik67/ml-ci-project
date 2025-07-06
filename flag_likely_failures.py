import pickle

tests_info = [
    {'name': 'test_login', 'prev_failures': 0, 'time_of_day': 0, 'flaky': 0},
    {'name': 'test_api_status', 'prev_failures': 1, 'time_of_day': 1, 'flaky': 0},
    {'name': 'test_ui_render', 'prev_failures': 3, 'time_of_day': 0, 'flaky': 1},
]

with open("failure_predictor.pkl", "rb") as f:
    model = pickle.load(f)

print("=== Predicting Likely Failures ===")
for test in tests_info:
    features = [[test['prev_failures'], test['time_of_day'], test['flaky']]]
    prediction = model.predict(features)[0]
    if prediction == 1:
        print(f"⚠️ Likely failure: {test['name']}")
    else:
        print(f"✅ Likely pass: {test['name']}")
