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

INSERT INTO Likes (id, user_id, post_id) VALUES (1, 3, 6);
INSERT INTO Likes (id, user_id, post_id) VALUES (2, 4, 9);
INSERT INTO Likes (id, user_id, post_id) VALUES (3, 2, 6);
INSERT INTO Likes (id, user_id, post_id) VALUES (4, 5, 3);
INSERT INTO Likes (id, user_id, post_id) VALUES (5, 1, 4);
