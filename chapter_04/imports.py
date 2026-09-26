# Standard library
from datetime import datetime, timezone         # two imports, same line
from unittest.mock import patch         # single import

# Third party library
import pytest

# Local code
from core.models import (           # multiline import
    Exam,
    Exercise,
    Solution,
)
