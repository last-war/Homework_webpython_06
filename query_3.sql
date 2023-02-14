SELECT
st.group_id,  
sub.sub_name,
ROUND(AVG(j.mark),2) as av_mark
FROM journal as j
left join students as st 
	on st.id = j.student_id  
left join subjects as sub
	on sub.id = j.subject_id 
where  j.subject_id = 4
GROUP BY st.group_id
;