import datetime

def validate_year(year):
	current_year = datetime.datetime.now().year

	try:
		input_year = int(year)
		if input_year > current_year:
			raise
		elif input_year < 1:
			raise
		else:
			return input_year
	except:
		raise

def validate_text(text):
	if text:
		return text
	else: 
		raise
