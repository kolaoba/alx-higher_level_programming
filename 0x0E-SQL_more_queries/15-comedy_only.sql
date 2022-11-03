-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT
	ts.title AS title
FROM tv_show_genres AS tsg
JOIN tv_genres AS tg ON tg.id = tsg.genre_id
JOIN tv_shows AS ts ON tsg.show_id = ts.id
WHERE tg.name = "Comedy"
ORDER BY ts.title;
