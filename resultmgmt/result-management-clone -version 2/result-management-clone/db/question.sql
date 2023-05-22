create table question(

	id numeric(6,0),
    test_id int,
    description varchar(1000) not null,
    option1 varchar(100),
    option2 varchar(100),
    option3 varchar(100),
    option4 varchar(100),
    answer varchar(1) not null,
    marks int not null,
    foreign key(test_id) references test(id),
    primary key(id)
);
---------------