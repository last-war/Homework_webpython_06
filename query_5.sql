SELECT
sub.sub_name,  
t.full_name
FROM subjects as sub left join teachers as t 
on sub.teacher_id = t.id 
where  t.id = 2;