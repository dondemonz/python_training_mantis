# from model.project import Project
import time


class ProjectHelper:
    def __init__(self, app):
        self.app = app


    def open_create_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        # time.sleep(5)
        wd.find_element_by_link_text("Manage Projects").click()
        # time.sleep(5)
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        time.sleep(5)

    def fill_project_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='name']").click()
        wd.find_element_by_xpath("//input[@name='name']").clear()
        wd.find_element_by_xpath("//input[@name='name']").send_keys("test")
        time.sleep(5)

    def add_new_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        self.click_first_project()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(5)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()


    def click_first_project(self):
        wd = self.app.wd
        if
        # wd.find_element_by_xpath("//tr[4]/td/a").click()
        time.sleep(5)


        # check = wd.find_element_by_xpath("//*[@id=" + id + "]")
        # check.click()
        # pass