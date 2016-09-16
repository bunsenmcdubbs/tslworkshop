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

## This will be our fake database. We will insert tasks as values and use taskIds as keys
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
    print "NOT YET IMPLEMENTED"
    ## get the "content" of the new todo item from the body of the request
    ## create a new task
    ## add new task to the `Tasks` dictionary, keyed by id
    return getTasks() ## return all tasks

## this isn't actually ever used because our client code is missing the
## code that sends a request to this route... do you want to try implementing
## the client code (HTML/JavaScript)?!?!
@app.route("/tasks/<int:taskId>", methods=["DELETE"])
def removeTask(taskId):
    print "NOT YET IMPLEMENTED"
    ## delete the task from the Tasks dictionary
    return getTasks() ## return all tasks

@app.route("/tasks/<int:taskId>/done", methods=["POST"])
def markDone(taskId):
    print "NOT YET IMPLEMENTED"
    ## set done=True for the task in Tasks (use the taskId as the key) 
    return getTasks() ## return all tasks

@app.route("/tasks/<int:taskId>/undone", methods=["POST"])
def markUndone(taskId):
    print "NOT YET IMPLEMENTED"
    ## mark the task as not done
    return getTasks() ## return all tasks

## Actually start the server!!!
if __name__ == "__main__":
    app.run(debug=True)
