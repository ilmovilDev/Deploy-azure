from flask import Blueprint, jsonify

main = Blueprint('routes', __name__)

@main.route('/', methods=['GET'])
def test_root():
    return jsonify({"message": "Hello word from Flask api!"}), 200