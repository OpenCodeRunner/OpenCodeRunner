from pydantic import BaseModel, ConfigDict
from pydantic import model_validator
from typing import Optional, Literal
import warnings
from collections import defaultdict


class FileInfo(BaseModel):
    model_config = ConfigDict(extra="allow") # Allow adding extra fields after initialization.

    file_relpath: str
    file_content: str



