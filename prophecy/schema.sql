CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE student (
    id INTEGER,
    student_name TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    student_id INTEGER NOT NULL,
    house TEXT,
    FOREIGN KEY (student_id) REFERENCES student(id)
);

CREATE TABLE heads (
    head_house TEXT NOT NULL,
    head TEXT,
    FOREIGN KEY (head_house) REFERENCES houses(house)
);