import logging

from taskcat._cfn_lint import Lint as TaskCatLint
from taskcat._config import Config
from taskcat.exceptions import TaskCatException

LOG = logging.getLogger(__name__)


class Lint:
    """checks CloudFormation templates for issues using cfn-python-lint"""

    def __init__(self, input_file: str, project_root: str = "./", strict: bool = False):
        """
        :param input_file: path to project config or CloudFormation template
        :param project_root: base path for project
        :param strict: fail on lint warnings as well as errors
        """
        config = Config(
            project_config_path=input_file,
            project_root=project_root,
            create_clients=False,
        )
        lint = TaskCatLint(config, strict)
        errors = lint.lints[1]
        lint.output_results()
        if errors or not lint.passed:
            raise TaskCatException("Lint failed with errors")
