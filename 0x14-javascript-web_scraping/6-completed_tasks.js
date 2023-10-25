#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, resource, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const todosUser = JSON.parse(body);
  const completedTasks = {};
  for (const todo of todosUser) {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedTasks[userId]) { completedTasks[userId] += 1; } else { completedTasks[userId] = 1; }
    }
  }
  console.log(completedTasks);
});
