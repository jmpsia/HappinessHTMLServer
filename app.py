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


@app.route("/set")
def render_sets():
    year = request.args.get("year", type=int)
    rank = request.args.get("rank", type=int)
    country = request.args.get("country", "")
    score = request.args.get("score", type=float)
    gdp = request.args.get("gdp", type=float)
    life_expectancy = request.args.get("life_expectancy", type=float)
    freedom = request.args.get("freedom", type=float)
    generosity = request.args.get("generosity", type=float)
    corruption = request.args.get("corruption", type=float)
    social_support = request.arg.get("social_support", type=float)

    #things we will need for the website..
    #sort_by = request.args.get("sort_by", "set_name")
    #sort_dir = request.args.get("sort_dir", "asc")
    #no pagination please

    params = {
        "year": year;
        "rank": rank;
        "country": country;
        "score": score;
        "gdp": gdp;
        "life_expectancy": life_expectancy;
        "freedom": freedom;
        "generosity": generosity;
        "corruption": corruption;
        "social_support": social_support;

        #"sort_by": sort_by
        #"sort_dir": sort_dir
    }

    from_where_clause =
        #INSERT SQL CODE
        
    #define methods we need for the variables, default

    with conn.cursor() as cur:
        cur.execute()#INSERTCODE)
        results = list(cur.fetchall())
        cur.execute()#INSERTCODE)
        count = cur.fetchone()["count"]


    return render_template(
        "sets.html",
        params=request.args,
        result_count=count,
        sets=results)


