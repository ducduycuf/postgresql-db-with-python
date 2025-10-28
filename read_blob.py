import os
import psycopg2
from config import load_config

def read_blob(part_id, path_to_dir):
    """ Read BLOB data from a table """
    # read database configuration
    config = load_config()

    try:
        # Create directory if it doesn't exist
        os.makedirs(path_to_dir, exist_ok=True)
        
        # connect to the PostgresQL database
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the SELECT statement
                cur.execute(""" SELECT part_name, file_extension, drawing_data
                                FROM part_drawings
                                INNER JOIN parts on parts.part_id = part_drawings.part_id
                                WHERE parts.part_id = %s """,
                            (part_id,))

                blob = cur.fetchone()
                
                if blob:
                    # write blob data into file
                    file_path = path_to_dir + blob[0] + blob[1]
                    with open(file_path, 'wb') as file:
                        file.write(blob[2])
                    print(f"File saved to: {file_path}")
                else:
                    print(f"No blob found for part_id {part_id}")
                    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    read_blob(2, 'images/output/')
