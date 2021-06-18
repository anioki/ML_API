import pandas as pd
from sklearn.preprocessing import StandardScaler
import re

class DataLoader(object):
    def __init__(self):
        self.dataset = 0

    def fit(self, dataset):
        self.dataset = dataset.copy()

    # apply regex
    def get_title(self, name):
        pattern = ' ([A-Za-z]+)\.'
        title_search = re.search(pattern, name)
        # If the title exists, extract and return it.
        if title_search:
            return title_search.group(1)
        return ""


    def load_data(self):
        return self.dataset
