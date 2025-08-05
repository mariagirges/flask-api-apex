from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return jsonify([
        {"message": "مرحبًا من بايثون!", "value": 123}
    ])

if __name__ == '__main__':
    app.run()
