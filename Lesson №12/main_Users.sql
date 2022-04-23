create table Users
(
    id          integer not null
        constraint Users_pk
            primary key autoincrement,
    name        text    not null,
    age         integer not null,
    gender      text    not null,
    nationality text    not null
);

INSERT INTO Users (id, name, age, gender, nationality) VALUES (1, 'Danil', 21, 'M', 'Belarus');
INSERT INTO Users (id, name, age, gender, nationality) VALUES (2, 'Ivan', 23, 'M', 'Belarus');
INSERT INTO Users (id, name, age, gender, nationality) VALUES (3, 'John', 26, 'M', 'Canada');
INSERT INTO Users (id, name, age, gender, nationality) VALUES (4, 'Zlatan', 37, 'M', 'Sweden');
INSERT INTO Users (id, name, age, gender, nationality) VALUES (5, 'Jakub', 22, 'M', 'Czech');
