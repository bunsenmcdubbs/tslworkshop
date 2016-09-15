from flask import Flask, json, send_from_directory, request
app = Flask(__name__)

taskId = -1
class Task():
    ## this is the contructor
    def __init__(self, content):
        global taskId ## this tells python to use the global variable we declared and assigned above
        taskId = taskId + 1
        self.id = taskId
        self.content = content
        self.done = False

    ## "to string", makes printing Task objects more human-readable
    ## similar to __str__(), they have subtle differences
    def __repr__(self):
        return '#%i %s' % (self.id, self.content) + (" <done>" if self.done else "")
    ##
    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'done': self.done
        }

Tasks = {}

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

if __name__ == "__main__":
    app.run(debug=True)
