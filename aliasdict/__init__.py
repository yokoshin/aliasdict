
try:
    from .version import version as __version__
except ImportError:
    __version__ = None

from .aliasdict import AliasDict,AliasDictError
