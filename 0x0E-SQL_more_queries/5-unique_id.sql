-- TASK 5
-- BEGINS
CREATE TABLE IF NOT EXIST unique_id (
				id INT DEFAULT 1,
				name VARCHAR(256),
				UNIQUE (id)
);

