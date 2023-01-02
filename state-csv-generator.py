from bs4 import BeautifulSoup
import re
import os

# Creates the soup to query HTML doc with
def create_soup(file_name):
    HTMLFile = open(file_name, "r")
    index = HTMLFile.read()
    return BeautifulSoup(index, 'html5lib')

# Parses the HTML file for the zip codes in state
# Returns list of zip codes
def generate_zip_code_list(soup):
    pattern = re.compile(r'/(\d+)/')
    zip_codes = []
    div_elements = soup.find_all("div", class_="list-group-item")

    # Iterate over the div elements
    for div in div_elements:
        # Extract zip codes
        # Find all anchor elements within the div element
        a_elements = div.find_all('a')

        # Iterate over the anchor elements
        for a in a_elements:
            # Check if the href attribute matches the regular expression pattern
            match = pattern.search(a['href'])
            if match:
                # Extract the matched number and print it
                number = match.group(1)
                # print(number)
                zip_codes.append(number.strip())

    return zip_codes

# Parses the HTML file for the county names in state
# Returns lis of county names
def generate_county_list(soup):
    counties = []
    div_elements = soup.find_all("div", class_="list-group-item")

    # Iterate over the div elements
    for div in div_elements:
        # Extract county names
        child_div_element = div.find('div')
        found_children = child_div_element.find_all('div')
        # print(found_children[3].text)
        counties.append(found_children[3].text.strip())

    return counties

# Generates a CSV file using the zip codes and counties list
# Headers for CSV are Zip Code, County, State, Entitlement
# This wil only fill in Zip Code and County and State
# Entitlement column will be done manually in Excel
def create_csv(zip_codes, counties, state):
    print("in create_csv")

def find_matching_zip_and_county(zip_codes, counties, zip_to_find):
    index = zip_codes.index(zip_to_find)
    print(zip_to_find, index)
    print(counties[index])


# Set the path to the folder
folder_path = 'state-html-data'

# Get the names of all the files in the folder
file_names = os.listdir(folder_path)

# Iterate over the file names
for file_name in file_names:
    # Construct the full path to the file
    file_path = os.path.join(folder_path, file_name)

    # Check if the file is a regular file (not a directory or a special file)
    if os.path.isfile(file_path):
        S = create_soup(file_path)
        zip_codes = generate_zip_code_list(S)
        counties = generate_county_list(S)
        find_matching_zip_and_county(zip_codes, counties, "31144")
        # print(len(generate_zip_code_list(S)))
        # print(len(generate_county_list(S)))
