-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT
	ts.title AS title,
	tg.name AS name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON tsg.show_id = ts.id
LEFT JOIN tv_genres AS tg ON tg.id = tsg.genre_id
WHERE tg.name = "Comedy"
ORDER BY ts.title, tg.name;
