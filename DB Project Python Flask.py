from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL 
from collections import defaultdict
from datetime import datetime
import json
import calendar


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cs6400mysql' # Note: different password for Derrick
app.config['MYSQL_DATABASE_DB'] = 'cs6400'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_SQL_MODE'] = 'TRADITIONAL'
mysql.init_app(app)

@app.route('/')
def home():
    cursor = mysql.connect().cursor()
    
    payload = {}

    cursor.execute("SELECT COUNT(*) FROM Store")
    store_count = cursor.fetchone()
    payload["store_count"] = "{:,}".format(store_count[0]) 

    cursor.execute("SELECT COUNT(*) FROM Store WHERE Has_Restaurant = TRUE or Has_Snack_Bar = TRUE")
    stores_with_food_count = cursor.fetchone()
    payload["stores_with_food_count"] = "{:,}".format(stores_with_food_count[0])

    cursor.execute("SELECT COUNT(*) FROM Store WHERE Time_Limit > 0")
    stores_with_child_care_count = cursor.fetchone()
    payload["stores_with_child_care_count"] = "{:,}".format(stores_with_child_care_count[0])

    cursor.execute("SELECT COUNT(*) FROM Product")
    product_count = cursor.fetchone()
    payload["product_count"] = "{:,}".format(product_count[0])

    cursor.execute("SELECT COUNT(DISTINCT Description) FROM Campaigns")
    campaigns_count = cursor.fetchone()
    payload["campaigns_count"] = "{:,}".format(campaigns_count[0])

    cursor.execute("SELECT City_Name, State, Population FROM City")
    payload["cities"] = list()
    for city in cursor.fetchall():
        payload["cities"].append({"city_name": '{}, {}'.format(city[0], city[1]), "population": "{:,}".format(city[2])})

    cursor.execute("SELECT * FROM Holidays")
    payload["holidays"] = list()
    for holiday in cursor.fetchall():
        payload["holidays"].append({"name": holiday[0], "date": holiday[1]})

    error_message = request.args.get('error')
    if error_message:
        payload["error_message"] = error_message

    return render_template('main.html', active='home', data=payload)

@app.route('/edit_city')
def edit_city():

    mydb = mysql.connect()
    cursor = mydb.cursor()

    payload = {}

    selected_city_and_state = request.args.get('city')
    population = request.args.get('population')
    if selected_city_and_state and population:
        split = selected_city_and_state.find(',')
        city = selected_city_and_state[:split]
        state = selected_city_and_state[split+1:]

        # input check, make sure population is a valid number >= 0.
        try:
          population = int(population)
          if population < 0:
            raise ValueError('Invalid population value')
        except Exception as ex:
          return redirect(url_for('home', error="Invalid input to edit {} population".format(selected_city_and_state)))


        query_string = "UPDATE City SET Population = %s WHERE City_Name = %s AND State = %s"
        cursor.execute(query_string, (population, city, state))
        mydb.commit()

        return redirect(url_for('home'))

    else:
        cursor.execute("SELECT City_Name, State FROM City")
        payload["cities"] = list()
        for city in cursor.fetchall():
            city_name = city[0]
            state = city[1]
            payload["cities"].append('{},{}'.format(city_name, state))
        
        return render_template('edit_city.html', active='home', data=payload)

