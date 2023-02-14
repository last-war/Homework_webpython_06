
SELECT
sub.sub_name
FROM journal as j
left join subjects as sub
	on sub.id = j.subject_id 
where j.subject_id IN (SELECT id FROM subjects WHERE teacher_id = 2) AND j.student_id = 17
GROUP BY sub.sub_name
;