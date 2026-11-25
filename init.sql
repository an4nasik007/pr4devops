CREATE TABLE IF NOT EXISTS public.items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO public.items (id, name)
VALUES
    (1, 'first item'),
    (2, 'second item')
ON CONFLICT (id) DO UPDATE
SET name = EXCLUDED.name;

SELECT setval(
    pg_get_serial_sequence('public.items', 'id'),
    COALESCE((SELECT MAX(id) FROM public.items), 1),
    true
);
