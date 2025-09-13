const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");

let tasks = []; // Array to hold task strings1

// Stage 3: DOM + Events
addTaskBtn.addEventListener("click", () => {
   const taskText = taskInput.value.trim(); 
   if (taskText === "") {
    alert("Please enter a task.");
    return;
   } 
   // Save the array
   tasks.push(taskText);

   // Clear input
   taskInput.value ="";

   // Re-render tasks
   renderTasks();
});

// Function to render tasks

function renderTasks() {
    taskList.innerHTML = ""; // clear previous

    tasks.forEach((task, index) => {
        const li = document.createElement("li");
        li.textContent = task;

    // Toggle task complete
        li.addEventListener("click", () => {
        li.classList.toggle("completed");
        });

        // Add delete buttton
        const delBtn = document.createElement("button");
        delBtn.textContent="Delete";
        delBtn.style.marginLeft = "10px";

        delBtn.addEventListener("click", function()  {
            tasks.splice(index, 1); // Remove task
            renderTasks();
        });

        li.appendChild(delBtn);
        taskList.appendChild(li);

    });
}