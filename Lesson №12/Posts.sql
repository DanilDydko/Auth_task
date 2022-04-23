create table Posts
(
    id          integer not null
        constraint Posts_pk
            primary key autoincrement,
    title       text    not null,
    description text    not null,
    user_id     integer not null
        references Users
);

