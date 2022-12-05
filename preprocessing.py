#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from collections import defaultdict

import pandas
import scipy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FOLDER = 'training2017'
LABEL_FILE = 'REFERENCE.csv'


def preprocess_data():
    label_csv = os.path.join(FOLDER, LABEL_FILE)

    labels = pd.read_csv(label_csv, header=None)
    label_filter = labels.iloc[:,1] != '~'
    labels = labels[label_filter]

    data = defaultdict(dict)

    for row in labels.iterrows():
        data[row[1][0]]['label'] = row[1][1]

    for filename in os.listdir(FOLDER):
        f = os.path.join(FOLDER, filename)
        if os.path.isfile(f) and f.endswith(".mat"):
            mat_data = scipy.io.loadmat(f)
            key = f.split('.')[0].split("/")[1]
            if key not in data:
                continue
            samples = mat_data['val'][0]
            if len(samples) < 3000:
                continue
            data[key]["signal"] = samples[0:3000]

    with open('data.csv', 'w') as file:
        for key, values in data.items():
            label = values['label']
            try:
                signal = values['signal'] / 1000.0
            except KeyError:
                continue
            signal_as_string = ';'.join(str(x) for x in signal)
            file.write(f'{key};{label};{signal_as_string}\n')

if __name__ == '__main__':
    # preprocess_data()

    data = pandas.read_csv('data.csv', header=None, sep=';')
    print(data)