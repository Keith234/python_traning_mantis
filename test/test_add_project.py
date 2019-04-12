from modal.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_projects = app.project.get_project_list()
    added_contact = (Project(name="TTTT", description="For start"))
    app.project.create(added_contact)
    new_projects = app.project.get_project_list()
    old_projects.append(added_contact)
    assert len(old_projects) == len(new_projects)
