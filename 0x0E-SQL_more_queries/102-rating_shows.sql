-- This script lists all shows from the hbtn_0d_tvshows_rate database by their rating.
-- Each record displays the title of the TV show followed by the sum of its ratings.
-- Results are sorted in descending order by the rating sum.
-- Only one SELECT statement is used.
SELECT title, SUM(rating) AS rating_sum
FROM tv_shows
GROUP BY title
ORDER BY rating_sum DESC;
