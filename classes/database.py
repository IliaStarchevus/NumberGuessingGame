class Database:
    requests = {
        "create_tb": {
            "rounds_tb": """
                CREATE TABLE IF NOT EXISTS "rounds_tb" (
                    "round_id"	INTEGER NOT NULL UNIQUE,
                    "round_started"	TEXT NOT NULL,
                    "round_ended"	TEXT NOT NULL,
                    "diff"	TEXT NOT NULL,
                    "atts"	INTEGER NOT NULL,
                    "defined_num"	INTEGER NOT NULL,
                    "is_num_guessed"	INTEGER NOT NULL,
                    "presumed_nums"	TEXT NOT NULL,
                    PRIMARY KEY("round_id" AUTOINCREMENT)
                );
            """,
            "game_tb": """
                CREATE TABLE IF NOT EXISTS "game_tb" (
                    "game_id"	INTEGER NOT NULL UNIQUE,
                    "game_started"	TEXT NOT NULL,
                    "game_ended"	TEXT NOT NULL,
                    "rounds"	INTEGER NOT NULL,
                    "round_ids"	INTEGER NOT NULL,
                    PRIMARY KEY("game_id" AUTOINCREMENT)
                );
            """,
        },
        "insert_data": {
            "rounds_tb": """
                INSERT INTO "rounds_tb" (
                    "round_started", "round_ended", "diff",
                    "atts", "defined_num", "is_num_guessed",
                    "presumed_nums"
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            "game_tb": """
                
            """,
        },
    }

    def __init__(self, db_path: str = "data/database.sql") -> None:
        if "data" not in listdir("./"): mkdir("./data")
        self.db_path = db_path
        self.create_tb("rounds_tb")

    def connect(self) -> None:
        self.connection = sql.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def disconnect(self) -> None:
        self.cursor.close()
        self.connection.close()

    def create_tb(self, tb_name: str) -> None:
        self.connect()
        request = self.requests["create_tb"][tb_name]
        self.cursor.execute(request)
        self.disconnect()

    def insert_data(self, tb_name: str, data: tuple) -> None:
        self.connect(self.db_path)
        request = self.requests["insert_data"][tb_name]
        self.cursor.execute(request, data)
        self.connection.commit()
        self.disconnect()


if __name__ == "__main__":
    pass
else:
    import sqlite3 as sql
    
    from os import mkdir, listdir
