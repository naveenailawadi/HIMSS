from bs4 import BeautifulSoup as bs


# class for the company
class HIMSSCompany:
	# company tag
	company_tag = None

	company_attributes = []

	def __init__(self, new_company_tag):
		# store the tag
		self.company_tag = new_company_tag

		self.company_attributes = self.company_tag.find_all("td")

	# function to get an attribute from a span tag class
	def get_attribute(self, tag_type, tag_class):
		attribute = self.company_tag.find(tag_type, class_=tag_class)

		if attribute:
			return attribute.text.strip()
		else:
			return 'N/A'

	# get the company name
	@property	
	def company(self):
		return self.company_attributes[1].text.strip()

	@property
	def booth(self):
		return self.company_attributes[3].text.strip()
	

	# get the full information in a dictionary
	@property
	def info(self):
		information_dir = {
			'company': self.company,
			'booth': self.booth
		}

		return information_dir


# load file function
def load_file(html_file):
	with open(html_file, 'r', encoding='utf8') as infile:
		# make a soup
		soup = bs(infile.read(), 'html.parser')

	return soup