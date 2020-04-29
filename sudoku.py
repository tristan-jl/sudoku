import time

import numpy as np
import pandas as pd
from tqdm import tqdm

from utils import solve


def main():
    sudokus_df = pd.read_csv("data/sudoku.csv")
    sudokus = np.array(
        [
            (np.fromstring(i, np.int8) - ord("0")).reshape(9, 9)
            for i in sudokus_df["quizzes"].to_numpy()
        ]
    )

    start_time = time.time()
    for p in tqdm(sudokus):
        solve(p)

    t = time.time() - start_time

    print(t)
    print(t / len(sudokus))
    np.save("data/sudokus.npy", sudokus)


if __name__ == "__main__":
    main()
