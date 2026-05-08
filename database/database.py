import aiosqlite

DB_NAME = "data/warnings.db"


async def setup_database():

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS warnings (
                guild_id INTEGER,
                user_id INTEGER,
                moderator_id INTEGER,
                reason TEXT
            )
            """
        )

        await db.commit()
