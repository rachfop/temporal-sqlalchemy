async function addTask() {
    const taskTitle = document.getElementById('taskInput').value;
    try {
        const response = await fetch('/add_task', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: taskTitle }),
        });
        
        if (!response.ok) throw new Error("Network response was not ok");
        const data = await response.json();
        alert(data.message);
        document.getElementById('taskInput').value = '';
    } catch (error) {
        console.error('Error adding task:', error);
        alert('An error occurred while adding the task. Please try again.');
    }
}
function escapeHTML(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}


async function getAllTasks() {
    try {
        const response = await fetch('/get_all_tasks');
        if (!response.ok) throw new Error("Network response was not ok");
        
        const data = await response.json();
        const tasksListElement = document.getElementById('tasksList');
        tasksListElement.innerHTML = ""; // Clear existing rows

        data.tasks.forEach(task => {
            const statusText = task.completed ? "Completed" : "Incomplete";
            const completedClass = task.completed ? "completed-task" : "";
            const btnText = task.completed ? "Incomplete" : "Complete";
            const row = document.createElement('tr');
            row.className = completedClass;
            row.innerHTML = `
                <td>${escapeHTML(task.id)}</td>
                <td>${escapeHTML(task.title)}</td>
                <td>${escapeHTML(statusText)}</td>
                <td>
                    <button onclick="completeTask(${task.id}, event, this)" class="${completedClass}">${btnText}</button>
                </td>
            `;
            tasksListElement.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching all tasks:', error);
        alert('An error occurred while fetching tasks. Please try again.');
    }
}

async function completeTask(id, event, btnElement) {
    console.log("Updating task status for ID:", id);
    
    try {
        const response = await fetch(`/toggle_task/${id}`, { method: 'POST' });
        const data = await response.json();

        if (data.success) {
            alert('Task status updated successfully.');

            // Find the parent row of the clicked button
            const parentRow = btnElement.closest('tr');
            // Update the status text cell (assuming it's the third cell in the row)
            const statusCell = parentRow.cells[2];
            
            if (statusCell.textContent === "Completed") {
                statusCell.textContent = "Incomplete";
                btnElement.textContent = "Complete";
                parentRow.classList.remove("completed-task");
            } else {
                statusCell.textContent = "Completed";
                btnElement.textContent = "Incomplete";
                parentRow.classList.add("completed-task");
            }

        } else {
            // get all tasks called
            getAllTasks();
        }

    } catch (error) {
        console.error('Error updating task:', error);
        alert('An error occurred while updating the task status. Please try again.');
    }
}

async function getTaskById() {
    const taskId = document.getElementById('taskIdInput').value;
    try {
        const response = await fetch(`/get_task/${taskId}`);
        if (!response.ok) throw new Error("Network response was not ok");

        const data = await response.json();
        const outputElement = document.getElementById('singleTaskOutput');
        outputElement.innerHTML = ""; // Clear the current content

        if (data.success) {
            const statusText = data.completed ? "Completed" : "Incomplete";
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${escapeHTML(data.id)}</td>
                <td>${escapeHTML(data.title)}</td>
                <td>${escapeHTML(statusText)}</td>
            `;
            outputElement.appendChild(row);
        } else {
            // If task is not found or any other message is available
            const row = document.createElement('tr');
            row.innerHTML = `<td colspan="3">${escapeHTML(data.message)}</td>`;
            outputElement.appendChild(row);
        }

    } catch (error) {
        console.error('Error fetching task:', error);
        alert('An error occurred while fetching the task. Please try again.');
    }
}

