"""
Quick tutorial on how to run python scripts on vscode:

All data path should be prefixed with '~/Python/file-name'

To execute your code from the OUTPUT tab hit 'ctrl + option + N'
"""

import pandas as pd

df = pd.read_csv("~/Developer/Python/bin/data.csv")
print(df)