@app.route('/edit_holidays')
def edit_holidays():

    # date format from request: YYYY-MM-DD
    selected_date = request.args.get('holiday-date')
    new_holiday = request.args.get('name')
    if selected_date and new_holiday:

        mydb = mysql.connect()
        cursor = mydb.cursor()

        cursor.execute("SELECT Name FROM Holidays WHERE Unique_Date = %s", (selected_date,))
        row = cursor.fetchone()
        if row:
            # there is already a holiday with the associated date, update if needed
            holiday_list = row[0].split(',')
            if new_holiday not in holiday_list:
                # holiday does not already exist at this date, append to existing name
                holiday_list.append(new_holiday)
                holiday_string = ','.join(holiday_list)
                query_string = "UPDATE Holidays SET Name = %s WHERE Unique_Date = %s"
                cursor.execute(query_string, (holiday_string, selected_date))
                mydb.commit()
                return redirect(url_for('home'))
            else:
                # holiday already exists, show error
                return redirect(url_for('home', error="{} is already a holiday at {}".format(new_holiday, selected_date)))
        else:
            # there is no holiday at this date. Create date if needed, then create the holiday
            cursor.execute("SELECT Unique_Date FROM Date WHERE Unique_Date = %s", (selected_date))
            row = cursor.fetchone()
            if not row:
                # this date does not exist in the Date table, add it
                query_string = "INSERT INTO Date (Unique_Date) VALUES (%s)"
                cursor.execute(query_string, (selected_date,))
                mydb.commit()

            query_string = "INSERT INTO Holidays (Name, Unique_Date) VALUES (%s, %s)"
            cursor.execute(query_string, (new_holiday, selected_date))
            mydb.commit()

        return redirect(url_for('home'))

    return render_template('edit_holidays.html', active='home')

@app.route('/report_1')
def report_1():
    cursor = mysql.connect().cursor()
    
    payload = {}
    payload["category_report"] = list()

    cursor.execute('''
       SELECT 
            Category.Name, 
            COUNT(DISTINCT assigned_category.PID) AS CategoryCount, 
            MIN(Product.Retail_Price) AS Min_Retail_Price, 
            ROUND(AVG(Product.Retail_Price), 2) AS Avg_Retail_Price, 
            MAX(Product.Retail_Price) AS Max_Retail_Price 
        FROM Assigned_Category 
        INNER JOIN Category ON Category.Name = Assigned_Category.Name 
        LEFT JOIN Product ON Assigned_Category.PID = Product.PID 
        GROUP BY Category.Name 
        ORDER BY Category.Name ASC
    ''')
    for row in cursor.fetchall():
        payload["category_report"].append({
            "category_name" :row[0], 
            "category_count": "{:,}".format(row[1]),
            "min_retail_price": "${:,.2f}".format(row[2]),
            "avg_retail_price": "${:,.2f}".format(row[3]),
            "max_retail_price": "${:,.2f}".format(row[4])
        })

    return render_template('report_1.html', active='report_1', data=payload)

@app.route('/report_2')
def report_2():
    cursor = mysql.connect().cursor()

    payload = {}
    payload["predicted_revenue_report"] = list()

    cursor.execute('''
        SELECT
            Product.PID,
            Product.Name,
            FORMAT(Product.Retail_Price, 2) AS Retail_Price,
            FORMAT(SUM(Sale.Quantity), 0) AS Total_Units,
            SUM(CASE WHEN Discount.Discount_Price IS NOT NULL
                THEN Sale.Quantity ELSE 0 END) AS Units_At_Discount,
            SUM(CASE WHEN Discount.Discount_Price IS NULL
                THEN Sale.Quantity ELSE 0 END) AS Units_At_Retail,
            FORMAT(SUM(CASE WHEN Discount.Discount_Price IS NOT NULL
                        THEN (Discount.Discount_Price * Sale.Quantity)
                        ELSE (Product.Retail_Price * Sale.Quantity) END), 2) AS Actual_Revenue,
            FORMAT(SUM(CASE WHEN Discount.Discount_Price IS NOT NULL
                        THEN (Product.Retail_Price * Sale.Quantity * 0.75)
                        ELSE (Product.Retail_Price * Sale.Quantity) END), 2) AS Predicted_Revenue,
            SUM(CASE WHEN Discount.Discount_Price IS NOT NULL
                        THEN (Discount.Discount_Price * Sale.Quantity)
                        ELSE (Product.Retail_Price * Sale.Quantity) END)
            -SUM(CASE WHEN Discount.Discount_Price IS NOT NULL
                    THEN (Product.Retail_Price * Sale.Quantity * 0.75)
                    ELSE (Product.Retail_Price * Sale.Quantity) END) AS DIFFERENCE
        FROM Product
        INNER JOIN Assigned_Category ON Assigned_Category.PID = Product.PID
        INNER JOIN Sale ON Sale.PID = Product.PID
        LEFT JOIN Discount ON Product.PID = Discount.PID AND Sale.Unique_Date = Discount.Unique_Date
        WHERE Assigned_Category.NAME = "Couches and Sofas"
        GROUP BY Product.PID
        HAVING DIFFERENCE > 5000 OR DIFFERENCE < -5000
        ORDER BY DIFFERENCE DESC;
        ''')
    for row in cursor.fetchall():
        payload["predicted_revenue_report"].append({
            "product_pid": row[0],
            "product_name": row[1],
            "product_retail_price": "${:}".format(row[2]),
            "total_units": row[3],
            "units_at_discount": row[4],
            "units_at_retail": row[5],
            "actual_revenue": "${:}".format(row[6]),
            "predicted_revenue": "${:}".format(row[7]),
            "revenue_difference": "${:,.2f}".format(row[8])
        })

    return render_template('report_2.html', active='report_2', data=payload)

@app.route('/report_3')
def report_3():

    cursor = mysql.connect().cursor()

    payload = defaultdict(list)

    cursor.execute("SELECT DISTINCT State FROM City ORDER BY State ASC")
    for state in cursor.fetchall():
        payload["states"].append(state[0])

    selected_state = request.args.get('state')
    if selected_state:
        payload["selected_state"] = selected_state
        payload["results"] = list()
        query_string = '''
            SELECT
                Store.Store_Number,
                Store.Street_Address,
                City.City_Name,
                SUM(CASE WHEN Discount.Discount_Price IS NOT NULL THEN (Discount.Discount_Price * Sale.Quantity) ELSE (Product.Retail_Price * Sale.Quantity) END) AS Revenue,
                YEAR(Sale.Unique_Date) AS Year
            FROM Store
            INNER JOIN City ON City.State = Store.State AND City.City_Name = Store.City_Name 
            INNER JOIN Sale ON Store.Store_Number = Sale.Store_Number
            INNER JOIN Product ON Product.PID = Sale.PID
            LEFT JOIN Discount ON Discount.PID = Sale.PID AND Discount.Unique_Date = Sale.Unique_Date
            WHERE Store.State = %s
            GROUP BY Store.Store_Number, Year
            ORDER BY Year ASC, Revenue DESC
        '''
        cursor.execute(query_string, (selected_state,))
        for row in cursor.fetchall():
            payload["results"].append({
                "store_number": row[0],
                "address": row[1],
                "city": row[2],
                "revenue": "${:,.2f}".format(row[3]),
                "year": row[4]
            })
    return render_template('report_3.html', active='report_3', data=dict(payload))

