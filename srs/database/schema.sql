CREATE TABLE Student(
    stID TEXT,
    sname TEXT NOT NULL,
    pass TEXT NOT NULL,
    PRIMARY KEY(stID)
);

CREATE TABLE Admin(
    aID TEXT,
    aname TEXT NOT NULL,
    pass TEXT NOT NULL,
    PRIMARY KEY(aID)
);

CREATE TABLE Professor(
    pID TEXT,
    pname TEXT NOT NULL,
    pass TEXT NOT NULL,
    PRIMARY KEY(pID)
);

CREATE TABLE Course(
    cID TEXT,
    cname TEXT NOT NULL,
    capacity int NOT NULL,
    semester TEXT NOT NULL,
    credits int NOT NULL,
    PrID TEXT,
    PRIMARY KEY(cID),
    FOREIGN KEY(PrID) REFERENCES Professor(pID)
);

CREATE TABLE Registered_In(
    stuID TEXT,
    coID TEXT,
    grade TEXT,   
    PRIMARY KEY(stuID, coID),
    FOREIGN KEY(stuID) REFERENCES Student(stID),
    FOREIGN KEY(coID) REFERENCES Course(cID)
);