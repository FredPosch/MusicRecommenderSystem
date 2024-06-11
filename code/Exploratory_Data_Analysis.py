##############################################################
#  This skript is a first exploration of the spotify dataset #
##############################################################

# loading relevant packages
import numpy as np
import pandas as pd
import torch
import matplotlib as plt

# loading the data

df = pd.read_csv('data/spotify_dataset.csv')

print(df.shape)