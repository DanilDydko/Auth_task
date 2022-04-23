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

INSERT INTO Posts (id, title, description, user_id) VALUES (1, 'How to improve your skills', 'Some text with recomendations', 1);
INSERT INTO Posts (id, title, description, user_id) VALUES (2, 'Chelsea -  Real Madrid', 'Final result: 3:2', 1);
INSERT INTO Posts (id, title, description, user_id) VALUES (3, 'SQL', 'Structured query language', 2);
INSERT INTO Posts (id, title, description, user_id) VALUES (4, 'SQL', 'INNER JOIN', 2);
INSERT INTO Posts (id, title, description, user_id) VALUES (5, 'SQL', 'LEFT JOIN', 3);
INSERT INTO Posts (id, title, description, user_id) VALUES (6, 'SQL', 'RIGHT JOIN', 3);
INSERT INTO Posts (id, title, description, user_id) VALUES (7, 'SQL', 'SELECT', 4);
INSERT INTO Posts (id, title, description, user_id) VALUES (8, 'SQL', 'GROUP BY', 4);
INSERT INTO Posts (id, title, description, user_id) VALUES (9, 'SQL', 'ORDER BY', 5);
INSERT INTO Posts (id, title, description, user_id) VALUES (10, 'SQL', 'UPDATE', 5);
