create table Comments
(
    id      integer not null
        constraint Comments_pk
            primary key autoincrement,
    text    text    not null,
    user_id integer not null
        references Users,
    post_id integer not null
        references Posts
);

