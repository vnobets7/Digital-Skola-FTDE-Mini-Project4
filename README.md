![image](https://github.com/vnobets7/Digital-Skola-FTDE-Mini-Project4/blob/main/images/kafka-icon.png)

# Digital-Skola-FTDE-Mini-Project4
## Deskripsi Mini-Project3
Bagian dari tugas Fast-Track homework, yang merupakan tugas individual. Membuat Stream data processing menggunakan apache kafka, lalu melakukan prediksi machine learning dengan python(sklearn), dan data hasil prediksi disimpan di mongoDB.

## Data stack
- Postgres (source)
- Dbeaver
- MongoDB 
- MongoDB compass
- Docker/Docker desktop/WSL2+Ubuntu+Docker
- Sklearn library
- Pandas library
- Sqlalchemy library
- Pymongo library
- Apache kafka

##  Simple Project Architecture
Berikut ini merupakan ilustrasi dari project yang dibuat. <br>
![Project Architecture](https://github.com/vnobets7/Digital-Skola-FTDE-Mini-Project4/blob/main/images/SS-project-8-flow-project-edit.PNG)

## Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/vnobets7/Digital-Skola-FTDE-Mini-Project4.git
    ```

2. Navigate to the project directory:
   ```
   cd Digital-Skola-FTDE-Mini-Project4
   ```

3. Starts the containers in the background
   ```
   docker compose up -d
   ```

4. Make sure that no containers are in an good condition
   ```
   docker ps
   ```

5. Set db connection (source)
* postgresDB
   ```
   create database connection postgres DB on dbeaver
   ```
* mongoDB
   ```
   create database connection mongo DB on mongo compass
   ```

6. Create ananconda python environment (i'm use miniconda instead ananconda)
   ```
   conda create -n <insert_name> python <python_version>
   ```

7. Activate ananconda environment on local computer
   ```
   conda activate <insert_name>
   ```

8. Install all necessary python library on requirements.txt
   ```
   pip install -r requirements. txt
   ```

9. Run producer.py to send message contain data 'new_information.csv'
   ```
   python producer.py
   ```

10. Run Tes-consumer.ipynb for recieve message from consumer and save into mongoDB

11. Run datadump.ipynb to ingest data into postgreSQL

12. Run modelling.ipynb to start machine leanring model for fraud detection
