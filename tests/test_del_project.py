from model.project import Project
import random


def test_delete_project_by_id(app, config, db):
    if len(db.get_project_list()) == 0:
        app.project.create_project(Project(name="first_project"))
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    username = config['webadmin']['username']
    password = config['webadmin']['password']
    new_project = app.soap.mc_projects(username, password)
    assert len(old_project) - 1 == len(new_project)


