from main import recommend_movies

def test_recommendation():
    test_title = 'Inception'
    recommendations = recommend_movies(test_title)
    print(f"Recommendations for '{test_title}': {recommendations}")

if __name__ == '__main__':
    test_recommendation()
