# -*- coding: utf-8 -*-
# flake8: noqa

from _channel import Channel
from _data import Data
from _event import Event
from _meeg import MEEG
from _trial import Trial
from pkg_resources import DistributionNotFound, get_distribution

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound
