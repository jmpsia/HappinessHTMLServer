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
    year = request.args.get("year")
    rank = request.args.get("rank", 1, type=int)
    country = request.args.get("country", "")
    score = request.args.get("score")
    gdp = request.args.get("gdp")
    life_expectancy = request.args.get("lifeExpectancy")
    freedom = request.args.get("freedom")
    generosity = request.args.get("generosity")
    corruption = request.args.get("corruption")
    social_support = request.args.get("socialSupport")

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
        for name, value in params.items():
            if value is not None:
                headers.append(name)
        return headers

    def select():
        sql_select = "Select "
        for count, i in enumerate(headers()):
            sql_select += (i + ", ") if count is not len(headers())-1 else i
        print(sql_select)
        return sql_select + " from happiness order by rank"
    
    
    with conn.cursor() as cur:
        cur.execute(select())
        results = list(cur.fetchall())
        cur.execute(countries())
        my_countries = list(cur.fetchall())

    print(results)
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


