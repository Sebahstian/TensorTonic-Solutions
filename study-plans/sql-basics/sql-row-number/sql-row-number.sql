-- Write your SQL query here
SELECT 
    username,
    segment,
    engagement_score,
    ROW_NUMBER() OVER (PARTITION BY segment ORDER BY engagement_score DESC) as activity_rank
FROM user_activity
ORDER BY segment ASC;