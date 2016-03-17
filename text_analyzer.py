import string, os

MW_API_KEY = os.environ.get('MW_API_KEY')

def build_url(word):
	return 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/' + word + '?key=' + MW_API_KEY

def parse_text(text):
	return [word.lower().strip(string.punctuation) for word in text.split()]

sample_text = 'Bacon ipsum dolor, amet doner beef-frankfurter, sausage beef ribs hamburger pork chop tenderloin biltong alcatra spare ribs corned beef kevin. Filet mignon pork belly venison short ribs tenderloin salami strip steak. Leberkas drumstick bacon cupim rump doner turkey andouille ball tip. Sirloin tail short loin, shankle cupim short ribs... frankfurter pastrami tongue ribeye.'

print parse_text(sample_text)

print words
for word in words:
	print urllib2.urlopen(build_url(word)).read()