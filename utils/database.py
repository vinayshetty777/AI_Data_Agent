import psycopg2


class DatabaseUtil:

    def __init__(self, db_config):
        self.db_config = db_config

        try: 
            self.connection = psycopg2.connect(**db_config) 

        except Exception as e:
            print(f"Error connecting to the database: {e}")
            self.connection = None

    def schema_details(self,schema_name):

        schema_info_context = ""

        connection = self.connection
        cursor = None

        if connection is None:
            return "Error: No database connection available"

        try:
            cursor = connection.cursor()
            schema_info_context = f"Database Schema: {schema_name}\n"

            cursor.execute("SELECT table_name from information_schema.tables where table_schema = %s;", (schema_name,))
            tables_list = cursor.fetchall()

            for table in tables_list:
                table_name = table[0]
                schema_info_context = f"{schema_info_context}\nTable: {table_name}\n"

                # Adding Columns & Data Types
                cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s;", (table_name,))
                columns_list = cursor.fetchall()

                for column in columns_list:
                    column_name = column[0]
                    data_type = column[1]
                    schema_info_context = f"{schema_info_context}  Column: {column_name}, Data Type: {data_type}\n"

                # Adding Sample Data
                cursor.execute(f"SELECT * FROM {schema_name}.{table_name} LIMIT 5;")
                sample_data = cursor.fetchall()
                schema_info_context = f"{schema_info_context}  Sample Data:\n"
                for row in sample_data:
                    schema_info_context = f"{schema_info_context}    {row}\n"

        except Exception as e:
            print(f"Error fetching schema details: {e}")
            schema_info_context = f"Error fetching schema details: {e}"

        finally:
            if cursor:
                cursor.close()

        return schema_info_context

    def execute_sql(self, query):
        connection = self.connection
        cursor = None

        if connection is None:
            error_msg = "Error: No database connection available"
            print(error_msg)
            return error_msg

        query = query.strip()
        if query.startswith("```"):
            query = query.split("\n", 1)[1]
        if query.endswith("```"):
            query = query.rsplit("\n", 1)[0]

        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            return str(result)
        except Exception as e:
            error_msg = f"Error executing query: {e}"
            print(error_msg)
            return error_msg
        finally:
            if cursor:
                cursor.close()


obj = DatabaseUtil({
    "database": "neondb",
    "host": "ep-weathered-haze-b5mwfpc2-pooler.c-7.us-east-2.aws.neon.tech",
    "user": "neondb_owner",
    "password": "npg_dzO3JjWk1vDF"
})

result = obj.schema_details("public")

with open("test_schema_details.txt", "w") as f:
    f.write(result)