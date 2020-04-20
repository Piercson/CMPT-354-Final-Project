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