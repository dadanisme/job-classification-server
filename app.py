from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


def convert_to_string(x):
    match x:
        case 0:
            return 'Big Data Science'
        case 1:
            return 'Programmer'
        case 2:
            return 'Network Specialist'
        case _:
            return 'nothing matched'


@app.route('/', methods=['POST'])
def predict():
    answers = request.get_json()

    import pickle
    import pandas as pd

    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

    test_data = [[4, 5, 4, 2, 3, 4, 1, 2, 5, 1, 2, 4]]
    test_df = pd.DataFrame(test_data)
    test_df

    y_respon_predict = loaded_model.predict(test_df)

    return {
        'result': convert_to_string(y_respon_predict[0])
    }
