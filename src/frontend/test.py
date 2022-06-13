import pandas as pd
from src import config

artist_name = "Moi dix Mois"
print(config.ARTIST_IMAGE_PATH)
image_path_df = pd.read_csv(config.ARTIST_IMAGE_PATH)
image_path = image_path_df[image_path_df["artist_name"]==artist_name]["image_path"].values[0]
# print(image_path)