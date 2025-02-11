CREATE TABLE researcher(
id SERIAL PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(50) UNIQUE NOT NULL,
organization VARCHAR(10)
);
CREATE TYPE callstatus AS ENUM('open','closed','paused','cancelled');

CREATE TABLE call(
id SERIAL PRIMARY KEY,
title VARCHAR(50) NOT NULL,
deadline DATE NOT NULL,
description VARCHAR(250),
area VARCHAR(30) NOT NULL,
status callstatus DEFAULT 'open'
);

CREATE TYPE appstatus AS ENUM('submitted','awarded','denied');

CREATE TABLE proposal(
id SERIAL PRIMARY KEY,
callid INT REFERENCES call(id) NOT NULL,
pi INT REFERENCES researcher(id) NOT NULL,
status appstatus DEFAULT 'submitted' NOT NULL,
requestedamount NUMERIC(14,2),
awardedamount NUMERIC(14,2)
);

CREATE TABLE collaborator(
id SERIAL PRIMARY KEY,
proposalid INT REFERENCES proposal(id) NOT NULL,
researcherid INT REFERENCES researcher(id) NOT NULL,
ispi BOOLEAN DEFAULT 'false' NOT NULL
);

CREATE TABLE conflict(
id SERIAL PRIMARY KEY,
researcher1 INT REFERENCES researcher(id) NOT NULL,
researcher2 INT REFERENCES researcher(id) NOT NULL,
reason VARCHAR(50),
expiry DATE
);

CREATE TABLE review(
id SERIAL PRIMARY KEY,
reviewerid INT REFERENCES researcher(id) NOT NULL,
proposalid INT REFERENCES proposal(id) NOT NULL,
deadline DATE NOT NULL,
submitted BOOLEAN DEFAULT 'false' NOT NULL
);

CREATE TABLE meeting(
id SERIAL PRIMARY KEY,
room INT NOT NULL,
meetdate DATE NOT NULL,
callid1 INT REFERENCES call(id) NOT NULL,
callid2 INT REFERENCES call(id) NOT NULL,
callid3 INT REFERENCES call(id) NOT NULL
);