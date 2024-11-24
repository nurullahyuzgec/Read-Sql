import mysql.connector

__author__ = 'Nurullah Yuzgec'

connect = mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="password",
    db="information_schema"

    )
database_name = connect.database
cursor = connect.cursor()
if connect.is_connected():
    print('[*] - Database Connected Successfully')
else:
    print('[*] - Database Connection Failed')


def data_check():
    cursor.execute("SHOW TABLES;")
    results = cursor.fetchall()
    
    table_string = ""
    table_string += str(results[0][0]) + "\n"
    
    for tables in results[1:]:   
        table_string += "\t" + "\t" + str(tables[0]) + "\n"
        
    print(f"""
          ------------------------------------------------------------
                            Tables in {database_name}              
          ------------------------------------------------------------
           {table_string}
          
          """)
    
    select_table = input('[*] - Please The Select Table Name :')
    query = cursor.execute(f"SELECT * FROM {select_table}")
    results = cursor.fetchall()
    
    query_str =  ""
    query_str += str(results[0][0]) + "\n"
    if results:
        for row in results[1:]:
            count_index = len(row)
            for i in range(count_index):
                query_str += "\t" +  "\t" +  str(row[i])
            query_str += "\n"

        print(f"""
                ------------------------------------------------------------
                                    QUERY in {select_table}              
                ------------------------------------------------------------
                {query_str}
          
                """)
    else:
        print(f"[!] - No data found in {select_table} table.")
        
    again = input('[*] - Do You Want To Check Another Table? (Y/N): ')
    if again.lower() == 'y':
        data_check()
    else:
        cursor.close()
        connect.close()

data_check()
    