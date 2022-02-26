from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from main import bg_sub, feature_extract
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:9876@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class leaf_database(db.Model):
	__tablename__ = 'leaf_database'
	id = db.Column(db.Integer, primary_key = True)
	leaf_name = db.Column(db.String(100))
	med_use = db.Column(db.String(1000))
	place = db.Column(db.String(100))
	nut_cont = db.Column(db.String(1000))
	other_name = db.Column(db.String(1000))
	season = db.Column(db.String(1000))
	soil_condi = db.Column(db.String(1000))
	other_use = db.Column(db.String(1000))
	scien_name = db.Column(db.String(1000))
	charac = db.Column(db.String(1000))
	side_effects = db.Column(db.String(1000))

	def __init__(self, id, leaf_name, med_use, place, nut_cont, other_name, season, soil_condi, other_use, scien_name, charac, side_effects):
		self.id = id
		self.leaf_name = leaf_name
		self.med_use = med_use
		self.place = place
		self.nut_cont = nut_cont
		self.other_name = other_name
		self.season = season
		self.soil_condi = soil_condi
		self.other_use = other_use
		self.scien_name = scien_name
		self.charac = charac
		self.side_effects = side_effects

@app.route('/', methods = ["POST", "GET"])

def home():
	#if request.method == "POST":
	return render_template('index.html')

@app.route('/upload.html', methods = ["POST", "GET"])

def upload():
	if request.method == "POST":
		f = request.files.get("file", False)
		if f:
			basepath = os.path.dirname(__file__)
			filename = secure_filename(f.filename)		
			file_path = os.path.join(basepath, 'static', 'img', filename)
			f.save(file_path)
			result = feature_extract(bg_sub(file_path))
			filename = f.filename
			leaf_var = leaf_database.query.filter_by(leaf_name = result).first()
			return render_template('success.html', result = result, leaf1 = leaf_var)
	return render_template('upload.html')

@app.route('/text.html', methods = ["POST", "GET"])

def text():
	if request.method == "POST":
		result = request.form['name']
		result = result.upper()
		leaf_var = leaf_database.query.filter_by(leaf_name = result).first_or_404(description='There is no data with {}'.format(result))
		return render_template('success.html', result = result, leaf1 = leaf_var)
	return render_template('text.html')

if __name__ == '__main__':
	app.run(debug = True)