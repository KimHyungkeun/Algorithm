select earnings, count(earnings)
from 
(select months*salary as earnings from employee) as t
group by earnings
order by earnings desc limit 1