
class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey_results (
            id INTEGER PRIMARY KEY 
            AUTOINCREMENT,
            name TEXT,
            numbers TEXT,
            data DATE,
            qualities INT,
            purities INT,
            comments TEXT
        )    
    """

