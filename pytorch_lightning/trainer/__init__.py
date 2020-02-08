"""
.. warning:: `trainer` package has been renamed to `train` since v0.6.0 and will be removed in v0.8.0
"""

import warnings

from pytorch_lightning.train import (  # noqa: E402
    auto_mix_precision,
    callback_config,
    data_loading,
    distrib_data_parallel,
    distrib_parts,
    evaluation_loop,
    ignored_warnings,
    logging,
    model_hooks,
    trainer,
    training_io,
    training_loop,
    training_tricks
)
from pytorch_lightning.train import Trainer

warnings.warn("`trainer` package has been renamed to `train` since v0.6.0"
              " and will be removed in v0.8.0", DeprecationWarning)

__all__ = ['Trainer']
