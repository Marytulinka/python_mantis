from model.project import Project


def test_add_new_project(app, db):
    old_project = db.get_project_list()
    project = Project(name="first@_project")
    if len(old_project) != 0:
        app.project.open_project_page()
        app.project.push_create_button()
    app.project.create_project(project)
    new_project = db.get_project_list()
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
