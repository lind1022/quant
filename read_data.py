import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web


df = web.DataReader('SPY', data_source='google')
