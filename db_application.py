def db_select(start = 0, end = -1):
    """
    Selects the [start, end] row(s) of the database
    """
    try:
        db_file = open("db.txt", "r")
        db_lines = db_file.readlines()
        n_lines = len(db_lines)
        db_file.close()
    except:
        return ""

    try:
        start = int(start)
        start = max(start, 0)
        start = min(start, n_lines-1)
    except:
        start = 0
    try:
        end = int(end)
        end = min(end, n_lines-1)
        if end < 0:
            end = n_lines-1
    except:
        end = n_lines-1

    return ''.join(db_lines[start:end+1])
    
def db_insert(line):
    """
    Inserts a line into the database
    """
    if line == None:
        return False
    try:
        line = str(line)
        db_file = open("db.txt", "a")
        db_file.write(line+'\n')
        db_file.close()
        return True
    except:
        return False

def db_delete(num_lines=1):
    """
    Deletes the last num_lines lines from the database
    If num_lines = 0, it deletes all the lines
    """
    try:
        db_file = open("db.txt", "r")
        db_lines = db_file.readlines()
        n_lines = len(db_lines)
        db_file.close()
    except:
        return True

    try:
        num_lines = int(num_lines)
        num_lines = max(num_lines, 0)
        num_lines = min(num_lines, n_lines)
    except:
        num_lines = 1

    try:
        db_file = open("db.txt", "w")
        db_file.writelines(db_lines[:-num_lines])
        db_file.close()
        return True
    except:
        return False

