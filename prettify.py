from constants import INFILE
from bs4 import BeautifulSoup as bs

# main function
def main(file=INFILE):
	# open the file
	with open(file, 'r', encoding='utf8') as infile:
		# make a soup
		soup = bs(infile.read(), 'html.parser')

	# save the new (prettified) soup
	with open(file, 'w', encoding='utf8') as outfile:
		outfile.write(soup.prettify())


if __name__ == '__main__':
	main()