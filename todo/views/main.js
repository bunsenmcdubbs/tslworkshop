function renderTodos(todos) {
  todos.map(function(todo) {
    return $("<li class='list-group-item todo-item'>" +
        "<input type='checkbox' checked='" + todo.done === true + "'>" +
        todo.content + "</li>");
  });
}

function getTodos() {
  $.get('/tasks', function(data) {
    console.log(data);
  });
}

getTodos();
