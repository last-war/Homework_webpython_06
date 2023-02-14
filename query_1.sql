SELECT
st.full_name,  
ROUND(AVG(j.mark),2) as av_mark
FROM journal as j
left join students as st 
	on st.id = j.student_id  
GROUP BY j.student_id
ORDER BY av_mark DESC
limit 5
;