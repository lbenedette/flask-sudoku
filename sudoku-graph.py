from app import app

app.config['SECRET_KEY'] = 'This key is secret'

app.run(debug=True)

