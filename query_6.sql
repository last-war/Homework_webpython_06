SELECT
st.full_name,  
g.gr_name
FROM students as st left join study_groups as g
on g.id = st.group_id 
where  g.id = 2;