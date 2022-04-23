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

