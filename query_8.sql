SELECT
sub.sub_name,
ROUND(AVG(j.mark),2) as av_mark
FROM journal as j
left join subjects as sub
	on sub.id = j.subject_id 
where j.subject_id IN (SELECT id FROM subjects WHERE teacher_id = 2)
GROUP BY j.subject_id, sub.sub_name
ORDER BY sub.sub_name
;