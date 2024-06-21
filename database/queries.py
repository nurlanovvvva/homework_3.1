
class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey_results (
            id INTEGER PRIMARY KEY 
            AUTOINCREMENT,
            name TEXT,
            phone INTEGER,
            visit_date DATE,
            food_quality INTEGER,
            cleanliness INTEGER,
            comments TEXT
        )    
    """

    DROP_CATEGORIES_TABLE = "DROP TABLE IF EXISTS categories"
    DROP_DISHES_TABLE = "DROP TABLE IF EXISTS dishes"

    CREATE_CATEGORIES_TABLE = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            )
            """

    CREATE_DISHES_TABLE = """
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price NUMERIC,
            category_id INTEGER,
         FOREIGN KEY (category_id) REFERENCES categories(id)
        )
        """

    POPULATE_CATEGORY = """
        INSERT INTO categories (name)
        VALUES ('Завтраки'),
            ('Супы'),
            ('Круассаны'),
            ('Пицца')
            """

    POPULATE_DISHES = """
        INSERT INTO dishes (name, price, category_id)
        VALUES ('Творожок', 360, 1),
            ('Сырник', 360, 1),
            ('Каша', 250, 1),
            ('Чечевичный суп', 290, 2),
            ('Томатный суп', 320, 2),
            ('Грибной суп', 310, 2),
            ('Классический', 150, 3),
            ('С нутеллой', 250, 3),
            ('С сыром', 350, 3),
            ('Пепперони', 550, 4),
            ('Маргарита', 490, 4),
            ('4 сыра', 610, 4)
            """