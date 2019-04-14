import random
from modal.project import Project

def test_del_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    if len(app.project.get_project_list()) == 0:
        added_contact = (Project(name="FirstSecond", description="For start"))
        app.project.create(added_contact)
    old_projects = app.project.get_project_list()
    deleted_project = random.choice(old_projects)
    app.project.delete_project(deleted_project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(deleted_project)
    assert len(old_projects) == len(new_projects)
