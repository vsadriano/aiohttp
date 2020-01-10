CREATE SEQUENCE public.author_author_id_seq;

CREATE TABLE public.Author (
                author_id BIGINT NOT NULL DEFAULT nextval('public.author_author_id_seq'),
                author_fname VARCHAR NOT NULL,
                author_lname VARCHAR NOT NULL,
                author_email VARCHAR NOT NULL,
                CONSTRAINT author_id PRIMARY KEY (author_id)
);

COMMENT ON TABLE public.Author IS 'Tabela para o crude';

ALTER SEQUENCE public.author_author_id_seq OWNED BY public.Author.author_id;

INSERT INTO public.author (author_fname, author_lname, author_email)
VALUES ('Francisco', 'SILVA', 'francisco.silva@mail.com');

INSERT INTO public.author (author_fname, author_lname, author_email)
VALUES ('José', 'SOUSA', 'jose.sousa@mail.com');

INSERT INTO public.author (author_fname, author_lname, author_email)
VALUES ('Maria', 'JOSE', 'maria.jose@mail.com');

SELECT * FROM author;
