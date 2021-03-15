# musical-time-machine
A Python script that creates a Spotify playlist with the top hits on a date specified by the user

The first step is web scraping using Python's Beautiful Soup module. The script scrapes the Billboard Hot 100 Chart (https://www.billboard.com/charts/hot-100) on a date specified by the user.

Then, a connection to the Spotify API is made. The script looks for songs on Spotify with the title from the Billboard chart scraping. The search is narrowed by the year of the Billboards chart. Then, a Spotify playlist is created with all the songs found in Spotify.

Narrowing down the search results by year ensures better accuracy when looking for songs. But it is a problem when the top hits chart has songs from prior years (this script won't find these songs in Spotify). Idea for improvement: the song search could use song title and artist name, not the year.

The script only works when I'm logged into my Spotify account on a web browser.
