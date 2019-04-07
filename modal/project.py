class Project:

    def __init__(self, project_name, description=None):
        self.project_name = project_name
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s, %s" % (self.project_name, self.description)
