import psycopg2
import json


class Database:
    import psycopg2

    @staticmethod
    def create_conn():
        try:
            conn = psycopg2.connect(
                "postgresql://housescraperdb_owner:NawQe2n7JBSP@ep-lucky-river-a2u5mie7.eu-central-1.aws.neon.tech/housescraperdb?sslmode=require&options=endpoint%3Dep-lucky-river-a2u5mie7"
            )
            print("Database connection established successfully!")
            return conn, conn.cursor()
        except psycopg2.OperationalError as e:
            print("Error: Could not connect to the database.")
            print(f"Details: {e}")


    @staticmethod
    def setup_sample_data():
        # Sample JSON data
        property_data = {
            "property_id": "f1a958df-ea94-41d5-bb87-ee50ff7c9520",
            "address_id": "0a3f50a2-bcc8-32b8-e044-0003ba298018",
            "price_cash": 4295000,
            "housing_area": 86,
            "city_name": "Frederiksberg",
            "json_data": {
                "address": {"cityName": "Frederiksberg", "roadName": "Roskildevej", "zipCode": 2000},
                "priceCash": 4295000,
                "housingArea": 86
            }
        }
        return property_data

    @staticmethod
    def insert_query(cursor, property_data):
        # Insert query
        insert_query = """
            INSERT INTO properties (property_id, address_id, price_cash, housing_area, city_name, json_data)
            VALUES (%s, %s, %s, %s, %s, %s::JSONB)
            ON CONFLICT (property_id) DO NOTHING;
        """

        cursor.execute(insert_query, (
            property_data['property_id'],
            property_data['address_id'],
            property_data['price_cash'],
            property_data['housing_area'],
            property_data['city_name'],
            json.dumps(property_data['json_data'])
        ))

    @staticmethod
    def close_connection(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()


def config_database():
    conn, cursor = Database.create_conn()
    property_data = Database.setup_sample_data()
    Database.insert_query(cursor, property_data)
    Database.close_connection(conn, cursor)
    print("Data inserted successfully!")
