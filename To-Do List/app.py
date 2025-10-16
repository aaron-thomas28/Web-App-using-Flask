from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='.', static_folder='.')

# Store tasks in memory
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index_route():
    global tasks
    if request.method == 'POST':
        # Add new task
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('index_route'))

    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index_route'))

if __name__ == '__main__':
    app.run(debug=True)
