from bs4 import BeautifulSoup
import re

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
                zip_codes.append(number)
    
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
        counties.append(found_children[3].text)
    
    return counties

# Generates a CSV file using the zip codes and counties list
# Headers for CSV are Zip Code, County, State, Entitlement
# This wil only fill in Zip Code and County and State
# Entitlement column will be done manually in Excel
def create_csv(zip_codes, counties, state):
    print("in create_csv")

S = create_soup("state-html-data\Georgia.html")
print(len(generate_zip_code_list(S)))
print(len(generate_county_list(S)))
