# Spotify Data Engineering Project

## Overview:
This is an ETL project in which the data is extracted from the Spotify API and then transformed and loaded in S3. The transformed data is then used to generate insights related to artist information, album information etc.

## Technologies Used: 
### This project uses Python 3.8. and AWS cloud services listed below - 
- AWS Lambda: It is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you.
- AWS S3: It is an object storage service that stores data as objects within buckets. An object is a file and any metadata that describes the file. A bucket is a container for objects.
- Cloud Watch: Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time.
- AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.
- AWS Glue: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.

## Architecture Diagram: 

![Architecture diagram of Spotify ETL Project](https://github.com/Shrutimo/spotify-data-engineering-project/blob/main/Architecture%20Diagram.png)


