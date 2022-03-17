-- upgrade --
CREATE TABLE IF NOT EXISTS "category" (
    "category_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL UNIQUE,
    "status" INT NOT NULL  DEFAULT 1
);
-- downgrade --
DROP TABLE IF EXISTS "category";
