from flask import Flask, request, jsonify
from main import recommend_movies

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the AI Movie Recommendation API!"

@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title')
    if not title:
        return jsonify({'error': 'Missing movie title'}), 400

    recommendations = recommend_movies(title)
    if not recommendations:
        return jsonify({'error': 'Movie not found'}), 404

    return jsonify({'recommended_movies': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
