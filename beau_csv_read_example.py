

import zipfile, csv
from pprint import pprint


def CMA(n):  return ','.join(textwrap.wrap(str(n)[::-1],3))[::-1]
# Pull from the exactbins zipfile directly.

def main():
    INFILE = 'exactbins.zip'    ;   INCSV = 'exactbins.csv'
    print 'Loading zipfile'
    if not zipfile.is_zipfile(INFILE):  return 'zipfile '+INFILE+' bad or not found'
    
    csvLines = zipfile.ZipFile(INFILE).read(INCSV).splitlines()

    reader = csv.reader(csvLines)

    for row in reader:
    	print row

if __name__ == '__main__':
	main()

	
    


