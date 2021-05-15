select hour(datetime) as hour, count(hour(datetime)) 
from animal_outs 
group by hour(datetime) 
having hour between 9 and 19
order by hour(datetime)