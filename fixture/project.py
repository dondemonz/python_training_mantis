
class ProjectHelper:
    def __init__(self, app):
        self.app = app


    def open_create_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    """
    def fill_project_form(self, text):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='name']").click()
        wd.find_element_by_xpath("//input[@name='name']").clear()
        wd.find_element_by_xpath("//input[@name='name']").send_keys(text)
    """


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def add_new_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//*[@value = 'Delete Project']").click()
        wd.find_element_by_xpath("//*[@value = 'Delete Project']").click()

    def click_some_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//tr[4]/td/a").click()


    def select_project_by_id(self, id):
        wd = self.app.wd
        pr = ("//*[@href='manage_proj_edit_page.php?project_id=" + str(id) + "']")
        wd.find_element_by_xpath(pr).click()


