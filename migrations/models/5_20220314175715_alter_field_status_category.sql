-- upgrade --
ALTER TABLE "category" RENAME COLUMN "stauts" TO "status";
-- downgrade --
ALTER TABLE "category" RENAME COLUMN "status" TO "stauts";
