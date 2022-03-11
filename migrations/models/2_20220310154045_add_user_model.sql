-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "user_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "email" VARCHAR(120) NOT NULL UNIQUE,
    "status" INT NOT NULL  DEFAULT 1
);
-- downgrade --
DROP TABLE IF EXISTS "user";
