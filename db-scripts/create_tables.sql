CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    user_id NUMERIC NOT NULL,
    amount NUMERIC NOT NULL,
    description TEXT NOT NULL,
    expense_date DATE NOT NULL,
    category_id INTEGER NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
