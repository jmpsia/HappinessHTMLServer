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
    return "Hey bitchessss!"


@app.route("/happiness")
def render_page():
    score_bool = request.args.get("score_bool", "1")
    gdp_bool = request.args.get("gdp_bool", "1")
    life_expectancy_bool = request.args.get("life_expectancy_bool", "1")
    freedom_bool = request.args.get("freedom_bool", "1")
    generosity_bool = request.args.get("generosity_bool", "1")
    corruption_bool = request.args.get("corruption_bool","1")
    social_support_bool = request.args.get("social_support_bool", "1")
    year = request.args.get("year", type=int)
    rank = request.args.get("rank", type=int)
    country = request.args.get("country")
    score = request.args.get("score", "-1" if not score_bool else "1")
    gdp = request.args.get("gdp", "-1" if not gdp_bool else "1")
    life_expectancy = request.args.get("life_expectancy", "-1" if not life_expectancy_bool else "1")
    freedom = request.args.get("freedom", "-1" if not freedom_bool else "1")
    generosity = request.args.get("generosity", "-1" if not generosity_bool else "1")
    corruption = request.args.get("corruption", "-1" if not corruption_bool else "1")
    social_support = request.args.get("social_support", "-1" if not social_support_bool else "1")

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
        "social_support": social_support

        #"sort_by": sort_by
        #"sort_dir": sort_dir
    }
    
    def countries():
        sql_statement = "Select country from happiness"
        return sql_statement


    def headers():
        headers = []
        for cat in params:
            print(cat)
            if not (cat == -1) and not (cat == year) and not (cat == rank) and not (cat == country):
                headers.append(cat)
        return headers

    def select():
        list = headers()
        sql_select = "Select rank"
        for i in list:
            sql_select += ", " + i
        return sql_select + " from happiness"
    
    with conn.cursor() as cur:
        cur.execute(select())
        results = list(cur.fetchall())
        cur.execute(countries())
        my_countries = list(cur.fetchall())

    c = my_countries
    h = headers()
    return render_template(
        "happiness.html",
        params=request.args,
        results_one=results,
        countries = c,
        headers = h
    )
# ,
#         result_count=count,
#         sets=results


