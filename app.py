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


@app.route("/webpage")
def render_page():
    country_bool = request.args.get("country_bool", "")
    score_bool = request.args.get("score_bool")
    gdp_bool = request.args.get("gdp_bool")
    life_expectancy_bool = request.args.get("life_expectancy_bool")
    freedom_bool = request.args.get("freedom_bool")
    generosity_bool = request.args.get("generosity_bool")
    corruption_bool = request.args.get("corruption_bool")
    social_support_bool = request.args.get("social_support_bool")
    year = request.args.get("year", type=int)
    rank = request.args.get("rank", type=int)
    country = request.args.get("country", "-1" if not country_bool else "1")
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

    def select_dumb():
        sql_select_py = "select rank, "
        cat2 =()
        for cat in params:
            print(cat)
            cat2 += (cat) if not cat == -1 or not cat == 1 else ("")
            
        sql_select_py += str.join(', ', cat2)
        return sql_select_py
    

    def select():
        cat2 = []
        sql_select = "Select rank"
        for cat in params:
            print(cat)
            if cat != -1 and cat != 1 and cat != year and cat != rank:
                cat2.append(cat)
        for i in cat2:
            sql_select += ", " + i
        return sql_select
        # does this mean that the result has to have the rank?
        # should rank be part of the checkbox mechanism if so

    def combine():
        return select() + " from happiness"

    
    with conn.cursor() as cur:
        cur.execute(combine())
        results = list(cur.fetchall())


    return render_template(
        "webpage.html",
        params=request.args,
        results_one=results)

# ,
#         result_count=count,
#         sets=results


