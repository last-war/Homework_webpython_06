
SELECT
st.full_name,  
sub.sub_name
--j.*
FROM journal as j
left join students as st 
	on st.id = j.student_id  
left join subjects as sub
	on sub.id = j.subject_id 
where  j.student_id = 30
GROUP BY st.full_name, sub.sub_name
;