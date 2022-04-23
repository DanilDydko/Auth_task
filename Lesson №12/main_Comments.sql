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

INSERT INTO Comments (id, text, user_id, post_id) VALUES (1, 'Good examples', 3, 3);
INSERT INTO Comments (id, text, user_id, post_id) VALUES (2, 'Top match', 2, 1);
INSERT INTO Comments (id, text, user_id, post_id) VALUES (3, 'Not difficult', 1, 4);
INSERT INTO Comments (id, text, user_id, post_id) VALUES (4, 'Nice structure', 4, 7);
INSERT INTO Comments (id, text, user_id, post_id) VALUES (5, 'Good luck', 5, 10);
