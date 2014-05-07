import mechanize

URL = 'http://www.nrcs.usda.gov/wps/portal/nrcs/soilsurvey/soils/survey/state/'

def main():
    # Create a Browser instance
    b = mechanize.Browser()
    # Load the page
    b.open(URL)
    # Select the form


if __name__ == '__main__':
    import sys
    sys.stdout.write(main().read())