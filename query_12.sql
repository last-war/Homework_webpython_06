
SELECT
st.full_name,  
sub.sub_name,
j.created_at,
j.mark
FROM journal as j
left join students as st 
	on st.id = j.student_id  
left join subjects as sub
	on sub.id = j.subject_id 
where j.student_id IN (SELECT id FROM students WHERE group_id = 2) 
	AND j.subject_id = 5 
	AND j.created_at IN (SELECT MAX(created_at) FROM journal)
ORDER BY created_at DESC
;