# Python RegEx notes





#raw string:
r'string'



#metacharacters:
#(.) match any char
ex. re.match('1..', '1111') #returns the regex object <111>
#(^) match start
ex. re.match('^11', '011') #returns None
#($) match end
ex. re.match('11$', '011') #returns the regex object <11>
#(|) or
ex. re.match('1|0', '011') #returns the regex object <0>
#(*) zero or more repetitions.
ex. re.match('0*', '01111011') #
#(+) one of more repetitions.
ex. re.match('0+', '01111011') #
#(?) zero of one repetitions.
ex. re.match('0?', '01111011') #
#({}) custom repetition range. (if the first int is missing,defaults to 0, the second missing will be taken to be infinity)
ex. re.match('0{1,3}', '01111011') #



#special sequences:
#(\d) digits (\D matches non-digits)
re.match(r'\d', '011') #
#(\s) whitespace (\S matches non-whitespace)
re.match(r'\s', '011') #
#(\w) word chars (\W matches non-word chars)
re.match(r'\w', '011') #
#(\A,\Z) beginning of a string and end of a string
re.match(r'\A011\Z', '011') #
#(\b) empty string (\B matches the empty string anywhere else)
re.match(r'\b(011)\b', '011 011 011') #
#(\0-99)
re.match(r'(011)\1', '011 011') #returns <011 011>



#char classes:
#combine ranges: [A-G][025]
#invert class: [^A-G] (find all except A-G)
#match any lowercase char
ex. re.match('[a-z]', '') #matches lowercase char 'a' - 'z'
#match any uppercase char
ex. re.match('[B-G]', '011') #matches uppercase char 'B' - 'G'
#match any digit
ex. re.match('[0-4]', '011') #matches uppercase char '0' - '4'
#
ex. re.match('[10]', '011') #returns the regex object <0>



#char groups:
#multiple and nested: '0(1(1)1)(00)'
#named groups: (?P<name>...) #name of the group and ... is the pattern. can be accessed by given name string.
#non-capturing groups: (?...) #ommited from group()
re.match('0(11)', '01111011') #returns <011>
re.match('0(11)', '01111011').group(0) #returns '011'
re.match('0(11)', '01111011').groups() #returns ('11')



#find at beginning
ex. re.match('11', '1111') #searches for '11' at the beginning of the string '1111'


#find anywhere
ex. re.search('11', '011')
ex. re.search('11', '011').group() 	#returns '11' (the matched string). 
ex. re.search('11', '011').start() 	#returns 1 (starting index)
ex. re.search('11', '011').end() 	#returns 3 (ending position(first char after search string))
ex. re.search('11', '011').span() 	#returns (1,3) (start and end as tuple.)


#return a list of each occurance.
ex. re.findall('11', '110110') #returns ['11','11']


#substitute:
ex. re.sub('11', '00', '011001', max=0) #returns '000001' (optional arg max: number of occurances to replace)



#extract email from string example:
pattern = r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)'
str_ = 'string containing x@xxx.xxx'

m = re.search(pattern, str_).group()