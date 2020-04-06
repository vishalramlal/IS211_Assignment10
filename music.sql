CREATE TABLE song (id INTEGER PRIMARY KEY ASC, song_title TEXT, album_name INTEGER, track_no INTEGER, run_time INTEGER);

CREATE TABLE artist (id INTEGER PRIMARY KEY, name TEXT);

CREATE TABLE album (id INTEGER PRIMARY KEY, album_name TEXT, artist_name INTEGER);


