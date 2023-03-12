from flask import Flask, request, render_template
from forms import Register, Login
from flask import session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myrandomlygeneratedkey'


users = [
            {"id": 1, "first_name": "Kateryna", 'last_name':'Ivaniuk', "email": "katherina.ivaniuk@gmail.com", "password": "mypassword"},
            {"id": 2, "first_name": "User1", 'last_name':'Random1', "email": "user1@gmail.com", "password": "user1password"},
            {"id": 3, "first_name": "User2", 'last_name':'Random2', "email": "user2@gmail.com", "password": "user2password"}
        ]

kanban = {
    "to do": [],
    "in progress": [],
    "completed": []
}

@app.route('/')
def home():
    """
    Renders a home page file written in HTML that 
    has the layout of the main page (left part of the display is the picture, and 
    the right one is the description of the Kanban board)

    """
    return render_template("home.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Function that handles the submission of the registration form with the included methods 'POST' and 'GET' using Flask-WTF. 

    When the server receives submission of the registration form (on POST request), it validates the data, 
    creates a new user, and renders the registration form and displays notification messages depending on
    whether user registered succesfully, or is already registered.

    When user accesses the page (on GET request), the registration form is displayed with the input fields: 
    (First name, Last name, Email and Password)

    """
    form = Register()
    if form.validate_on_submit():
        email = form.email.data
        if any(user["email"] == email for user in users):
            return render_template("register.html", form=form, notification="You already have an account. Please proceed to the login page")

        new_user = {"id": len(users)+1, 
                    "first_name": form.first_name.data, 
                    "last_name": form.last_name.data, 
                    "email": form.email.data, 
                    "password": form.password.data}

        users.append(new_user)
        return render_template("register.html", notification = "You Successfully registered!")
    return render_template("register.html", form = form)



@app.route("/login", methods=["POST", "GET"])
def login():
    '''
    Function that handles the submission of the login form with the included methods 'POST' and 'GET' using Flask-WTF. 
    When user accesses the page (on GET request), the login form is displayed with the input fields: (Email and Password)

    When the server receives submission of the login form (on POST request), it validates the data, checks is the user exists, 
    (whether credentials are correct), and renders the login form and displays notification message if the info was incorrect, or 
    navigates to the kanban board. 
    
    '''
    form = Login()
    if form.validate_on_submit():
        user = None
        for u in users:
            if u['email'] == form.email.data and u['password'] == form.password.data:
                user = u
                break
        if user is None:
            return render_template("login.html", form = form,  notification = "Please Try Again. Your password/email is incorrect")
        else:
            session['user'] = user
            return render_template("kanban_layout.html", kanban=kanban)
    return render_template("login.html", form = form)



@app.route("/kanban_board")
def kanban_board():
    '''
    Renders a layout page file written in HTML that has the structure for the Kanban board
    (with stages "To Do", "In progress", "Completed")
    '''
    return render_template("kanban_layout.html", kanban=kanban)




@app.route('/add_task', methods=['POST'])
def add_task():
    '''
    Function that handles the addition of new tasks to the Kanban board utilizing POST method.
    It receives the name of the task, and the state of the task (on POST request), which is used to place the task into it, 
    and it further renders kanban_layout template to display changes on Kanban board. 

    '''
    added_task = request.form['added_task']
    task_state = request.form['status']

    if added_task in kanban[task_state]:
        return render_template('kanban_layout.html', kanban=kanban, notification='Task already exists!')

    kanban[task_state].append(added_task)
    return render_template('kanban_layout.html', kanban=kanban)



@app.route('/delete_task', methods=['POST'])
def delete_task():
    '''
    Function that handles the deletion of tasks in the Kanban board, and specifically section "Completed" 
    utilizing POST method. It receives the name of the task, and the state of the task (on POST request), 
    and it further removes the task from the state, and renders kanban_layout template to display changes on Kanban board. 
    If the user wants to delete non-existent task, it will state "There is no such task to delete "

    '''
    deleted_task = request.form['deleted_task']
    task_state = request.form['status']

    if deleted_task in kanban[task_state]:
        kanban[task_state].remove(deleted_task)
        return render_template('kanban_layout.html', kanban=kanban)
    else:
        return "There is no such task to delete "
    


@app.route('/move_task', methods=['POST'])
def move_task():
    '''
    Function that handles the moving of tasks in the Kanban board utilizing "POST" method. 
    It receives the name of the task, and the state where it should be moved to, 
    finds its current state, and moves to the new one. It renders kanban_layout template to display changes on Kanban board. 
    The template itself creates two drop-down menus: one with all the tasks in all states, and the other one with the 3 states. 
    '''
    moving_task = request.form['moving_task']
    updated_state = request.form['status']
    found= False

    for state, task in kanban.items():
        if moving_task in kanban[state]:
            found = True
            kanban[state].remove(moving_task)
            kanban[updated_state].append(moving_task)
            break
    if not found:
        return "Task not found in any state"
    return render_template('kanban_layout.html',kanban=kanban)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port = 3000)


