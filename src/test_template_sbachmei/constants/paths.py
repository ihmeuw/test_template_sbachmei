from pathlib import Path

import test_template_sbachmei
from test_template_sbachmei.constants import metadata

BASE_DIR = Path(test_template_sbachmei.__file__).resolve().parent

ARTIFACT_ROOT = Path(
    f"/mnt/team/simulation_science/pub/models/{metadata.PROJECT_NAME}/artifacts/"
)