@app.route('/report_4')
def report_4():
    cursor = mysql.connect().cursor()

    ordered_years = list()
    total_sales = defaultdict(dict)
    average_sales = defaultdict(dict)
    gh_sales = defaultdict(dict)
    cursor.execute('''
        SELECT
            YEAR(Sale.Unique_Date) AS Year,
            SUM(Sale.Quantity) AS Quantity,
            SUM(Sale.Quantity)/365 AS Avg_Quantity
        FROM Sale
        INNER JOIN Product ON Product.PID = Sale.PID
        INNER JOIN Assigned_Category ON Assigned_Category.PID = Product.PID WHERE Assigned_Category.Name = "Outdoor Furniture"
        GROUP BY Year
        ORDER BY Year ASC;
    ''')
    for row in cursor.fetchall():
        year = row[0]
        total_quantity = row[1]
        avg_quantity = row[2]
        ordered_years.append(year)
        total_sales[year]["quantity"] = total_quantity
        average_sales[year]["quantity"] = avg_quantity
        gh_sales[year]["quantity"] = 0
    
    cursor.execute('''
        SELECT
            YEAR(Sale.Unique_Date) AS Year,
            SUM(Sale.Quantity) AS GH_Quantity
        FROM Sale
        INNER JOIN Product ON Product.PID = Sale.PID
        INNER JOIN Assigned_Category ON Assigned_Category.PID = Product.PID WHERE Assigned_Category.Name = "Outdoor Furniture"
        AND MONTH(Sale.Unique_Date) = 2 AND DAY(Sale.Unique_Date) = 2 GROUP BY Year
        ORDER BY Year ASC;
    ''')
    for row in cursor.fetchall():
        year = row[0]
        gh_quantity = row[1]
        gh_sales[year]["quantity"] = gh_quantity

    payload = list()
    for year in ordered_years:
        payload.append({
            "year": year,
            "total_quantity": "{:,}".format(total_sales[year]["quantity"]),
            "avg_quantity": "{:,.2f}".format(average_sales[year]["quantity"]),
            "gh_quantity": "{:,}".format(gh_sales[year]["quantity"])
        })

    return render_template('report_4.html', active='report_4', data=payload)

@app.route('/report_5')
def report_5():
    cursor = mysql.connect().cursor()

    payload = {}

    cursor.execute("SELECT Unique_Date FROM Date")
    payload["months"] = list()
    for row in cursor.fetchall():
        date = row[0]
        date_string = date.strftime("%Y-%m")
        if date_string not in payload["months"]:
            payload["months"].append(date_string)

    selected_month_and_year = request.args.get('month_year')
    if selected_month_and_year:
        payload["selected_month_and_year"] = selected_month_and_year
        year = int(selected_month_and_year[:4])
        month = int(selected_month_and_year[5:])
        query_string = '''
            SELECT
                TB1.Name AS Category_Name,
                TB1.State AS State_Name,
                SUM(TB1.Quantity) AS Highest_Volume
            FROM(
                SELECT
                    Assigned_Category.Name,
                    Store.State,
                    Sale.Quantity,
                    Sale.Unique_Date
                FROM Store
                INNER JOIN Sale ON Store.Store_Number = Sale.Store_Number
                INNER JOIN Product ON Product.PID = Sale.PID
                INNER JOIN Assigned_Category ON Product.PID = Assigned_Category.PID
            ) AS TB1
            WHERE Year(TB1.Unique_Date) = %s
            AND Month(TB1.Unique_Date) = %s
            GROUP BY TB1.Name, TB1.State
            ORDER BY TB1.Name;
        '''
        cursor.execute(query_string, (year, month))

        categories = dict()
        ordered_categories = list()
        for row in cursor.fetchall():
            category, state, volume = row
            if category not in ordered_categories:
                ordered_categories.append(category)

            if not categories.get(category):
                categories[category] = [{"category_name": category, "state": state, "volume": volume}]
            elif categories[category][0]["volume"] < volume:
                categories[category] = [{"category_name": category, "state": state, "volume": volume}]
            elif categories[category][0]["volume"] == volume:
                categories[category].append({"category_name": category, "state": state, "volume": volume})

        payload["categories"] = list()
        for category in ordered_categories:
            payload["categories"].extend(categories[category])

    return render_template('report_5.html', active='report_5', data = payload)

