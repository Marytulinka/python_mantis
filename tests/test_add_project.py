from model.project import Project


def test_add_new_project(app):
    project = Project(name="test_from_tests")
    app.project.create_project(project)
