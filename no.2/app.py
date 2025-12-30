from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient(
    "mongodb+srv://mrksrout_db_user:Mongo12345@cluster0.tlsegtu.mongodb.net/assignmentDB?retryWrites=true&w=majority"
)

db = client.assignmentDB
collection = db.students



@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']

            collection.insert_one({
                "name": name,
                "email": email
            })

            return render_template('success.html')

        except Exception as e:
            error = str(e)

    return render_template('form.html', error=error)



@app.route('/todo')
def todo_page():
    return render_template('todo.html')



@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    itemName = request.form['itemName']
    itemDescription = request.form['itemDescription']

    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })

    return "To-Do item stored successfully"



if __name__ == '__main__':
    app.run(debug=True)