@app.route('/report_6')
def report_6():
    cursor = mysql.connect().cursor()

    payload = {}

    cursor.execute('''
        SELECT
            TB3.Year,
            SUM(TB3.Small_Rev) AS Small,
            SUM(TB3.Med_Rev) AS Medium,
            SUM(TB3.Large_Rev) AS Large,
            SUM(TB3.XL_Rev) AS Extra_Large
        FROM(
            SELECT
                TB2.Year,
                CASE
                WHEN TB2.Population < 3700000 THEN TB2.Revenue
                ELSE NULL
                END AS Small_Rev,
                CASE
                WHEN TB2.Population >= 3700000 AND TB2.Population < 6700000 THEN
                TB2.Revenue ELSE NULL
                END AS Med_Rev,
                CASE
                WHEN TB2.Population >= 6700000 AND TB2.Population < 9000000 THEN
                TB2.Revenue ELSE NULL
                END AS Large_Rev,
                CASE
                WHEN TB2.Population >= 9000000 THEN TB2.Revenue
                ELSE NULL
                END AS XL_Rev
            FROM(
                SELECT
                    TB1.City_Name,
                    TB1.State,
                    TB1.Population,
                    Year(TB1.Unique_Date) AS Year,
                    CASE
                    WHEN TB1.Discount_Price IS NOT NULL THEN (TB1.Discount_Price * TB1.Quantity)
                    ELSE (TB1.Retail_Price * TB1.Quantity)
                    END AS Revenue
                FROM(
                    SELECT City.City_Name, City.State, City.Population, Sale.Unique_Date,
                        Discount.Discount_Price, Sale.Quantity, Product.Retail_Price
                    FROM Sale
                    INNER JOIN Store ON Store.Store_Number = Sale.Store_Number
                    INNER JOIN City ON Store.City_Name = City.City_Name
                    INNER JOIN Product ON Sale.PID = Product.PID
                    LEFT JOIN Discount ON Product.PID = Discount.PID AND Discount.Unique_Date = Sale.Unique_Date
                ) AS TB1
            ) AS TB2
        ) AS TB3
        GROUP BY Year
        ORDER BY Year
    ''')

    payload["revenue_by_population"] = list()
    for row in cursor.fetchall():
        payload["revenue_by_population"].append({
            "year" : row[0], 
            "small" : "${:,.2f}".format(row[1] if row[1] else 0),
            "medium" : "${:,.2f}".format(row[2] if row[2] else 0),
            "large" : "${:,.2f}".format(row[3] if row[3] else 0),
            "extra_large" : "${:,.2f}".format(row[4] if row[4] else 0)
        })

    return render_template('report_6.html', active='report_6', data = payload)

@app.route('/report_7')
def report_7():
    cursor = mysql.connect().cursor()

    payload = {}

    cursor.execute('''
        SELECT
            Store.Time_Limit,
            MONTH(Sale.Unique_Date) AS Sales_Month,
            SUM(CASE
                WHEN Sale.Unique_Date > SUBDATE((SELECT MAX(Sale.Unique_Date) FROM Sale), INTERVAL 365 DAY)
                THEN 
                    CASE        
                    WHEN Discount.Discount_Price IS NOT NULL 
                    THEN (Discount.Discount_Price * Sale.Quantity)
                    ELSE (Product.Retail_Price * Sale.Quantity)
                    END
                ELSE 0    
            END ) AS Revenue
        FROM Sale
        INNER JOIN Store ON Store.Store_Number = Sale.Store_Number
        INNER JOIN Childcare ON Childcare.Time_Limit = Store.Time_Limit
        INNER JOIN Product ON Sale.PID = Product.PID
        LEFT JOIN Discount ON Product.PID = Discount.PID AND Sale.Unique_Date = Discount.Unique_Date
        GROUP BY Store.Time_Limit, Sales_Month
        ORDER BY Sales_Month, Store.Time_Limit ASC;
    ''')

    current_month = None
    payload["childcare_sales_volume"] = list()
    for row in cursor.fetchall():
        time_limit, sales_month, revenue = row
        if current_month != sales_month:
            current_month = sales_month
            payload["childcare_sales_volume"].append({
                "month": calendar.month_name[sales_month]
            })
        payload["childcare_sales_volume"][-1][str(time_limit)] = "${:,.2f}".format(revenue)

    return render_template('report_7.html', active='report_7', data = payload)

