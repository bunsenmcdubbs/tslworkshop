$("#create-todo button").click(function(event) {
  event.preventDefault();
  var taskContent = $("#create-todo input[type=text]").val();
  createTodo(taskContent);
});

getTodos();

// ================
// HELPER FUNCTIONS
// ================

/*
 * Take JSON task array and create DOM elements and render them on the page
 */
function renderTodos(tasks) {
  console.log(tasks);
  var $tasks = tasks.map(function(task) {
    var $task = $("<li class='list-group-item todo-item'>" +
      "<input type='checkbox'>" +
      task.content + "</li>");

    if (task.done) {
      $task.addClass('done');
      $task.find('input[type=checkbox]')[0].checked = true;
    }

    $task.attr('id', task.id);

    $task.find('input[type=checkbox]').click(function(event) {
      var done = $(this).is(':checked');
      var id = $(this).parent().attr('id');

      if (done) {
        markDone(id);
      } else {
        markUndone(id);
      }
    });

    return $task;
  });

  $("#todo-items").html($tasks);
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
