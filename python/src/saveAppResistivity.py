import numpy as np
from scipy.constants import mu_0, pi

from layeredearthfunctions import PlaneWaveImpedance, apparentresistivity
from mtsphere3d import mtsphere3d

import pickle

with open('ZdataAnalytic.pkl', 'rb') as f:
    Zanalytic = pickle.load(f)

appres, phase = apparentresistivity(
    1,
    45,
    1,
    [1.0],
    Zanalytic
)

with open('AppResdataAnalytic.pkl', 'wb') as f:
    pickle.dump(appres, f)

with open('phasedataAnalytic.pkl', 'wb') as f:
    pickle.dump(phase, f)