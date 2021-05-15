select animal_type, 
    case 
        when name is null then 'No name'
        else name
    end,
    sex_upon_intake
from animal_ins
order by animal_id