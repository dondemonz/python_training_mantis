from model.project import Project
import random

def test_delete_project(app, db):
    app.session.login("administrator", "root")
    if len(db.get_project_list()) == 0:
        app.project.open_create_project_page()
        app.project.fill_project_form()
        app.project.add_new_project()
    old_list = db.get_project_list()
    selected_p = random.choice(old_list)
    app.project.delete_project_by_id(selected_p.id)
    old_list.remove(selected_p)
    new_list = db.get_project_list()
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)