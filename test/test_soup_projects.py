from modal.project import Project
import random



def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_projects = app.soap.get_project_from_soup()
    added_contact = (Project(name="Dina", description="For start"))
    app.project.create(added_contact)
    new_projects = app.soap.get_project_from_soup()
    old_projects.append(added_contact)
    assert len(old_projects) == len(new_projects)



def test_del_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    if len(app.project.get_project_list()) == 0:
        added_contact = (Project(name="FirstSecond", description="For start"))
        app.project.create(added_contact)
    old_projects = app.soap.get_project_from_soup()
    deleted_project = random.choice(old_projects)
    app.project.delete_project(deleted_project.name)
    new_projects = app.soap.get_project_from_soup()
    old_projects.remove(deleted_project)
    assert len(old_projects) == len(new_projects)