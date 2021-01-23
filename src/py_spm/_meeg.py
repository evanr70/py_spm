import numpy as np
from scipy.io import loadmat

from ._channel import Channel, chan_types
from ._data import Data
from ._trial import Trial
from .utils import check_lowered_string


class MEEG:
    def __init__(self, filename):
        D = loadmat(filename, simplify_cells=True)["D"]
        self.type = D["type"]
        self.n_samples = D["Nsamples"]
        self.f_sample = D["Fsample"]
        self.time_onset = D["timeOnset"]
        self.trials = Trial(**D["trials"])
        self.channels = [Channel.from_dict(channel) for channel in D["channels"]]
        self.data = Data(**D["data"])
        self.fname = D["fname"]
        self.path = D["path"]
        self.sensors = D["sensors"]
        self.fiducials = D["fiducials"]
        self.transform = D["transform"]
        self.condlist = D["condlist"]
        self.montage = D["montage"]
        self.history = D["history"]
        self.other = D["other"]

        self.trials.calculate_samples(self.f_sample)
        self.index = np.ones(self.n_samples, dtype=bool)
        self.good_index = np.zeros(self.n_samples, dtype=int)

        self.mark_artefacts_as_bad()
        self.reindex_good_samples()

    def define_trial(self, event_type, pre_stim, post_stim):
        for event in self.trials.events:
            event.trial_start = event.time - pre_stim
            event.trial_end = event.time + post_stim

    def mark_artefacts_as_bad(self):
        artefacts = check_lowered_string(self.trials.event_types, "artefact")
        starts = self.trials.event_samples[artefacts]
        ends = self.trials.event_end_samples[artefacts]

        for start, end in zip(starts, ends):
            self.index[start:end] = False

    def _channel_property(self, property_):
        return np.array([getattr(channel, property_) for channel in self.channels])

    def channel_types(self):
        return self._channel_property("type")

    def channel_selection(self, channel_type):
        return np.isin(self.channel_types(), chan_types[channel_type])

    def full_index(self, channel_type):
        return np.ix_(self.index, self.channel_selection(channel_type))

    def reindex_good_samples(self):
        self.good_index = np.zeros_like(self.index) - 1
        self.good_index[self.index] = self.index.cumsum()[self.index] - 1

    # TODO: Add method to reindex event samples. Perhaps this should be in _trial?