@app.route('/report_8')
def report_8():
    cursor = mysql.connect().cursor()

    payload = list()
    
    cursor.execute('''
        SELECT 
            WITH_FOOD.Name,
            WITH_FOOD.With_Food_Quantity,
            NO_FOOD.No_Food_Quantity
        FROM ( 
            SELECT
                Assigned_Category.Name,
                SUM(Sale.Quantity) AS No_Food_Quantity
            FROM Store
            INNER JOIN Sale ON Store.Store_Number = Sale.Store_Number
            INNER JOIN Product ON Product.PID = Sale.PID
            INNER JOIN Assigned_Category ON Assigned_Category.PID = Product.PID 
            WHERE Store.Has_Restaurant = FALSE
            GROUP BY Assigned_Category.Name
        ) AS NO_FOOD
        INNER JOIN ( 
            SELECT
                Assigned_Category.Name,
                SUM(Sale.Quantity) AS With_Food_Quantity
            FROM Store
            INNER JOIN Sale ON Store.Store_Number = Sale.Store_Number
            INNER JOIN Product ON Product.PID = Sale.PID
            INNER JOIN Assigned_Category ON Assigned_Category.PID = Product.PID 
            WHERE Store.Has_Restaurant = TRUE
            GROUP BY Assigned_Category.Name
        ) AS WITH_FOOD
        ON NO_FOOD.Name = WITH_FOOD.Name
        ORDER BY Name ASC
    ''')
    for row in cursor.fetchall():
        category, with_food_quantity, no_food_quantity = row
        payload.append({
            "category": category, 
            "without_restaurant_sales": "{:,}".format(no_food_quantity),
            "with_restaurant_sales": "{:,}".format(with_food_quantity)
        })

    return render_template('report_8.html', active='report_8', data=payload)

@app.route('/report_9')
def report_9():
    cursor = mysql.connect().cursor()

    payload = list()

    cursor.execute('''
        SELECT 
            A.PID,
            A.Product_Name,
            A.With_Campaign_Quantity,
            B.Without_Campaign_Quantity,
            A.With_Campaign_Quantity - B.Without_Campaign_Quantity AS Difference
        FROM ( 
            SELECT 
                Product.PID AS PID,
                Product.Name AS Product_Name, 
                SUM(Sale.Quantity) AS With_Campaign_Quantity
            FROM Sale
            INNER JOIN Product ON Product.PID = Sale.PID
            INNER JOIN Discount ON Discount.PID = Sale.PID AND Sale.Unique_Date = Discount.Unique_Date
            LEFT JOIN Campaign_Date ON Sale.Unique_Date = Campaign_Date.Unique_Date WHERE Campaign_Date.Unique_Date IS NOT NULL
            GROUP BY Product.PID
        ) AS A
        INNER JOIN ( 
            SELECT 
                Product.PID AS PID,
                Product.Name AS Product_Name, 
                SUM(Sale.Quantity) AS Without_Campaign_Quantity
            FROM Sale
            INNER JOIN Product ON Product.PID = Sale.PID
            INNER JOIN Discount ON Discount.PID = Sale.PID AND Sale.Unique_Date = Discount.Unique_Date
            LEFT JOIN Campaign_Date ON Sale.Unique_Date = Campaign_Date.Unique_Date WHERE Campaign_Date.Unique_Date IS NULL
            GROUP BY Product.PID
        ) AS B
        ON A.PID = B.PID
        ORDER BY Difference DESC
    ''')
    for row in cursor.fetchall():
        payload.append({
            "pid": row[0],
            "name": row[1],
            "quantity_campaign_on": "{:,}".format(row[2]),
            "quantity_campaign_off": "{:,}".format(row[3]),
            "difference": "{:,}".format(row[4])
        })
    
    payload = payload[:10] + payload[-10:]

    return render_template('report_9.html', active='report_9', data=payload)
