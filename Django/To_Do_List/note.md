


(To_Do_List) bash-3.2$ mkdir static
(To_Do_List) bash-3.2$ mkdir templates
(To_Do_List) bash-3.2$ mkdir templates/pages
(To_Do_List) bash-3.2$ mkdir templates/todos
(To_Do_List) bash-3.2$ mkdir static/css
(To_Do_List) bash-3.2$ mkdir static/js
(To_Do_List) bash-3.2$ touch static/js/main.js
(To_Do_List) bash-3.2$ touch static/css/site.css

setting up templates and html pages
setup setting.py
setut urls.py and views.py

create urls.py for todo app
- make the path show a list of todo
    - go create a method to list todo in views.py
    - test and make sure that it showings

- create a models in models.py
    - makemigrations
    - migrate
    - python manage.y createsuperuser
    - create username, password, email
    - test admin panel
    - create a class of Todo in models.py
        - title field = charfield
        - text field = textfield
        - status of completion = boolean
        - created_at = Datetimefield (auto_now_add = True)
        - completed_at = DateTimeField(blank = True, null=True)
        - task_duration = DateTimeField(blank = True, null=True)
        - CREATE A TODO_TYPE TUPLES
            - define the datatype for todo_type
        - create a method in this class def __str_(self): return self.title





