import psycopg2
import math
from flask import Flask, request, render_template
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route("/webpage")
def render_sets():
    year = request.args.get("year", type=int)
    rank = request.args.get("rank", type=int)
    country = request.args.get("country", "")
    score = request.args.get("score")
    gdp = request.args.get("gdp")
    life_expectancy = request.args.get("life_expectancy")
    freedom = request.args.get("freedom")
    generosity = request.args.get("generosity")
    corruption = request.args.get("corruption")
    social_support = request.args.get("social_support")
    sort_by = request.args.get("sort_by", "rank")
    choice = request.args.get("choice", "gdp")


    #things we will need for the website..
    #sort_by = request.args.get("sort_by", "set_name")
    #sort_dir = request.args.get("sort_dir", "asc")
    #no pagination please

    params = {
        "year": year,
        "rank": rank,
        "country": country,
        "score": score,
        "gdp": gdp,
        "life_expectancy": life_expectancy,
        "freedom": freedom,
        "generosity": generosity,
        "corruption": corruption,
        "social_support": social_support,
        "choice": f"%{choice}%"

        #"sort_by": sort_by
        #"sort_dir": sort_dir
    }

    sql_clause = """
        select rank, year, country, score, choice
        """
        #INSERT SQL CODE
        
    #define methods we need for the variables, default

    # with conn.cursor() as cur:
    #     cur.execute()#INSERTCODE)
    #     results = list(cur.fetchall())
    #     cur.execute()#INSERTCODE)
    #     count = cur.fetchone()["count"]


    return render_template(
        "webpage.html",
        params=request.args)

# ,
#         result_count=count,
#         sets=results


