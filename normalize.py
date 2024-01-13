
import numpy as np
import pandas as pd

def normalize(row):
    word = row["word"]
    strokes = row["drawing"]

    stroke_lengths = [len(stroke[0]) for stroke in strokes]
    total_points = sum(stroke_lengths)
    arr_strokes = np.zeros((total_points, 3), dtype=np.float32)
    current_t = 0

    for stroke in strokes:
        for i in [0, 1]:
            arr_strokes[current_t:(current_t + len(stroke[0])), i] = stroke[i]
        current_t += len(stroke[0])
        arr_strokes[current_t - 1, 2] = 1 

    lower = np.min(arr_strokes[:, 0:2], axis=0)
    upper = np.max(arr_strokes[:, 0:2], axis=0)

    scale = upper - lower
    arr_strokes[:, 0:2] = (arr_strokes[:, 0:2] - lower) / scale
    scale[scale == 0] = 1
    
    arr_strokes[1:, 0:2] -= arr_strokes[0:-1, 0:2]
    arr_strokes = arr_strokes[1:, :]
    return arr_strokes, word

def pad_strokes(file, max_stroke):
    df = pd.read_json(file, lines=True)
    # Apply the parsing function to each row using df.apply
    result = df.apply(normalize, axis=1)

    # # Process the results if needed
    # data_x = np.empty((0, 100, 3), float)
    # ctr = 0

    result_df = result.to_frame()
    result_df['name'] = result_df[0].apply(lambda x: x[1])
    result_df  = result_df.rename(columns = {0 : 'Strokes'})
    result_df.Strokes = result_df.Strokes.apply(lambda x: x[0].tolist())
    max_length = max_stroke
    padded_strokes = result_df.Strokes.apply(lambda x: x + [(0, 0, 0)] * (max_length - len(x)))
    return padded_strokes

def max_strokes(file):
    df = pd.read_json(file, lines=True)
    # Apply the parsing function to each row using df.apply
    result = df.apply(normalize, axis=1)
    result_df = result.to_frame()
    result_df['name'] = result_df[0].apply(lambda x: x[1])
    result_df  = result_df.rename(columns = {0 : 'Strokes'})
    result_df.Strokes = result_df.Strokes.apply(lambda x: x[0].tolist())
    max_length = result_df.Strokes.apply(len).max()
    return max_length