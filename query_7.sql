
SELECT
st.full_name,  
j.mark
FROM journal as j
left join students as st 
	on st.id = j.student_id  
left join subjects as sub
	on sub.id = j.subject_id 
where  st.group_id = 3 AND j.subject_id = 3
ORDER BY sub.sub_name
;