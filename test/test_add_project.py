from model.project import Project



def test_add_project(app, db):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    app.session.login("administrator", "root")
    old_list = app.soap.get_list_project(username, password)
    name = Project(name="test")
    app.project.open_create_project_page()

    app.project.fill_project_form(name)

    app.project.add_new_project()

    old_list.append(name)
    new_list = app.soap.get_list_project(username, password)
    print(new_list)
    # assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)