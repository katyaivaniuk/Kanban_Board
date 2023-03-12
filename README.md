# Kanban_Board

Link to the Loom recording: https://www.loom.com/share/8ef8cd69595c4ac58fc0ddf68fa7fd70

## Templates Folder:
1. base.html: contains the standard structure of the website, such as the header, footer, and navigation bar, since it is the information that should be displayed on each page. Hence, it allows other templates to inherit from it, override it and reduce code duplication.
2. home.html: contains the structure of the home page of the website, which is divided into two parts: the right part (65% of the screen) of it contains the image of how the Kanban Board looks like so that the user can get to know the idea behind better; the left part (35% of the screen) contains the description of the Kanban board and its benefits. 
3. login.html: contains the structure for the "Your Kanban" page (login), which allows you to input the email and password to be successfully redirected to the Kanban board. If there are any errors linked to the form fields (unrecognized email, wrong password), they are displayed alongside the rendered form fields, which are produced using the Jinja2 templating engine.
4. register.html: contains the structure for the "Register" page, which allows you to input the first name, last name, email, and password to be successfully registered on the website. The form is rendered using the Jinja2 templating engine, and if any errors are associated with the form fields, they are also displayed. When the form is submitted, the data is sent to the server using the POST method, and the Flask app handles the form data to create a new user account.
5. kanban_layout.html: contains the structure for the kanban board page that is divided into three columns: "To Do," "In Progress," and "Completed." This page includes three forms "Add task," "Move task," and "Delete task." The implementation of these forms was designed in the following way: the form for adding tasks was in the "To do" column, the form for moving tasks was in the "In Progress" column, and the form for deleting tasks was in the "Completed" column. When the tasks are added to the "To do" column, they construct an unordered list of tasks. The user can move a task to a different column by selecting the task from a drop-down menu in the "In progress" column and selecting one of the three available columns from a drop-down menu to move it to. To delete the task, it should be in a "Completed" column, and the user can quickly type it in the form and delete it. 


## Python files: 
**app.py - primary python file containing the following routes:**
1. /: a page that gives the overarching idea of what the Kanban board is, and explains the benefits behind it (home page).
2. /register: a page that allows users to register by providing their first and last name, email, and password. 
3. /login: a page that allows users to log in to the Kanban board by providing their email and password.
4. /kanban_board: the main page that displays the Kanban board with tasks organized in three states: "To Do," "In Progress," and "Completed."
5. /add_task: handles the submission of the form that allows users to add tasks to an unordered list. When the form is submitted, the task is added to the "to do" state of the Kanban board and added tasks are displayed in the form of an unordered list.
6. /move_task: handles the submission of the form that allows users to move tasks between the three states of the Kanban board (“to do”, “in progress”, “completed”). To ensure that the user can move any task, there is one form that contains a select input listing all the tasks in the three states which are automatically inputted in it when a task is added. After the user selects a task and a new state (which is another selection form), the selected task is moved to the specified state.
7. /delete_task: handles the submission of the form that allows users to delete tasks. When the form is submitted, the task selected by the user is deleted from the "completed" state of the Kanban board since it is “already finished by the user”.


**forms.py - python file that incorporates Flask-WTF extension allowing for WTForms’ integration, which includes automatic form generation and CSRF protection. (Flask-WTF — Flask-WTF Documentation (1.0.x), n.d.)**

1. The Login class: creates a form with fields for an email address and password. It validates that the email is not empty and is in the proper email format and that the password is not empty (uses fields such as StringField, PasswordField, and SubmitField along with validators such as InputRequired and Email).

2. The Register class: creates a form with fields for a first name, last name, email, and password. It validates that the first and last names are not empty, that the email is not empty and is in the proper email format, and that the password is not empty (uses fields such as StringField, PasswordField, and SubmitField along with validators such as InputRequired and Email).


**app_test.py - Python file carrying out unit test**
1. test_add_task(): this test was designed to check the “add” functionality of the Kanban board. It sends a POST request to the /add_task endpoint with the name of the task “Task 1” and the status “to do”, and further we check if the response from the server side contains the bytes “Task 1”. 
2. test_delete_task(): this test was designed to check the “delete” functionality of the Kanban board. It sends a POST request to the /delete_task endpoint containing the information about the task that should be deleted and its status after its addition to the Kanban board. If the task was deleted, then it shouldn’t be in any columns, and therefore, in the response data. 
3. test_move_task(): this test was designed to check the “move” functionality of the Kanban board. For the moving part to happen, we need to add the task first by sending the POST request to the /add_task endpoint, and further send a POST request to the /move_task endpoint, which will move the task from “to do” to “in progress”. We further check if the response status code was 200 ensuring the success of the task movement, and we check if the task is indeed in a new column. 
4. test_move_task_2(): this test was designed to check the “move” functionality of the Kanban board. For the moving part to happen, we need to add the task first by sending the POST request to the /add_task endpoint, and further sending a POST request to the /move_task endpoint, which will move the task from “in progress” to “completed”. We further check if the response status code was 200 ensuring the success of the task movement, and we check if the task is indeed in a new column. 
5. test_move_task_not_in_there(): this test was designed to check the “move” functionality of the Kanban board of the non-existent task “Imaginary Task”. For the moving part to happen, we added “Task 5” first by sending the POST request to the /add_task endpoint, and further sending a POST request to the /move_task endpoint, which will move the task from “to do” to “complete”. We further check if the response status code was 200 ensuring the success of the task movement, and we check if the non-existent “Imaginary Task” is in there (this should throw an error shown in the picture below, so to avoid having it I used self.assertNotIn)

6. test_register_login(): this test was designed to check the “registration”, and “login” functionality of the Kanban board. Since I did not work with the dataset (SQLAlchemy), I simply created a list with 3 users. Hence, it was crucial to check if people who are registering can be further stored in the list and successfully log in. For the registration to happen, we sent a POST request to the /register endpoint with information like first name, last name, email, and password, and further sent a POST request to the ‘/login endpoint with the new user email and password. Afterward, we check if the response status code is 200, which would indicate that the login after the registration of the new user was successful. 



## Static Folder:
1. delete.png: picture for the “delete” button
2. kanban.png: picture for the home page (visual representation of the kanban board)
3. style.css: file containing all the CSS code used for the styling of the web application based on the classes, IDs, and specific elements. The main colors used are Alice blue and dark blue. 
