"""
Write methods that can parse a CSV and a TSV.

CSV: comma-separated values
TSV: tab-separated values

This solution eliminates the repeated code by
creating a private function to do the "grunt work."

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
    return general_parser(filename, ".csv", ",")
    
    
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
    return general_parser(filename, ".tsv", "\t")


# Bonus method!
# Did you notice that you repeated a lot of the same code?
# This method generalizes a single-deliminated file
def general_parser(filename, delimeter, file_extension):
    """
    Parses a file with delimeter-separated values.
    
    Parameters
    ----------
    filename : path to file
    
    Returns
    --------
    list : multi-dimensional list of file content
    """
    # 1. Validate file
    if not filename.endswith(file_extension):
        print("{} is not a valid {}".format(filename, file_extension))
        return
    # 2. Open file and save lines
    with open(filename, "r") as f:
        lines = f.readlines()
    # 3. Parse lines into list
    parsed_lines = []
    for line in lines:
        line_items = line.split(delimeter)
        cleaned_line_items = [item.strip() for item in line_items]
        parsed_lines.append(cleaned_line_items)
    # 4. Return list
    return parsed_lines


if __name__ == "__main__":
    parsed_file = parse_csv("library_checkouts.csv")
    print(parsed_file)
    
    parsed_file = parse_tsv("movie_streams.tsv")
    print(parsed_file)

