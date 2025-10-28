import psycopg2
from config import load_config

def write_blob(part_id, path_to_file, file_extension):
    """ Insert a BLOB into a table """
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Read the file
                with open(path_to_file, 'rb') as file:
                    drawing_data = file.read()
                
                # Insert into database
                cur.execute(
                    "INSERT INTO part_drawings(part_id, file_extension, drawing_data) "
                    "VALUES(%s, %s, %s)",
                    (part_id, file_extension, psycopg2.Binary(drawing_data))
                )
                conn.commit()
                print(f"Blob inserted for part_id {part_id}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    write_blob(2, 'images.jpeg', '.jpeg')
