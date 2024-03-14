-- This script lists all genres in the hbtn_0d_tvshows_rate database by their rating.
-- Each record displays the name of the genre followed by the sum of ratings for all TV shows belonging to that genre.
-- Results are sorted in descending order by the rating sum.
-- Only one SELECT statement is used, joining the tv_genres and tv_shows tables.
SELECT tv_genres.name, SUM(tv_shows.rating) AS rating_sum
FROM tv_genres
JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
