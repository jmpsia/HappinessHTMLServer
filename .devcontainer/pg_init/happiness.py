from psycopg2.extensions import cursor

from utils import parse_int

#year,rank,country,score,gdp,life_expectancy,freedom,generosity,corruption,social_support
def populate_happiness(cur: cursor, rows: list[dict[str, str]]):
    for row in rows:
        happiness = (parse_int(row['year']), parse_int(row['rank']), row['country'], row['score'], 
                      row['gdp'], row['life_expectancy'], row['freedom'], row['generosity'], 
                        row['corruption'], row['social_support'])
        cur.execute("""
            insert into happiness(year, rank, country, score, gdp, life_expectancy, freedom, generosity, corruption, social_support)
            values(%s, %s,%s, %s, %s, %s, %s,%s, %s, %s)
            on conflict do nothing
            """, happiness)