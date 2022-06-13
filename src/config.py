# config names 
from pathlib import Path
PAGE_TITLE = "Song Recommendation"
TITLE = "Last FM"

ARTIST_LIST_PATH = Path(__file__).resolve().parents[1]/"data/artist_list.csv"
ARTIST_IMAGE_PATH = Path(__file__).resolve().parents[1]/"data/artist_image.csv"

## LAST FM API
API_KEY = "d3979ccb5a422a438636c4fc9a054e38"
BASE_URL = "https://ws.audioscrobbler.com/2.0/"
USER_AGENT = "Dataquest"
LIMIT_TOP_SONG =5