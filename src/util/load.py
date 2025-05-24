import zipfile
import pandas as pd
from io import StringIO

import zipfile
import pandas as pd
from io import StringIO

def load_satcat_by_date(nb_level, date_name, dashdir='/'):
    """
    Load the 'satcat.csv' file for a specific date from a ZIP archive.

    Parameters:
    ----------
    nb_level : str
        Base path or directory level prefix leading to the 'data' folder.
    date_name : str
        The date string (e.g., '2024-01-01') used to identify the specific ZIP file and contents.
    dashdir : str, optional
        Directory separator to use when constructing file paths. Default is '/'.

    Returns:
    -------
    pd.DataFrame or None

    """
    with zipfile.ZipFile(nb_level + dashdir + "data" + dashdir + "by_date" + dashdir + date_name + '.zip') as z:
        sat_cat = None
        for file in z.namelist():
            if file.startswith(date_name) and file.endswith('satcat.csv'):
                with z.open(file) as f:
                    sat_cat = pd.read_csv(StringIO(f.read().decode('utf-8')))
        return sat_cat

def load_catalogs_by_date(nb_level, date_name, dashdir='/'):
    
    with zipfile.ZipFile(nb_level+dashdir+"data"+dashdir+"by_date"+dashdir+date_name+'.zip') as z:
        sat_cat = None
        state_cat = None
        for file in z.namelist():
            if file.startswith(date_name):
                if file.endswith('satcat.csv'):
                    with z.open(file) as f:
                        sat_cat = pd.read_csv(StringIO(f.read().decode('utf-8')))
                    
                elif file.endswith('statecat.csv'):
                    with z.open(file) as f:
                        state_cat = pd.read_csv(StringIO(f.read().decode('utf-8')), header=None, names=['TLE_LINE'] )
                    
        return sat_cat, state_cat