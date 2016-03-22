import string, os, datetime
from textblob import TextBlob
import data_handler

MW_API_KEY = os.environ.get('MW_API_KEY')

def build_url(word):
	return 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/' + word + '?key=' + MW_API_KEY

def tokenize(text):
	return [word.lower().strip(string.punctuation) for word in text.split()]

# then = datetime.datetime.now()
sample_text = TextBlob("AMERICA has a water problem. To put it simply, the national network for providing safe, clean water is falling apart.This state of affairs, which is the focus of a summit meeting on Tuesday at the White House, threatens more than our drinking water supplies. Water is used in every sector of industry, grows our food, affects our health and props up our energy system. The price of this neglect will be high. In Flint, Mich., the mayor has estimated that it will cost as much as $1.5 billion to fix or replace lead pipes. Over all, repairing our water and wastewater systems could cost $1.3 trillion or more, according to the American Society of Civil Engineers. We need to do this to improve water quality, protect natural ecosystems and ensure a reliable supply for our cities, agriculture and industry. The problem is a result of many factors, including old, leaky pipes; archaic pricing; and a remarkable lack of data about how much water we use. In cities across the country, billions of gallons of water disappear every day through leaky pipes. Houston alone lost 22 billion gallons in 2012. As the water expert David Sedlak at the University of California, Berkeley, has noted, the water system is facing a double whammy: It has reached the end of its service life just as climate change and population growth have increased its burdens. No wonder the civil engineers society gave the nation's drinking water systems a grade of D in 2013. Wastewater treatment systems are also in serious need of upgrading. Flooding strains treatment plants and sewer systems in many older cities, causing them to discharge untreated sewage whenever rainfall or snowmelt overwhelm them. After Hurricane Sandy, treatment plants in the New York area backed up, with sewage flowing the wrong direction from drainage pipes. The New York Times noted that in one neighborhood a plume of feces and wastewater burst through the street like a geyser. Droughts also jeopardize water supplies, causing cities in the West to reach farther or dig deeper to get their water. Outside Las Vegas, Lake Mead, fed by the Colorado River, was recently measured at 39 percent of capacity. These problems are compounded by an antiquated system of regulations, dysfunctional water markets, policies that encourage overpumping, and contracts that discourage conservation by requiring customers to pay for water they don't use. These approaches depress investment and inhibit innovation. To fix our water systems, we need prices that lead to more rational water use and invite needed investment, data to track water resources and usage, and much more research and development. Take prices, for example. Water prices should rise or fall according to supply and demand. The idea that the price should be the same in the dry season (when supplies are low and demand for irrigation is high) as the wet season (when supplies are high and demand is low) is nonsense. Water utilities should take a page out of the energy sector's playbook. Electric utilities had been plagued for decades by many of the same difficulties. But now they are moving toward time-of-use pricing, with prices rising when demand is up, and inverted block pricing, where prices increase with consumption. Allowing these price shifts would change user behavior. Higher prices would encourage conservation and new technologies. Regulations can ensure that the first few gallons per person per day are cheap or free, with escalating costs beyond that. Water for necessities such as drinking, cooking and hygiene should be affordable. Beyond that, water for lawns, filling swimming pools, washing cars and other uses should be more expensive. We also have to fix our data gaps. We are operating blind. Compared to sectors like energy, where robust statistics on prices, production and consumption are generated weekly, key information on water use and supply is missing or published only every few years. We should increase the federal budgets for water monitoring. Establishing a Water Information Administration, just as the Department of Energy has an Energy Information Administration, to collect, curate and maintain up-to-date, publicly available water data would inform policy makers and the markets. Congress should also significantly increase support for water research and development, making sure to include the private sector as a partner. ")
# print sample_text.tags

# print tokenize(sample_text)
# print datetime.datetime.now() - then

# print words
# for word in words:
# 	print urllib2.urlopen(build_url(word)).read()

# mw_parts_of_speech = {
# 	'abbreviation' 											:
# 	'adjective'												:
# 	'adverb'												:
# 	'adverb or adjective'									:
# 	'conjunction'											:
# 	'definite article'										:
# 	'indefinite article'									:
# 	'interjection'											:
# 	'intransitive verb'										:	
# 	'noun'													:
# 	'noun plural'											:
# 	'noun plural but singular in construction'				:
# 	'noun plural but singular or plural in construction'	:
# 	'noun, plural in construction'							:
# 	'preposition'											:
# 	'pronoun'												:
# 	'pronoun, plural in construction'						:
# 	'pronoun, singular or plural in construction'			:
# 	'pronoun, sometimes plural in construction'				:
# 	'transitive verb'										:
# 	'verb'													:
# 	'verbal auxiliary'										:
# }

pos_tags = {
	'CC'	: ['conjunction'], 								# coordinating conjunction
	'CD'	: ['noun'],										# cardinal number
	'DT'	: ['indefinite article', 'definite article'],	# determiner
	'EX'	: '',											# existential there
	'FW'	: '',											# foreign word
	'IN'	: ['preposition', 'conjunction'],				# preposition or subordinating conjunction
	'JJ'	: ['adjective'],								# adjective
	'JJR'	: ['adjective'],								# adjective, comparative
	'JJS'	: ['adjective'],								# adjective, superlative
	'LS'	: '',											# list item marker
	'MD'	: ['verb', 'verbal auxiliary'],					# modal
	'NN'	: ['noun'],										# noun, singular or mass
	'NNS'	: ['noun'],										# noun, plural
	'NNP'	: ['noun'],										# proper noun, singular
	'NNPS' 	: ['noun'],										# proper noun, plural
	'PDT'	: '',											# predeterminer
	'POS'	: '',											# possessive ending
	'PRP'	: ['pronoun'],									# personal pronoun
	'PRP$'	: ['pronoun'],									# possessive pronoun
	'RB'	: ['adverb'],									# adverb
	'RBR'	: ['adverb'],									# adverb, comparative
	'RBS'	: ['adverb'],									# adverb, superlative
	'RP'	: '',											# particle
	'SYM'	: '',											# symbol
	'TO'	: '',											# to
	'UH'	: ['interjection'],								# interjection
	'VB'	: ['verb'],										# verb, base form
	'VBD'	: ['verb'],										# verb, past tense
	'VBG'	: ['verb'],										# verb, gerund or present participle
	'VBN'	: ['verb'],										# verb, past participle
	'VBP'	: ['verb'],										# verb, non-3rd person singular present
	'VBZ'	: ['verb'],										# verb, 3rd person singular present
	'WDT'	: ['indefinite article', 'definite article'],	# wh-determiner
	'WP'	: ['pronoun'],									# wh-pronoun
	'WP$'	: ['pronoun'],									# possessive wh-pronoun
	'WRB'	: ['adverb'],									# wh-adverb
}

def get_dates(text):
	for word in text.tags:
		print word[0]
		pos = pos_tags[word[1]]
		if pos == '':
			print 'ignore\n'
		else:
			for p in pos:
				print data_handler.get_date_by_word_string_and_pos(word[0].lower(), p)

get_dates(sample_text)