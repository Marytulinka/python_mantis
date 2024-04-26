from model.project import Project


def test_delete_project_by_id(app):
    id = 14
    app.project.delete_project_by_id(id)
