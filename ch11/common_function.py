import os

def save_csv(df , hfp):
    if os.path.exists(hfp):
        os.remove(hfp)
    df.to_csv(hfp)

