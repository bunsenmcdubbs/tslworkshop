from flask import Flask, json, send_from_directory, request
app = Flask(__name__)

## global static id to ensure that all our Tasks have unique ids
taskId = -1

class Task():
    ## this is the contructor
    def __init__(self, content):
        global taskId ## this tells python to use the global variable we declared and assigned above
        taskId = taskId + 1
        self.id = taskId
        self.content = content
        self.done = False

    ## "to string", makes printing Task objects more human-readable in your terminal
    ## similar to __str__(), they have subtle differences
    def __repr__(self):
        return 'id:%i done:%s content:%s' % (self.id, self.done, self.content)

    ## Where is this used? What is it doing?
    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'done': self.done
        }

Tasks = {}

## this is totally optional and just for demonstration purposes, remove if you wish
testTask = Task("MAGICCCCCCCC")
Tasks[testTask.id] = testTask

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name="World"):
    return "Hello %s!" % name

@app.route("/")
@app.route("/<path:filepath>")
def index(filepath="index.html"):
    return send_from_directory("client", filepath)

@app.route("/tasks", methods=["GET"])
def getTasks():
    allTasks = Tasks.values()
    print allTasks
    return json.jsonify(tasks=[t.serialize() for t in allTasks])

@app.route("/tasks", methods=["POST"])
def addTask():
    content = request.form["content"]
    newTask = Task(content)
    Tasks[newTask.id] = newTask
    return getTasks()

## this isn't actually ever used because our client code is missing the
## code that sends a request to this route... do you want to try implementing
## the client code (HTML/JavaScript)?!?!
@app.route("/tasks/<int:taskId>", methods=["DELETE"])
def removeTask(taskId):
    del Tasks[taskId]
    return getTasks()

@app.route("/tasks/<int:taskId>/done", methods=["POST"])
def markDone(taskId):
    Tasks[taskId].done = True
    return getTasks()

@app.route("/tasks/<int:taskId>/undone", methods=["POST"])
def markUndone(taskId):
    Tasks[taskId].done = False
    return getTasks()

## Actually start the server!!!
if __name__ == "__main__":
    app.run(debug=True)
