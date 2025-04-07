from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'
db = SQLAlchemy(app)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class MoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(20), nullable=False)
    reasons = db.Column(db.String(255))  # Store reasons as a comma-separated string
    entry = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow) #Add a timestamp.
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breath.html')
def breath():
    return render_template('breath.html')

@app.route('/moodLog.html', methods=['GET', 'POST'])
def mood_log():
    if request.method == 'POST':
        mood = request.form.get('mood')
        reasons_list = request.form.getlist('reasons')  # Get a list of selected reasons
        reasons = ','.join(reasons_list)  # Convert list to comma-separated string
        entry = request.form.get('entry')

        new_mood_log = MoodLog(mood=mood, reasons=reasons, entry=entry)
        db.session.add(new_mood_log)
        db.session.commit()

        return jsonify({'message': 'Mood log saved successfully!'}) #Return a json response.
    return render_template('moodLog.html')

@app.route('/resources.html', methods=['GET', 'POST'])
def resources():
    if request.method == 'POST':
        resource_name = request.form.get('resource-name')
        resource_url = request.form.get('resource-url')
        resource_description = request.form.get('resource-description')
        resource_category = request.form.get('resource-category')

        if not resource_name or not resource_url or not resource_description or not resource_category:
            return jsonify({'message': 'All fields are required!'}), 400

        new_resource = Resource(
            name=resource_name,
            url=resource_url,
            description=resource_description,
            category=resource_category,
        )

        db.session.add(new_resource)
        db.session.commit()

        return jsonify({'message': 'Resource submitted successfully!'})

    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)

@app.route('/get_resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    resource_list = [{'id': res.id, 'name': res.name, 'url': res.url, 'description': res.description, 'category': res.category} for res in resources]
    return jsonify(resource_list)

if __name__ == '__main__':
    app.run(debug=True)