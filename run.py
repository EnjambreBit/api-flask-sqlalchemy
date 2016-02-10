from app import app

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.run(debug=False)
