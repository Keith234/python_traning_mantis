from modal.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_projects = app.soap.get_project_from_soup()
    added_contact = (Project(name="Tiana", description="For start"))
    app.project.create(added_contact)
    new_projects = app.soap.get_project_from_soup()
    old_projects.append(added_contact)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
