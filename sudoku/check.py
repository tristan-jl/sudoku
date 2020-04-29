import numpy as np
import pandas as pd

sudokus = np.load("../data/sudokus.npy")
sudokus = sudokus.reshape(1000, 81)

solutions = np.array(
    [np.array2string(i, separator="", max_line_width=1000)[1:-1] for i in sudokus]
)
answers = pd.read_csv("../data/sudoku.csv")["solutions"].to_numpy()[:1000]

assert (solutions == answers).all()
