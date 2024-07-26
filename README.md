# MealGuru
AI chatbot specalized in resturants 

-1 Getting started with PostgreSQL (Windows CMD)
    psql -U postgres
    createdb mydb
    \c mydb
    GRANT ALL PRIVILEGES ON DATABASE mydb to mydb;
    - to troubleshoot (
        >>>import psycopg2
        >>>psycopg2.connect("dbname=postgres user=postgres host=localhost password=oracle port=5432")
    )

-2 To test localy 
    uvicorn main:app --reload

-3 Test with Ngrok
    ngrok http 8000