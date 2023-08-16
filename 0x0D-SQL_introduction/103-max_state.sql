-- displays the max temperature of each state (ordered by State name).

SELECT state, MAX(val) AS max_temp
FROM temperature
GROUP BY state,
ORDER BY state DESC;
