INSERT INTO researcher VALUES
(DEFAULT,'Andrea','Le','andreale@sfu.ca','SFU'),
(DEFAULT,'Lori','Hoknes','LoriH@sfu.ca','SFU'),
(DEFAULT, 'Jeffery', 'Liam', 'jli@ubc.ca','UBC'),
(DEFAULT, 'Owen', 'Yuler', 'owyu@uofs', 'UofS'),
(DEFAULT, 'Thomas', 'John', 'ToJo@ubc.ca','UBC');

INSERT INTO call VALUES
(DEFAULT, 'John student fund: looking for applicants', now() + interval '3 week' , 'NULL', 'Biology', 'closed'),
(DEFAULT, 'Looking for reseach of shortest paths', now() + interval '2 week' , 'NULL' , 'Computer Science', 'open'),
(DEFAULT, 'Research for COVID-19', now() + interval '1 week' , 'NULL','Mircobiology', 'open'),
(DEFAULT, 'Need Research for Classical Conditioning', now() + interval '1 week' , 'NULL', 'Psycology', 'cancelled'),
(DEFAULT, 'Research Jacobi Iterations', now() + interval '2 week' , 'NULL', 'MATH', 'paused');

INSERT INTO proposal VALUES
(DEFAULT,1,1,'awarded',36000, 30000),
(DEFAULT,3,4,'submitted',25000, 0),
(DEFAULT,5,2,'denied',30000, 0);

INSERT INTO collaborator VALUES
(DEFAULT,2,4,True);

INSERT INTO conflict VALUES
(DEFAULT,4,3,'Are collaborators', now() + interval '1 year');

INSERT INTO review VALUES
(DEFAULT,5,2, now() + interval '2 week', True);