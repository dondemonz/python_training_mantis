

def test_delete_project(app):
    app.session.login("administrator", "root")
    """
    if len(db.get_contacts_list()) == 0:
        app.project.open_create_project_page()
        app.project.fill_project_form()
        app.project.add_new_project()
    """
    app.project.delete_project()