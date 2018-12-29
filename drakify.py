## Some Libraries 
import requests
import urllib.request
import lyricsgenius as genius
from bs4 import BeautifulSoup
import re

# Importing drake's lyrics
api = genius.Genius('Ye9vStKoQbjvtVoC2U9Rmdw8srYz2f4DrobmZCMlkXLqAxJCuEB_k2x-FXN118Zt')
artist = api.search_artist('Drake')
artist.save_lyrics(format_='txt')
artist.save_lyrics(format_='json')

