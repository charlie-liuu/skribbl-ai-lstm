# skribbl-AI-LSTM

This repository trains a LSTM Model for the [Skribbl.ai](https://github.com/William-Gao1/skribbl-ai) web app.

The data used comes from the Quick, Draw! [dataset](https://quickdraw.withgoogle.com/data) provided by Google.

## Data Normalization
Raw data is given in stroke format:

```
[
  [  // First stroke
    [x0, x1, x2, x3, ...],
    [y0, y1, y2, y3, ...],
    [t0, t1, t2, t3, ...]
  ],
  [  // Second stroke
    [x0, x1, x2, x3, ...],
    [y0, y1, y2, y3, ...],
    [t0, t1, t2, t3, ...]
  ],
  ... // Additional strokes
]
```

We want to perform normalization on the stroke data using a variant of the RDP algorithm to construct a stroke format compatible with the LSTM model: 

  [  // First stroke
    [x0_norm, y0_norm, is_end_1],
    [x1_norm, y2_norm, is_end_2],
    [x0_norm, y0_norm, is_end_3],
    ........
  ]......


 We then pad each stroke using the post-padding technique, to ensure consistency of stroke size for LSTM model.


