import os

import pytest
import sys

pytest.main('--junitxml={path}/report.xml'.format(path=os.path.dirname(os.path.realpath(__file__))))
sys.exit(0)
