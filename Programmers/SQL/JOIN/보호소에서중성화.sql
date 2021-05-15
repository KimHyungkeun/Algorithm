select t1.animal_id, t1.animal_type, t1.name
from animal_ins t1 join animal_outs t2
on t1.animal_id = t2.animal_id
where sex_upon_intake like '%Intact%' and (sex_upon_outcome like '%Spayed%' or sex_upon_outcome like '%Neutered%')
order by t1.animal_id