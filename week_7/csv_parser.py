"""
Write methods that can parse a CSV and a TSV.

CSV: comma-separated values
TSV: tab-separated values

@author: Alexandra DeLucia
"""


# Write this method first
def parse_csv(filename):
    """
    Parses a file with comma-separated values (CSV).
    
    Parameters
    ----------
    filename : path to file
    
    Returns
    --------
    list : multi-dimensional list of file content
    """
    # 1. Validate file. Is it a CSV?
    
    # 2. Open file and save lines
    
    # 3. Parse lines into list
    
    # 4. Return list
    return
    

# Can you use the same concepts to write this method?
def parse_tsv(filename):
    """
    Parses a file with tab-separated values (TSV).
    
    Parameters
    ----------
    filename : path to file
    
    Returns
    --------
    list : multi-dimensional list of file content
    """
    return


if __name__ == "__main__":
    parse_csv("library_checkouts.csv")
    parse_tsv("movie_streams.tsv")
    