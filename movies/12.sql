SELECT title FROM movies WHERE id IN
(SELECT movie_id FROM stars WHERE person_id in (SELECT id FROM people WHERE name LIKE "Bradley Cooper")
)
AND id IN
(SELECT movie_id FROM stars WHERE person_id in (SELECT id FROM people WHERE name LIKE "Jennifer Lawrence")
)