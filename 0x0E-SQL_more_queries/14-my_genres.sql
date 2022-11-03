-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT
	tg.name AS genre
FROM tv_show_genres AS tsg
JOIN tv_genres AS tg ON tg.id = tsg.genre_id
JOIN tv_shows AS ts ON tsg.show_id = ts.id
WHERE ts.title = "Dexter"
ORDER BY tg.name;
