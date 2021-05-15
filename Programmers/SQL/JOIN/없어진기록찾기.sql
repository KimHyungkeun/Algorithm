select t2.animal_id, t2.name
from animal_ins t1 right outer join animal_outs t2
using (animal_id)
where t1.animal_id is null
order by t2.animal_id