# MealGuru
AI chatbot specalized in resturants 
===================================

Getting started with PostgreSQL (Windows CMD)
```bash
    psql -U postgres
```
``` bash
    createdb mydb
```
```bash
    \c mydb
```
```bash
    GRANT ALL PRIVILEGES ON DATABASE mydb to mydb;
```
Troubleshoot tips 
```bash
    >>>import psycopg2
```
```bash
    >>>psycopg2.connect("dbname=postgres user=postgres host=localhost password=oracle port=5432")
```

To test localy 
```bash
    uvicorn main:app --reload
```

Test with Ngrok
```bash
    ngrok http 8000
```

Userfull links:
    [Inspiration](https://www.twilio.com/en-us/blog/ai-chatbot-whatsapp-python-twilio-openai)
    [Userfull API Info](https://www.twilio.com/docs/messaging/api/message-resource)
    [Troubleshhoting](https://stackoverflow.com/questions/69934467/error-while-using-createdb-command-postgresql-on-windows-10)
    [Troubleshhoting](https://stackoverflow.com/questions/48999379/psycopg2-operationalerror-fatal-password-authentication-failed-for-user-my-u)
    [Troubleshooting](https://stackoverflow.com/questions/60138692/sqlalchemy-psycopg2-errors-insufficientprivilege-permission-denied-for-relation)