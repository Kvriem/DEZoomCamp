Green Taxi ETL Pipeline 

This repository contains the files for the Green Taxi ETL (Extract, Transform, Load) pipeline in response to the assigned task"https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/02-workflow-orchestration/homework.md".
Below is a detailed explanation of the components and procedures implemented in this pipeline:

    Pipeline Name:
        green_taxi_etl

    Data Loader Block:
        Utilizes Pandas to read data for the final quarter of 2020 (months 10, 11, 12).

    Transformer Block:
        Removes rows where the passenger count or trip distance is equal to zero.
        Creates a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
        Renames columns in Camel Case to Snake Case, e.g., VendorID to vendor_id.
        Includes two assertions:
            passenger_count is greater than 0.
            trip_distance is greater than 0.

    Postgres Data Exporter:
        Writes the dataset to a table called green_taxi in a schema mage.
