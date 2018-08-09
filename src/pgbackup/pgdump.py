import subprocess
import sys

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def dump_file_name(url, timestamp=None):
    db_name = url.split("/")[-1] # get last bit of url
    db_name = db_name.split("?")[0] # remove url params

    if timestamp:
        return f"{db_name}-{timestamp}.sql"

    return f"{db_name}.sql"
