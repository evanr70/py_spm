from py_spm import Channel, Data, Trial
from scipy.io import loadmat


class MEEG:
    def __init__(self, filename):
        D = loadmat(filename, simplify_cells=True)["D"]
        self.type = D["type"]
        self.n_samples = D["Nsamples"]
        self.f_sample = D["Fsample"]
        self.timeOnset = D["timeOnset"]
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
