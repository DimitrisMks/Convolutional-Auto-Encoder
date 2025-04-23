from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago


# Define the DAG
with DAG(
    dag_id='nasa_apod_postgres',
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False,
)   as dag:

    ## step 1: Create the table for the data if it doesnt exitst
    @task
    def create_table():
        ##initialize PostgresHook
        postgres_hook = PostgresHook(postgres_conn_id='δε')

        create_table_query="""
        CREATE TABLE IF NOT EXISTS apod_data (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE UNIQUE,
            media_type VARCHAR(50)
            
            );
            
        
        """

        ## Execute the table creation query
        postgres_hook.run(create_table_query)
    ## Step 2: Extract the NASA API Data(apod= AstronomicPictureOftheDay)
    extract_apod = SimpleHttpOperator(
        task_id='extract_apod',
        http_conn_id='nasa_api',  ## Connection ID Defined In Airflow for  NAA API
        endpoint='planetary/apod', ## NASA API endpoint for APOD
        method = 'GET',
        data = {"api_key": "{{conn.nasa_api.extra_dejson.api_key}}"},
        response_filter = lambda response: response.json() ##Convert response to json
    )
    ## Step 3: Transform the data
    @task
    def transform_apod_data(response):
        apod_data ={
            'title':response.get('title', ''),
            'explanation':response.get('explanation', ''),
            'url':response.get('url', ''),
            'date':response.get('date', ''),
            'media_type':response.get('media_type', ''),
        }
        return apod_data
    ## Step 4: Load the data into Postgres SQL
    @task
    def load_data_to_postgres(apo_data):
        ##initialize the PosgresHook
        postgres_hook = PostgresHook(postgres_conn_id='my_postgres_connection')

        ## Define the SQL Insert Query
        insert_query="""
        INSERT INTO apod_data (title, explanation, url, date, media_type)
        VALUES (%s, %s, %s, %s, %s)
        """
        ## Execute the Query
        postgres_hook.run(insert_query,parameters=(
            apo_data['title'],
            apo_data['explanation'],
            apo_data['url'],
            apo_data['date'],
            apo_data['media_type']
        ))
    ## Step 5: Verify the data

    ## Step 6: Define  the task dependancies
    create_table() >> extract_apod
    api_response = extract_apod.output
    transform_data=transform_apod_data(api_response)
    load_data_to_postgres(transform_data)


