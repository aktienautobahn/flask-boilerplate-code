from app import app

@app.route('/')
def home():
    return "Welcome to the Flask News API!"

@app.route('/news')
def news():
    # Example static news content
    return "Breaking News: Flask powers simple API services efficiently!"
