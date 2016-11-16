-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE TABLE players (id SERIAL PRIMARY KEY, name text);

CREATE TABLE matches (
						id SERIAL PRIMARY KEY,
						winner integer, FOREIGN KEY(winner) REFERENCES players(id),
						loser integer, FOREIGN KEY(loser) REFERENCES players(id));
CREATE VIEW standings AS
SELECT players.id, players.name,
(SELECT COUNT(matches.winner) FROM matches WHERE players.id = matches.winner) as winner,
(SELECT COUNT(matches.id) FROM matches WHERE players.id = matches.winner or players.id = matches.loser) as total FROM players ORDER BY winner,total;



