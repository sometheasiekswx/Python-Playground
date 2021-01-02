from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index of Flask'


@app.route('/get_similar_courses', methods=['GET', 'POST'])
def get_similar_courses():
    course = request.args.get('course')
    return f'Courses Similar to {course}'


print('Flask running in docker!!')
