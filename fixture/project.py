from modal.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def chenge_project_field_value(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.chenge_project_field_value("name", project.project_name)
        self.chenge_project_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath('//table[@class="width100"]//tr[@class="row-1"]'):
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[4].text
                self.project_cache.append(Project(project_name=name, description=description))
            for element in wd.find_elements_by_xpath('//table[@class="width100"]//tr[@class="row-2"]'):
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[4].text
                self.project_cache.append(Project(project_name=name, description=description))
        return list(self.project_cache)
