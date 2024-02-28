from bs4 import BeautifulSoup as bs
import pandas as pd
from constants import INFILE
from HIMSS import HIMSSCompany, load_file

OUTFILE = 'HIMSS_companies.csv'

# main function
def main(html_file=INFILE, csv_file=OUTFILE):
	# load the file
	soup = load_file(html_file)

	# get all the companies
	company_blocks = soup.find_all('tr', class_="js-List justify-between")

	# make all the companies
	companies = [HIMSSCompany(block) for block in company_blocks]
	print(f"found {len(companies)} companies")

	# generate all the company objects
	objects = [company.info for company in companies]

	# export to excel
	df = pd.DataFrame(objects)
	df.to_csv(csv_file, index=False)


if __name__ == '__main__':
	main()