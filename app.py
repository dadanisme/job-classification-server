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


def laila_converter(x):
    match x:
        case 0:
            return 'Data Analyst'
        case 1:
            return 'Programmer'
        case 2:
            return 'Network'
        case _:
            return 'nothing matched'


@app.route('/', methods=['POST'])
def predict():
    answers = request.get_json()

    import pickle
    import pandas as pd

    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

    test_data = [answers]
    test_df = pd.DataFrame(test_data)

    y_respon_predict = loaded_model.predict(test_df)

    return {
        'result': convert_to_string(y_respon_predict[0])
    }


@app.route('/laila', methods=['POST'])
def predict():
    answers = request.get_json()

    import pickle
    import pandas as pd

    loaded_model = pickle.load(open('modelrf56.sav', 'rb'))

    test_data = [answers]
    test_df = pd.DataFrame(test_data)

    y_respon_predict = loaded_model.predict(test_df)

    return {
        'result': laila_converter(y_respon_predict[0])
    }
