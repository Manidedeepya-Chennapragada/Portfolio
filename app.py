from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

# Project Routes
@app.route('/project/mlinsightbot')
def mlinsightbot():
    return render_template('projects/mlinsightbot.html')

@app.route('/project/energy-analysis')
def energy_analysis():
    return render_template('projects/energy_analysis.html')

@app.route('/project/fraud-detection')
def fraud_detection():
    return render_template('projects/fraud_detection.html')

if __name__ == '__main__':
    app.run(debug=True)
