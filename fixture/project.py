from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def create_first_project(self, project):
        wd = self.app.wd
        self.fill_project_form(project)
        self.project_cache = None

    #  РАБОТАЕТ
    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        self.project_cache = None

    # РАБОТАЕТ
    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()

    # РАБОТАЕТ
    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='/mantisbt-1.2.20/manage_overview_page.php']").click()
        wd.find_element_by_link_text("Manage Projects").click()

    # РАБОТАЕТ
    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()

    # РАБОТАЕТ
    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None

    # def get_project_list(self):

