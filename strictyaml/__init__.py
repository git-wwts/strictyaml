# The all important loader
from strictyaml.parser import load

# Document builder
from strictyaml.document import as_document

# YAML object
from strictyaml.representation import YAML

# Validators
from strictyaml.validators import Optional
from strictyaml.validators import Validator
from strictyaml.validators import OrValidator
from strictyaml.any_validator import Any
from strictyaml.scalar import Scalar
from strictyaml.scalar import Enum
from strictyaml.scalar import Regex
from strictyaml.scalar import Email
from strictyaml.scalar import Url
from strictyaml.scalar import Str
from strictyaml.scalar import Int
from strictyaml.scalar import Bool
from strictyaml.scalar import Float
from strictyaml.scalar import Decimal
from strictyaml.scalar import Datetime
from strictyaml.scalar import CommaSeparated
from strictyaml.scalar import EmptyNone
from strictyaml.scalar import EmptyDict
from strictyaml.scalar import EmptyList
from strictyaml.validators import Map
from strictyaml.validators import MapPattern
from strictyaml.validators import Seq
from strictyaml.validators import UniqueSeq
from strictyaml.validators import FixedSeq

# Base exception from ruamel.yaml (all exceptions inherit from this)
from ruamel.yaml import YAMLError

# Exceptions
from strictyaml.exceptions import StrictYAMLError
from strictyaml.exceptions import YAMLValidationError

# Disallowed token exceptions
from strictyaml.exceptions import DisallowedToken

from strictyaml.exceptions import TagTokenDisallowed
from strictyaml.exceptions import FlowMappingDisallowed
from strictyaml.exceptions import AnchorTokenDisallowed
from strictyaml.exceptions import DuplicateKeysDisallowed
from strictyaml import exceptions

__version__ = "DEVELOPMENT_VERSION"
