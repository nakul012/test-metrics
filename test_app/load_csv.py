# Run these command on SQL Shell(psql) to load data from csv to postgres database

''''
COPY test_app_metrics (time, voltage, current)
FROM 'C:\Program Files\PostgreSQL\15\data\CV.csv'
DELIMITER ',' CSV HEADER;

'''
