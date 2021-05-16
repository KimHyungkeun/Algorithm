-- 210516 재풀이
SET @hour = -1;

select (@hour := @hour + 1) as hour, (select count(*) from animal_outs where hour(datetime) = @hour)
from animal_outs
where @hour < 23


-- SET @hour = -1;

-- select (@hour := @hour + 1) as hour, (select count(*) from animal_outs where hour(datetime) = @hour) as count
-- from animal_outs
-- where @hour < 23