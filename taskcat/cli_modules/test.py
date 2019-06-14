from taskcat.config import Config

class Test:
    """
    Performs functional tests on CloudFormation templates.
    """

    @staticmethod
    def run(entry_point, project_root='./'):
        print("doing a run, yeah!")
        config = Config(entry_point, project_root=project_root)

    @staticmethod
    def resume(run_id):
        # do some stuff
        pass
