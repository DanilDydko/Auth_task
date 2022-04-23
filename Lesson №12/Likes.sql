create table Likes
(
    id      integer not null
        constraint Likes_pk
            primary key autoincrement,
    user_id integer not null
        references Users,
    post_id integer not null
        references Posts
);

