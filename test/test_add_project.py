

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_create_project_page()
    app.project.fill_project_form()
    app.project.add_new_project()

