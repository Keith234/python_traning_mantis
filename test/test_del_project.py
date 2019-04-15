import random
from modal.project import Project

def test_del_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    if len(app.soap.get_project_from_soup()) == 0:
        added_contact = (Project(name="FirstSecond", description="For start"))
        app.project.create(added_contact)
    old_projects = app.soap.get_project_from_soup()
    deleted_project = random.choice(old_projects)
    app.project.delete_project(deleted_project.name)
    new_projects = app.soap.get_project_from_soup()
    old_projects.remove(deleted_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
