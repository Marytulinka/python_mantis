from model.project import Project


def test_add_new_project(app, config):
    username = config['webadmin']['username']
    password = config['webadmin']['password']
    old_project = app.soap.mc_projects(username, password)
    project = Project(name="project_name")
    if len(old_project) != 0:
        app.project.open_project_page()
        app.project.push_create_button()
    app.project.create_project(project)
    new_project = app.soap.mc_projects(username, password)
    assert len(old_project) + 1 == len(new_project)
