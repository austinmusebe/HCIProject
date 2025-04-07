from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'
db = SQLAlchemy(app)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resource_name = request.form.get('resource-name')
        resource_url = request.form.get('resource-url')
        resource_description = request.form.get('resource-description')
        resource_category = request.form.get('resource-category')

        # Basic form validation
        if not resource_name or not resource_url or not resource_description or not resource_category:
            return jsonify({'message': 'All fields are required!'}), 400 #Return a bad request

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