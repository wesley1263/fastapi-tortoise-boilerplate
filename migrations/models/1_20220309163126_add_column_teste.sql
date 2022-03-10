-- upgrade --
ALTER TABLE "textsummary" ADD "teste" INT NOT NULL  DEFAULT 1;
-- downgrade --
ALTER TABLE "textsummary" DROP COLUMN "teste";
