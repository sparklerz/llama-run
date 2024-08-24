import warnings

warnings.warn(
    "llama-run.dht_utils has been moved to llama-run.utils.dht. This alias will be removed in Petals 2.2.0+",
    DeprecationWarning,
    stacklevel=2,
)

from llama-run.utils.dht import *
