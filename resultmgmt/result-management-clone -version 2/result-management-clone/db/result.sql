create table result(
	 student_id int not null,
     test_id int not null,
     score float not null,
     total_score float not null,
     foreign key(student_id) references student(id),
     foreign key(test_id) references test(id)
);
-----------