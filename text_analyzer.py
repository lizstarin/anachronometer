import string, os, datetime
from textblob import TextBlob, Word
import data_handler, scraper
from date_parser import WordDate

MW_API_KEY = os.environ.get('MW_API_KEY')

def build_url(word):
	return 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/' + word + '?key=' + MW_API_KEY

a = 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.'

b = 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'

c = 'It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here.'

d = 'But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground.'

e = 'This quotation and my objection to the Dewey film were thrown back at me some years later, when I published a novel about the Watergate scandal. Frank Gannon, reviewing the book in The Wall Street Journal, had a number of nice things to say about it, but he asked how the author of that essay Ive been citing could now "justify subjecting Pat Nixons daughters and grandchildren to the creation and elaboration of a fictional adultery on her part."'

f = 'When submitting information to the Federal government, it usually doesnt do you any good to provide more information than what is requested. In this case, assuming I am understanding correctly that you are starting a business, you have a supplier and the necessary facilities and staffing to conduct business in the U.S., and you are preparing an application to send to the Alcohol and Tobacco Tax and Trade Bureau, the requirements for the letter of intent are few (see top of page 3), so a simple letter from your supplier, like the following, would be perfectly adequate'

sample_text = TextBlob(f)

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
	'CC'	: ['conjunction'], 														# coordinating conjunction
	'CD'	: ['noun'],																# cardinal number
	'DT'	: ['indefinite article', 'definite article', 'adjective', 'pronoun'],	# determiner
	'EX'	: '',																	# existential there
	'FW'	: '',																	# foreign word
	'IN'	: ['preposition', 'conjunction'],										# preposition or subordinating conjunction
	'JJ'	: ['adjective'],														# adjective
	'JJR'	: ['adjective'],														# adjective, comparative
	'JJS'	: ['adjective'],														# adjective, superlative
	'LS'	: '',																	# list item marker
	'MD'	: ['verb', 'verbal auxiliary'],											# modal
	'NN'	: ['noun'],																# noun, singular or mass
	'NNS'	: ['noun'],																# noun, plural
	'NNP'	: ['noun'],																# proper noun, singular
	'NNPS' 	: ['noun'],																# proper noun, plural
	'PDT'	: '',																	# predeterminer
	'POS'	: '',																	# possessive ending
	'PRP'	: ['pronoun'],															# personal pronoun
	'PRP$'	: ['pronoun'],															# possessive pronoun
	'RB'	: ['adverb'],															# adverb
	'RBR'	: ['adverb'],															# adverb, comparative
	'RBS'	: ['adverb'],															# adverb, superlative
	'RP'	: '',																	# particle
	'SYM'	: '',																	# symbol
	'TO'	: ['preposition', 'adverb'],											# to
	'UH'	: ['interjection'],														# interjection
	'VB'	: ['verb'],																# verb, base form
	'VBD'	: ['verb'],																# verb, past tense
	'VBG'	: ['verb'],																# verb, gerund or present participle
	'VBN'	: ['verb'],																# verb, past participle
	'VBP'	: ['verb'],																# verb, non-3rd person singular present
	'VBZ'	: ['verb'],																# verb, 3rd person singular present
	'WDT'	: ['indefinite article', 'definite article', 'adjective', 'pronoun'],	# wh-determiner
	'WP'	: ['pronoun'],															# wh-pronoun
	'WP$'	: ['pronoun'],															# possessive wh-pronoun
	'WRB'	: ['adverb'],															# wh-adverb
}

def get_dates(text):

	def date_lookup(word):
		print word[0]
		pos = pos_tags[word[1]]
		if pos == '':
			return 'ignore'
		else:
			dates = [el for el in [data_handler.get_date_by_word_string_and_pos(word[0], p) for p in pos] if el]	# query db by word and pos
			
			if not dates and pos[0] == 'verb':
				w = Word(str(word[0])).lemmatize('v')
				dates = [el for el in [data_handler.get_date_by_word_string_and_pos(w, 'verb')] if el]	# query db by base verb

			if not dates and pos[0] == 'noun':
				w = Word(str(word[0])).lemmatize()
				dates = [el for el in [data_handler.get_date_by_word_string_and_pos(w, 'noun')] if el]	# query db by base noun

			if not dates:
				dates = data_handler.get_dates_by_word_string(word[0]) 	#query db for all dates

			if not dates:
				data_handler.parse_word_line(word[0] + scraper.get_file_line(word[0])) # scrape mw and add new word to db
				dates = [el for el in [data_handler.get_date_by_word_string_and_pos(word[0], p) for p in pos] if el]		
			
			if not dates:
				dates = [None]

			return min(dates, key=lambda date: WordDate(date).latest)

	return [(word, date_lookup(word)) for word in text.tags]


print get_dates(sample_text)
