INSERT INTO researcher VALUES
(DEFAULT,'Andrea','Le','andreale@sfu.ca','SFU'),
(DEFAULT,'Lori','Hoknes','LoriH@sfu.ca','SFU'),
(DEFAULT, 'Jeffery', 'Liam', 'jli@ubc.ca','UBC'),
(DEFAULT, 'Owen', 'Yuler', 'owyu@uofs', 'UofS'),
(DEFAULT, 'Thomas', 'John', 'ToJo@ubc.ca','UBC'),
(DEFAULT, 'James', 'Smith', 'jsmith@sfu.ca','SFU'),
(DEFAULT, 'Mary', 'Johnson', 'mjohnson@ubc.ca','UBC'),
(DEFAULT, 'John', 'Williams', 'jwill@uofs.ca','UofS'),
(DEFAULT, 'Patricia', 'Jones', 'patj@sfu.ca','SFU'),
(DEFAULT, 'Robert', 'Brown', 'bobbrown@ubc.ca','UBC'),
(DEFAULT, 'Linda', 'Davis', 'ldavis@sfu.ca','SFU'),
(DEFAULT, 'Michael', 'Miller', 'mmiller@UofS.ca','UofS'),
(DEFAULT, 'Barbara', 'Wilson', 'barbwilson@ubc.ca','UBC'),
(DEFAULT, 'William', 'Moore', 'wmoore@sfu.ca','SFU'),
(DEFAULT, 'Elizabeth', 'Taylor', 'liztaylor@sfu.ca','SFU'),
(DEFAULT, 'David', 'Anderson', 'danderson@sfu.ca','SFU'),
(DEFAULT, 'Jennifer', 'Thomas', 'jthomas@ubc.ca','UBC'),
(DEFAULT, 'Richard', 'Jackson', 'rjackson@ubc.ca','UBC'),
(DEFAULT, 'Charles', 'White', 'charlesw@ubc.ca','UBC'),
(DEFAULT, 'Joseph', 'Harris', 'joharris@ubc.ca','UBC'),
(DEFAULT, 'Thomas', 'Martin', 'tmartin@ubc.ca','UBC'),
(DEFAULT, 'Maria', 'Anderson', 'manderson@sfu.ca','SFU'),
(DEFAULT, 'Susan', 'Garcia', 'sgarcia@sfu.ca','SFU'),
(DEFAULT, 'Margaret', 'Young', 'myoung@sfu.ca','SFU'),
(DEFAULT, 'David', 'Anderson', 'danderson@sfu.ca','SFU'),
(DEFAULT, 'George', 'Walker', 'gwalker@uofs.ca','UofS'),
(DEFAULT, 'Clark', 'Clarkson', 'cclarkson@uofs.ca','UofS'),
(DEFAULT, 'Rodrigo', 'Rodriguez', 'roro@uofs.ca','UofS'),
(DEFAULT, 'Sandra', 'Peters', 'speters@uofs.ca','UofS'),
(DEFAULT, 'Sharon', 'Evans', 'sevans@uofs.ca','UofS');

INSERT INTO call VALUES
(DEFAULT, 'Student Research Fund', '2018-01-01' , 'NULL', 'Biology', 'closed'),
(DEFAULT, 'Cancer Research', now() + interval '10 week' , 'NULL', 'Biology', 'open'),
(DEFAULT, 'Blood Cells Research', now() + interval '20 week' , 'NULL', 'Biology', 'open'),
(DEFAULT, 'Research of shortest paths', now() + interval '2 week' , 'NULL' , 'Computer Science', 'open'),
(DEFAULT, 'Dynamic Programming Research', now() + interval '8 week' , 'NULL' , 'Computer Science', 'open'),
(DEFAULT, 'Greedy Algorithm Research', now() + interval '4 week' , 'NULL' , 'Computer Science', 'open'),
(DEFAULT, 'Divide and Conquer Algorithm Research', '2019-09-17' , 'NULL' , 'Computer Science', 'closed'),
(DEFAULT, 'Research for COVID-19 Round 3', now() + interval '8 week' , 'NULL','Mircobiology', 'open'),
(DEFAULT, 'Research for COVID-19 Round 2', now() + interval '4 week' , 'NULL','Mircobiology', 'open'),
(DEFAULT, 'Research for COVID-19 Round 1', '2020-03-16' , 'NULL','Mircobiology', 'closed'),
(DEFAULT, 'Research for HIV', now() + interval '12 week' , 'NULL','Mircobiology', 'open'),
(DEFAULT, 'Research for Ebola', now() + interval '14 week' , 'NULL','Mircobiology', 'open'),
(DEFAULT, 'Research for Flu', now() + interval '52 week' , 'NULL','Mircobiology', 'open'),
(DEFAULT, 'Classical Conditioning Research', now() + interval '1 week' , 'NULL', 'Psycology', 'cancelled'),
(DEFAULT, 'Clinical Psychology Research', now() + interval '4 week' , 'NULL', 'Psycology', 'open'),
(DEFAULT, 'Developmental Psychology Research', now() + interval '6 week' , 'NULL', 'Psycology', 'open'),
(DEFAULT, 'Cognitive Psychology Research', '2018-05-12' , 'NULL', 'Psycology', 'closed'),
(DEFAULT, 'Neuropsychology Research', '2019-12-12' , 'NULL', 'Psycology', 'closed'),
(DEFAULT, 'Research Jacobi Iterations', now() + interval '2 week' , 'NULL', 'Math', 'paused');
(DEFAULT, 'Research Graph Theory', now() + interval '6 week' , 'NULL', 'Math', 'open');
(DEFAULT, 'Research Discrete Mathematics', now() + interval '22 week' , 'NULL', 'Math', 'open');
(DEFAULT, 'Research Jacobi Iterations', '2019-10-14' , 'NULL', 'Math', 'closed');
(DEFAULT, 'Research Matrix Algebra', '2019-07-11' , 'NULL', 'Math', 'closed');
(DEFAULT, 'Research: Combinatorics', '2020-01-01' , 'NULL', 'Math', 'closed');

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