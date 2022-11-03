-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT
	tg.name AS genre,
	COUNT(tg.genre_id) AS number_of_shows
FROM tv_show_genres AS tsg
JOIN tv_genres AS tg ON tg.id = tsg.genre_id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC, tg.id ASC;
