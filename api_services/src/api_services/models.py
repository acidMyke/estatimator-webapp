# Add each individual models imports here

from sqlmodel import SQLModel

from .features.admin.models import *
from .features.admin_auth.models import *
from .features.auth.models import *
from .features.users.models import *

target_metadata = SQLModel.metadata
