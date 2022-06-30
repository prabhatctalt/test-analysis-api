from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Analysis():
    import pandas as pd

    filepath = request.args.get('filepath')


    if not filepath:
        return '<h2>Please Specify a Filepath by Adding : <i>?filepath=_filepath_</i> at the End of the URL.</h2>'
    elif '.csv' in filepath:
        data = pd.read_csv(filepath)
    elif '.xlsx' in filepath:
        data = pd.read_excel(filepath)
    else:
        return '<h2>Invalid File Format! Only .csv and .xlsx files are Accepted!</h2>'
    
    resString = ''
    resString += ('<h1>DATA SAMPLE</h1>')
    resString += "<br>" + data.head().to_html() + "<br>"

    resString += ('<h1>DATA DESCRIPTION</h1>')
    resString += (f'<h3>This Data has Total of {data.shape[1]} Columns and {data.shape[0]} Observations.</h3>')
    resString += "<br>" + round(data.describe().T, 2).to_html() + "<br>"
    return resString

if __name__ == '__main__':
    app.run(debug=True, port=5000)