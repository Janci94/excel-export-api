from flask import Flask, request, jsonify
from data_layer import fetch_data_from_db
from logic_layer import calculate_sum
from file_export import export_to_excel

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    phrase = request.args.get('phrase')

    if phrase:
        data = fetch_data_from_db(phrase)
        if data:
            sum_data = calculate_sum(data)
            export_to_excel(sum_data, phrase)
            return jsonify(data), 200
        else:
            return jsonify({'error': 'No data found'}), 400
    else:
        return jsonify({'error': 'BadRequest'}), 400

if __name__ == '__main__':
    app.run(debug=True)
