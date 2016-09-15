function renderTodos(tasks) {
  console.log(tasks);
  tasks.forEach(function(task) {
    var $task = $("<li class='list-group-item todo-item" +
      (task.done ? "done" : "") + "'>" +
      "<input type='checkbox' " + (task.done ? "checked" : "") + ">" +
      task.content + "</li>");

    $task.attr('id', task.id);

    $task.find('input[type=checkbox]').click(function(event) {
      var done = $(this).is(':checked');
      if (done) {
        markDone(this.attr('id'));
      } else {
        markUndone(this.attr('id'));
      }
    });

    $("#todo-items").append($task);
  });
}

function getTodos() {
  $.get('/tasks', function(data) {
    renderTodos(data.tasks);
  });
}

function createTodo(content) {
  $.post('/tasks', {content: content}, function(data) {
    renderTodos(data.tasks);
  });
}

function markDone(id) {
  $.post("/tasks/"+id+"/done", function(data) {
    renderTodos(data.tasks);
  });
}

function markUndone(id) {
  $.post("/tasks/"+id+"/undone", function(data) {
    renderTodos(data.tasks);
  });
}



getTodos();
