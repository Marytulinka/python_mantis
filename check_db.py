
def test_project_list(app, db):
    db_list = db.get_project_list()
    print("OK")
