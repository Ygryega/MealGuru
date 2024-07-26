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

Userfull links:
    https://www.twilio.com/en-us/blog/ai-chatbot-whatsapp-python-twilio-openai
    https://stackoverflow.com/questions/69934467/error-while-using-createdb-command-postgresql-on-windows-10
    https://stackoverflow.com/questions/48999379/psycopg2-operationalerror-fatal-password-authentication-failed-for-user-my-u
    https://stackoverflow.com/questions/60138692/sqlalchemy-psycopg2-errors-insufficientprivilege-permission-denied-for-relation