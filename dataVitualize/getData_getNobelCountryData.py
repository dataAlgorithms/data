REST_EU_ROOT_URL = "http://restcountries.eu/rest/v1"
def REST_country_request(field='all', name=None, params=None):
    
    headers = {'User-Agent':'Mozilla/5.0'}

    if not params:
        params = {}

    if field == 'all':
        return requests.get(REST_EU_ROOT_URL + '/all')

    url = '%s/%s/%s'%(REST_EU_ROOT_URL, field, name)
    print('Requesting URL:' + url)
    response = requests.get(url, params=params, headers=headers)

    if not response.status_code == 200:
        raise Exception('Request failed with status code ' \
            + str(response.status_code))

    return response

# get a list of all the countries using US dollar as currency
response = REST_country_request('currency', 'usd')
print(response.json())

'''
[{u'timezones': [u'UTC-11:00'], u'demonym': u'American Samoan', u'currencies': [
u'USD'], u'alpha2Code': u'AS', u'alpha3Code': u'ASM', u'area': 199.0, u'language
s': [u'en', u'sm'], u'capital': u'Pago Pago', u'relevance': u'0.5', u'borders':
[], u'altSpellings': [u'AS', u'Amerika S\u0101moa', u'Amelika S\u0101moa', u'S\u
0101moa Amelika'], u'gini': None, u'translations': {u'fr': u'Samoa am\xe9ricaine
s', u'de': u'Amerikanisch-Samoa', u'ja': u'\u30a2\u30e1\u30ea\u30ab\u9818\u30b5\
u30e2\u30a2', u'es': u'Samoa Americana', u'it': u'Samoa Americane'}, u'nativeNam
e': u'American Samoa', u'topLevelDomain': [u'.as'], u'numericCode': u'016', u'po
pulation': 55519, u'callingCodes': [u'1684'], u'name': u'American Samoa', u'regi
on': u'Oceania', u'subregion': u'Polynesia', u'latlng': [-14.33333333, -170.0]},
 {u'timezones': [u'UTC-04:00'], u'demonym': u'Dutch', u'currencies': [u'USD'], u
'alpha2Code': u'BQ', u'alpha3Code': u'BES', u'area': 294.0, u'languages': [u'nl'
], u'capital': u'Kralendijk', u'relevance': u'0', u'borders': [], u'altSpellings
': [u'BQ', u'Boneiru'], u'gini': None, u'translations': {u'fr': None, u'de': Non
e, u'ja': None, u'es': None, u'it': None}, u'nativeName': u'Bonaire', u'topLevel
Domain': [u'.an', u'.nl'], u'numericCode': u'535', u'population': 17408, u'calli
ngCodes': [u'5997'], u'name': u'Bonaire', u'region': u'Americas', u'subregion':
u'Caribbean', u'latlng': [12.15, -68.266667]}, {u'timezones': [u'UTC+06:00'], u'
demonym': u'Indian', u'currencies': [u'USD'], u'alpha2Code': u'IO', u'alpha3Code
': u'IOT', u'area': 60.0, u'languages': [u'en'], u'capital': u'Diego Garcia', u'
relevance': u'0', u'borders': [], u'altSpellings': [u'IO'], u'gini': None, u'tra
nslations': {u'fr': u"Territoire britannique de l'oc\xe9an Indien", u'de': u'Bri
tisches Territorium im Indischen Ozean', u'ja': u'\u30a4\u30ae\u30ea\u30b9\u9818
\u30a4\u30f3\u30c9\u6d0b\u5730\u57df', u'es': u'Territorio Brit\xe1nico del Oc\x
e9ano \xcdndico', u'it': u"Territorio britannico dell'oceano indiano"}, u'native
Name': u'British Indian Ocean Territory', u'topLevelDomain': [u'.io'], u'numeric
Code': u'086', u'population': 3000, u'callingCodes': [u'246'], u'name': u'Britis
h Indian Ocean Territory', u'region': u'Africa', u'subregion': u'Eastern Africa'
, u'latlng': [-6.0, 71.5]}, {u'timezones': [u'UTC-11:00', u'UTC-10:00', u'UTC+12
:00'], u'demonym': u'American', u'currencies': [u'USD'], u'alpha2Code': u'UM', u
'alpha3Code': u'UMI', u'area': None, u'languages': [u'en'], u'capital': u'', u'r
elevance': u'0', u'borders': [], u'altSpellings': [u'UM'], u'gini': None, u'tran
slations': {u'fr': u'\xceles mineures \xe9loign\xe9es des \xc9tats-Unis', u'de':
 u'Kleinere Inselbesitzungen der Vereinigten Staaten', u'ja': u'\u5408\u8846\u56
fd\u9818\u6709\u5c0f\u96e2\u5cf6', u'es': u'Islas Ultramarinas Menores de Estado
s Unidos', u'it': u"Isole minori esterne degli Stati Uniti d'America"}, u'native
Name': u'United States Minor Outlying Islands', u'topLevelDomain': [u'.us'], u'n
umericCode': u'581', u'population': 300, u'callingCodes': [u''], u'name': u'Unit
ed States Minor Outlying Islands', u'region': u'Americas', u'subregion': u'North
ern America', u'latlng': []}, {u'timezones': [u'UTC-04:00'], u'demonym': u'Virgi
n Islander', u'currencies': [u'USD'], u'alpha2Code': u'VG', u'alpha3Code': u'VGB
', u'area': 151.0, u'languages': [u'en'], u'capital': u'Road Town', u'relevance'
: u'0.5', u'borders': [], u'altSpellings': [u'VG'], u'gini': None, u'translation
s': {u'fr': u'\xceles Vierges britanniques', u'de': u'Britische Jungferninseln',
 u'ja': u'\u30a4\u30ae\u30ea\u30b9\u9818\u30f4\u30a1\u30fc\u30b8\u30f3\u8af8\u5c
f6', u'es': u'Islas V\xedrgenes del Reino Unido', u'it': u'Isole Vergini Britann
iche'}, u'nativeName': u'British Virgin Islands', u'topLevelDomain': [u'.vg'], u
'numericCode': u'092', u'population': 28054, u'callingCodes': [u'1284'], u'name'
: u'Virgin Islands (British)', u'region': u'Americas', u'subregion': u'Caribbean
', u'latlng': [18.431383, -64.62305]}, {u'timezones': [u'UTC-04:00'], u'demonym'
: u'Virgin Islander', u'currencies': [u'USD'], u'alpha2Code': u'VI', u'alpha3Cod
e': u'VIR', u'area': 346.36, u'languages': [u'en'], u'capital': u'Charlotte Amal
ie', u'relevance': u'0.5', u'borders': [], u'altSpellings': [u'VI', u'USVI', u'A
merican Virgin Islands', u'U.S. Virgin Islands'], u'gini': None, u'translations'
: {u'fr': u'\xceles Vierges des \xc9tats-Unis', u'de': u'Amerikanische Jungferni
nseln', u'ja': u'\u30a2\u30e1\u30ea\u30ab\u9818\u30f4\u30a1\u30fc\u30b8\u30f3\u8
af8\u5cf6', u'es': u'Islas V\xedrgenes de los Estados Unidos', u'it': u'Isole Ve
rgini americane'}, u'nativeName': u'Virgin Islands of the United States', u'topL
evelDomain': [u'.vi'], u'numericCode': u'850', u'population': 114743, u'callingC
odes': [u'1 340'], u'name': u'Virgin Islands (U.S.)', u'region': u'Americas', u'
subregion': u'Caribbean', u'latlng': [18.34, -64.93]}, {u'timezones': [u'UTC-06:
00', u'UTC-05:00'], u'demonym': u'Ecuadorean', u'currencies': [u'USD'], u'alpha2
Code': u'EC', u'alpha3Code': u'ECU', u'area': 276841.0, u'languages': [u'es'], u
'capital': u'Quito', u'relevance': u'0', u'borders': [u'COL', u'PER'], u'altSpel
lings': [u'EC', u'Republic of Ecuador', u'Rep\xfablica del Ecuador'], u'gini': 4
9.3, u'translations': {u'fr': u'\xc9quateur', u'de': u'Ecuador', u'ja': u'\u30a8
\u30af\u30a2\u30c9\u30eb', u'es': u'Ecuador', u'it': u'Ecuador'}, u'nativeName':
 u'Ecuador', u'topLevelDomain': [u'.ec'], u'numericCode': u'218', u'population':
 16027500, u'callingCodes': [u'593'], u'name': u'Ecuador', u'region': u'Americas
', u'subregion': u'South America', u'latlng': [-2.0, -77.5]}, {u'timezones': [u'
UTC-06:00'], u'demonym': u'Salvadoran', u'currencies': [u'SVC', u'USD'], u'alpha
2Code': u'SV', u'alpha3Code': u'SLV', u'area': 21041.0, u'languages': [u'es'], u
'capital': u'San Salvador', u'relevance': u'0', u'borders': [u'GTM', u'HND'], u'
altSpellings': [u'SV', u'Republic of El Salvador', u'Rep\xfablica de El Salvador
'], u'gini': 48.3, u'translations': {u'fr': u'Salvador', u'de': u'El Salvador',
u'ja': u'\u30a8\u30eb\u30b5\u30eb\u30d0\u30c9\u30eb', u'es': u'El Salvador', u'i
t': u'El Salvador'}, u'nativeName': u'El Salvador', u'topLevelDomain': [u'.sv'],
 u'numericCode': u'222', u'population': 6401240, u'callingCodes': [u'503'], u'na
me': u'El Salvador', u'region': u'Americas', u'subregion': u'Central America', u
'latlng': [13.83333333, -88.91666666]}, {u'timezones': [u'UTC+10:00'], u'demonym
': u'Guamanian', u'currencies': [u'USD'], u'alpha2Code': u'GU', u'alpha3Code': u
'GUM', u'area': 549.0, u'languages': [u'en', u'ch', u'es'], u'capital': u'Hag\xe
5t\xf1a', u'relevance': u'0', u'borders': [], u'altSpellings': [u'GU', u'Gu\xe5h
\xe5n'], u'gini': None, u'translations': {u'fr': u'Guam', u'de': u'Guam', u'ja':
 u'\u30b0\u30a2\u30e0', u'es': u'Guam', u'it': u'Guam'}, u'nativeName': u'Guam',
 u'topLevelDomain': [u'.gu'], u'numericCode': u'316', u'population': 159358, u'c
allingCodes': [u'1671'], u'name': u'Guam', u'region': u'Oceania', u'subregion':
u'Micronesia', u'latlng': [13.46666666, 144.78333333]}, {u'timezones': [u'UTC-05
:00'], u'demonym': u'Haitian', u'currencies': [u'HTG', u'USD'], u'alpha2Code': u
'HT', u'alpha3Code': u'HTI', u'area': 27750.0, u'languages': [u'fr', u'ht'], u'c
apital': u'Port-au-Prince', u'relevance': u'0', u'borders': [u'DOM'], u'altSpell
ings': [u'HT', u'Republic of Haiti', u"R\xe9publique d'Ha\xefti", u'Repiblik Ayi
ti'], u'gini': 59.2, u'translations': {u'fr': u'Ha\xefti', u'de': u'Haiti', u'ja
': u'\u30cf\u30a4\u30c1', u'es': u'Haiti', u'it': u'Haiti'}, u'nativeName': u'Ha
\xefti', u'topLevelDomain': [u'.ht'], u'numericCode': u'332', u'population': 109
11819, u'callingCodes': [u'509'], u'name': u'Haiti', u'region': u'Americas', u's
ubregion': u'Caribbean', u'latlng': [19.0, -72.41666666]}, {u'timezones': [u'UTC
+12:00'], u'demonym': u'Marshallese', u'currencies': [u'USD'], u'alpha2Code': u'
MH', u'alpha3Code': u'MHL', u'area': 181.0, u'languages': [u'en', u'mh'], u'capi
tal': u'Majuro', u'relevance': u'0.5', u'borders': [], u'altSpellings': [u'MH',
u'Republic of the Marshall Islands', u'Aolep\u0101n Aor\u014dkin M\u0327aje\u013
c'], u'gini': None, u'translations': {u'fr': u'\xceles Marshall', u'de': u'Marsh
allinseln', u'ja': u'\u30de\u30fc\u30b7\u30e3\u30eb\u8af8\u5cf6', u'es': u'Islas
 Marshall', u'it': u'Isole Marshall'}, u'nativeName': u'M\u0327aje\u013c', u'top
LevelDomain': [u'.mh'], u'numericCode': u'584', u'population': 56086, u'callingC
odes': [u'692'], u'name': u'Marshall Islands', u'region': u'Oceania', u'subregio
n': u'Micronesia', u'latlng': [9.0, 168.0]}, {u'timezones': [u'UTC+10:00', u'UTC
+11'], u'demonym': u'Micronesian', u'currencies': [u'USD'], u'alpha2Code': u'FM'
, u'alpha3Code': u'FSM', u'area': 702.0, u'languages': [u'en'], u'capital': u'Pa
likir', u'relevance': u'0', u'borders': [], u'altSpellings': [u'FM', u'Federated
 States of Micronesia'], u'gini': None, u'translations': {u'fr': u'Micron\xe9sie
', u'de': u'Mikronesien', u'ja': u'\u30df\u30af\u30ed\u30cd\u30b7\u30a2\u9023\u9
0a6', u'es': u'Micronesia', u'it': u'Micronesia'}, u'nativeName': u'Micronesia',
 u'topLevelDomain': [u'.fm'], u'numericCode': u'583', u'population': 101351, u'c
allingCodes': [u'691'], u'name': u'Federated States of Micronesia', u'region': u
'Oceania', u'subregion': u'Micronesia', u'latlng': [6.91666666, 158.25]}, {u'tim
ezones': [u'UTC+10:00'], u'demonym': u'American', u'currencies': [u'USD'], u'alp
ha2Code': u'MP', u'alpha3Code': u'MNP', u'area': 464.0, u'languages': [u'en', u'
ch'], u'capital': u'Saipan', u'relevance': u'0.5', u'borders': [], u'altSpelling
s': [u'MP', u'Commonwealth of the Northern Mariana Islands', u'Sankattan Siha Na
 Islas Mari\xe5nas'], u'gini': None, u'translations': {u'fr': u'\xceles Marianne
s du Nord', u'de': u'N\xf6rdliche Marianen', u'ja': u'\u5317\u30de\u30ea\u30a2\u
30ca\u8af8\u5cf6', u'es': u'Islas Marianas del Norte', u'it': u'Isole Marianne S
ettentrionali'}, u'nativeName': u'Northern Mariana Islands', u'topLevelDomain':
[u'.mp'], u'numericCode': u'580', u'population': 53883, u'callingCodes': [u'1670
'], u'name': u'Northern Mariana Islands', u'region': u'Oceania', u'subregion': u
'Micronesia', u'latlng': [15.2, 145.75]}, {u'timezones': [u'UTC+09:00'], u'demon
ym': u'Palauan', u'currencies': [u'USD'], u'alpha2Code': u'PW', u'alpha3Code': u
'PLW', u'area': 459.0, u'languages': [u'en'], u'capital': u'Ngerulmud', u'releva
nce': u'0.5', u'borders': [], u'altSpellings': [u'PW', u'Republic of Palau', u'B
eluu er a Belau'], u'gini': None, u'translations': {u'fr': u'Palaos', u'de': u'P
alau', u'ja': u'\u30d1\u30e9\u30aa', u'es': u'Palau', u'it': u'Palau'}, u'native
Name': u'Palau', u'topLevelDomain': [u'.pw'], u'numericCode': u'585', u'populati
on': 20901, u'callingCodes': [u'680'], u'name': u'Palau', u'region': u'Oceania',
 u'subregion': u'Micronesia', u'latlng': [7.5, 134.5]}, {u'timezones': [u'UTC-05
:00'], u'demonym': u'Panamanian', u'currencies': [u'PAB', u'USD'], u'alpha2Code'
: u'PA', u'alpha3Code': u'PAN', u'area': 75417.0, u'languages': [u'es'], u'capit
al': u'Panama City', u'relevance': u'0', u'borders': [u'COL', u'CRI'], u'altSpel
lings': [u'PA', u'Republic of Panama', u'Rep\xfablica de Panam\xe1'], u'gini': 5
1.9, u'translations': {u'fr': u'Panama', u'de': u'Panama', u'ja': u'\u30d1\u30ca
\u30de', u'es': u'Panam\xe1', u'it': u'Panama'}, u'nativeName': u'Panam\xe1', u'
topLevelDomain': [u'.pa'], u'numericCode': u'591', u'population': 3764166, u'cal
lingCodes': [u'507'], u'name': u'Panama', u'region': u'Americas', u'subregion':
u'Central America', u'latlng': [9.0, -80.0]}, {u'timezones': [u'UTC-04:00'], u'd
emonym': u'Puerto Rican', u'currencies': [u'USD'], u'alpha2Code': u'PR', u'alpha
3Code': u'PRI', u'area': 8870.0, u'languages': [u'es', u'en'], u'capital': u'San
 Juan', u'relevance': u'0', u'borders': [], u'altSpellings': [u'PR', u'Commonwea
lth of Puerto Rico', u'Estado Libre Asociado de Puerto Rico'], u'gini': None, u'
translations': {u'fr': u'Porto Rico', u'de': u'Puerto Rico', u'ja': u'\u30d7\u30
a8\u30eb\u30c8\u30ea\u30b3', u'es': u'Puerto Rico', u'it': u'Porto Rico'}, u'nat
iveName': u'Puerto Rico', u'topLevelDomain': [u'.pr'], u'numericCode': u'630', u
'population': 3548397, u'callingCodes': [u'1787', u'1939'], u'name': u'Puerto Ri
co', u'region': u'Americas', u'subregion': u'Caribbean', u'latlng': [18.25, -66.
5]}, {u'timezones': [u'UTC+09:00'], u'demonym': u'East Timorese', u'currencies':
 [u'USD'], u'alpha2Code': u'TL', u'alpha3Code': u'TLS', u'area': 14874.0, u'lang
uages': [u'pt'], u'capital': u'Dili', u'relevance': u'0', u'borders': [u'IDN'],
u'altSpellings': [u'TL', u'East Timor', u'Democratic Republic of Timor-Leste', u
'Rep\xfablica Democr\xe1tica de Timor-Leste', u'Rep\xfablika Demokr\xe1tika Tim\
xf3r-Leste'], u'gini': 31.9, u'translations': {u'fr': u'Timor oriental', u'de':
u'Timor-Leste', u'ja': u'\u6771\u30c6\u30a3\u30e2\u30fc\u30eb', u'es': u'Timor O
riental', u'it': u'Timor Est'}, u'nativeName': u'Timor-Leste', u'topLevelDomain'
: [u'.tl'], u'numericCode': u'626', u'population': 1212107, u'callingCodes': [u'
670'], u'name': u'East Timor', u'region': u'Asia', u'subregion': u'South-Eastern
 Asia', u'latlng': [-8.83333333, 125.91666666]}, {u'timezones': [u'UTC-04:00'],
u'demonym': u'Turks and Caicos Islander', u'currencies': [u'USD'], u'alpha2Code'
: u'TC', u'alpha3Code': u'TCA', u'area': 948.0, u'languages': [u'en'], u'capital
': u'Cockburn Town', u'relevance': u'0.5', u'borders': [], u'altSpellings': [u'T
C'], u'gini': None, u'translations': {u'fr': u'\xceles Turques-et-Ca\xefques', u
'de': u'Turks- und Caicosinseln', u'ja': u'\u30bf\u30fc\u30af\u30b9\u30fb\u30ab\
u30a4\u30b3\u30b9\u8af8\u5cf6', u'es': u'Islas Turks y Caicos', u'it': u'Isole T
urks e Caicos'}, u'nativeName': u'Turks and Caicos Islands', u'topLevelDomain':
[u'.tc'], u'numericCode': u'796', u'population': 31458, u'callingCodes': [u'1649
'], u'name': u'Turks and Caicos Islands', u'region': u'Americas', u'subregion':
u'Caribbean', u'latlng': [21.75, -71.58333333]}, {u'timezones': [u'UTC-12:00', u
'UTC-11:00', u'UTC-10:00', u'UTC-09:00', u'UTC-08:00', u'UTC-07:00', u'UTC-06:00
', u'UTC-05:00', u'UTC-04:00', u'UTC+10:00', u'UTC+12:00'], u'demonym': u'Americ
an', u'currencies': [u'USD', u'USN', u'USS'], u'alpha2Code': u'US', u'alpha3Code
': u'USA', u'area': 9629091.0, u'languages': [u'en'], u'capital': u'Washington,
D.C.', u'relevance': u'3.5', u'borders': [u'CAN', u'MEX'], u'altSpellings': [u'U
S', u'USA', u'United States of America'], u'gini': 48.0, u'translations': {u'fr'
: u'\xc9tats-Unis', u'de': u'Vereinigte Staaten von Amerika', u'ja': u'\u30a2\u3
0e1\u30ea\u30ab\u5408\u8846\u56fd', u'es': u'Estados Unidos', u'it': u"Stati Uni
ti D'America"}, u'nativeName': u'United States', u'topLevelDomain': [u'.us'], u'
numericCode': u'840', u'population': 321645000, u'callingCodes': [u'1'], u'name'
: u'United States', u'region': u'Americas', u'subregion': u'Northern America', u
'latlng': [38.0, -97.0]}, {u'timezones': [u'UTC+02:00'], u'demonym': u'Zimbabwea
n', u'currencies': [u'USD'], u'alpha2Code': u'ZW', u'alpha3Code': u'ZWE', u'area
': 390757.0, u'languages': [u'en', u'sn', u'nd'], u'capital': u'Harare', u'relev
ance': u'0', u'borders': [u'BWA', u'MOZ', u'ZAF', u'ZMB'], u'altSpellings': [u'Z
W', u'Republic of Zimbabwe'], u'gini': None, u'translations': {u'fr': u'Zimbabwe
', u'de': u'Simbabwe', u'ja': u'\u30b8\u30f3\u30d0\u30d6\u30a8', u'es': u'Zimbab
ue', u'it': u'Zimbabwe'}, u'nativeName': u'Zimbabwe', u'topLevelDomain': [u'.zw'
], u'numericCode': u'716', u'population': 13061239, u'callingCodes': [u'263'], u
'name': u'Zimbabwe', u'region': u'Africa', u'subregion': u'Eastern Africa', u'la
tlng': [-20.0, 30.0]}]
'''

# store dataset into MongoDB
from pymongo import MongoClient

def get_mongo_database(db_name, host='localhost',\
              port=27017, username=None, password=None):
    # make mongo connection with/out anthentication
    if username and passowrd:
        mongo_uri = 'mongodb://%s:%s@%s'%\
         (username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]

db_nobel = get_mongo_database('nobel_prize')
col = db_nobel['country_data'] # country data collection

# get all the restful country-data
response = REST_country_request()
# insert the json-object to our collection
col.insert(response.json())

# query 
res = col.find({'currencies': {'$in':['USD']}})
print(list(res))

'''
d:\Anaconda2\Scripts\ipython-script.py:20: DeprecationWarning: insert is depreca
ted. Use insert_one or insert_many instead.
[{u'timezones': [u'UTC-11:00'], u'demonym': u'American Samoan', u'subregion': u'
Polynesia', u'alpha2Code': u'AS', u'gini': None, u'alpha3Code': u'ASM', u'area':
 199.0, u'languages': [u'en', u'sm'], u'capital': u'Pago Pago', u'relevance': u'
0.5', u'borders': [], u'altSpellings': [u'AS', u'Amerika S\u0101moa', u'Amelika
S\u0101moa', u'S\u0101moa Amelika'], u'currencies': [u'USD'], u'translations': {
u'fr': u'Samoa am\xe9ricaines', u'de': u'Amerikanisch-Samoa', u'ja': u'\u30a2\u3
0e1\u30ea\u30ab\u9818\u30b5\u30e2\u30a2', u'es': u'Samoa Americana', u'it': u'Sa
moa Americane'}, u'nativeName': u'American Samoa', u'topLevelDomain': [u'.as'],
u'numericCode': u'016', u'population': 55519, u'callingCodes': [u'1684'], u'name
': u'American Samoa', u'region': u'Oceania', u'_id': ObjectId('59f6551c7fae3b129
0e4f0f6'), u'latlng': [-14.33333333, -170.0]}, {u'timezones': [u'UTC-04:00'], u'
demonym': u'Dutch', u'subregion': u'Caribbean', u'alpha2Code': u'BQ', u'gini': N
one, u'alpha3Code': u'BES', u'area': 294.0, u'languages': [u'nl'], u'capital': u
'Kralendijk', u'relevance': u'0', u'borders': [], u'altSpellings': [u'BQ', u'Bon
eiru'], u'currencies': [u'USD'], u'translations': {u'fr': None, u'de': None, u'j
a': None, u'es': None, u'it': None}, u'nativeName': u'Bonaire', u'topLevelDomain
': [u'.an', u'.nl'], u'numericCode': u'535', u'population': 17408, u'callingCode
s': [u'5997'], u'name': u'Bonaire', u'region': u'Americas', u'_id': ObjectId('59
f6551c7fae3b1290e4f10d'), u'latlng': [12.15, -68.266667]}, {u'timezones': [u'UTC
+06:00'], u'demonym': u'Indian', u'subregion': u'Eastern Africa', u'alpha2Code':
 u'IO', u'gini': None, u'alpha3Code': u'IOT', u'area': 60.0, u'languages': [u'en
'], u'capital': u'Diego Garcia', u'relevance': u'0', u'borders': [], u'altSpelli
ngs': [u'IO'], u'currencies': [u'USD'], u'translations': {u'fr': u"Territoire br
itannique de l'oc\xe9an Indien", u'de': u'Britisches Territorium im Indischen Oz
ean', u'ja': u'\u30a4\u30ae\u30ea\u30b9\u9818\u30a4\u30f3\u30c9\u6d0b\u5730\u57d
f', u'es': u'Territorio Brit\xe1nico del Oc\xe9ano \xcdndico', u'it': u"Territor
io britannico dell'oceano indiano"}, u'nativeName': u'British Indian Ocean Terri
tory', u'topLevelDomain': [u'.io'], u'numericCode': u'086', u'population': 3000,
 u'callingCodes': [u'246'], u'name': u'British Indian Ocean Territory', u'region
': u'Africa', u'_id': ObjectId('59f6551c7fae3b1290e4f112'), u'latlng': [-6.0, 71
.5]}, {u'timezones': [u'UTC-11:00', u'UTC-10:00', u'UTC+12:00'], u'demonym': u'A
merican', u'subregion': u'Northern America', u'alpha2Code': u'UM', u'gini': None
, u'alpha3Code': u'UMI', u'area': None, u'languages': [u'en'], u'capital': u'',
u'relevance': u'0', u'borders': [], u'altSpellings': [u'UM'], u'currencies': [u'
USD'], u'translations': {u'fr': u'\xceles mineures \xe9loign\xe9es des \xc9tats-
Unis', u'de': u'Kleinere Inselbesitzungen der Vereinigten Staaten', u'ja': u'\u5
408\u8846\u56fd\u9818\u6709\u5c0f\u96e2\u5cf6', u'es': u'Islas Ultramarinas Meno
res de Estados Unidos', u'it': u"Isole minori esterne degli Stati Uniti d'Americ
a"}, u'nativeName': u'United States Minor Outlying Islands', u'topLevelDomain':
[u'.us'], u'numericCode': u'581', u'population': 300, u'callingCodes': [u''], u'
name': u'United States Minor Outlying Islands', u'region': u'Americas', u'_id':
ObjectId('59f6551c7fae3b1290e4f113'), u'latlng': []}, {u'timezones': [u'UTC-04:0
0'], u'demonym': u'Virgin Islander', u'subregion': u'Caribbean', u'alpha2Code':
u'VG', u'gini': None, u'alpha3Code': u'VGB', u'area': 151.0, u'languages': [u'en
'], u'capital': u'Road Town', u'relevance': u'0.5', u'borders': [], u'altSpellin
gs': [u'VG'], u'currencies': [u'USD'], u'translations': {u'fr': u'\xceles Vierge
s britanniques', u'de': u'Britische Jungferninseln', u'ja': u'\u30a4\u30ae\u30ea
\u30b9\u9818\u30f4\u30a1\u30fc\u30b8\u30f3\u8af8\u5cf6', u'es': u'Islas V\xedrge
nes del Reino Unido', u'it': u'Isole Vergini Britanniche'}, u'nativeName': u'Bri
tish Virgin Islands', u'topLevelDomain': [u'.vg'], u'numericCode': u'092', u'pop
ulation': 28054, u'callingCodes': [u'1284'], u'name': u'Virgin Islands (British)
', u'region': u'Americas', u'_id': ObjectId('59f6551c7fae3b1290e4f114'), u'latln
g': [18.431383, -64.62305]}, {u'timezones': [u'UTC-04:00'], u'demonym': u'Virgin
 Islander', u'subregion': u'Caribbean', u'alpha2Code': u'VI', u'gini': None, u'a
lpha3Code': u'VIR', u'area': 346.36, u'languages': [u'en'], u'capital': u'Charlo
tte Amalie', u'relevance': u'0.5', u'borders': [], u'altSpellings': [u'VI', u'US
VI', u'American Virgin Islands', u'U.S. Virgin Islands'], u'currencies': [u'USD'
], u'translations': {u'fr': u'\xceles Vierges des \xc9tats-Unis', u'de': u'Ameri
kanische Jungferninseln', u'ja': u'\u30a2\u30e1\u30ea\u30ab\u9818\u30f4\u30a1\u3
0fc\u30b8\u30f3\u8af8\u5cf6', u'es': u'Islas V\xedrgenes de los Estados Unidos',
 u'it': u'Isole Vergini americane'}, u'nativeName': u'Virgin Islands of the Unit
ed States', u'topLevelDomain': [u'.vi'], u'numericCode': u'850', u'population':
114743, u'callingCodes': [u'1 340'], u'name': u'Virgin Islands (U.S.)', u'region
': u'Americas', u'_id': ObjectId('59f6551c7fae3b1290e4f115'), u'latlng': [18.34,
 -64.93]}, {u'timezones': [u'UTC-06:00', u'UTC-05:00'], u'demonym': u'Ecuadorean
', u'subregion': u'South America', u'alpha2Code': u'EC', u'gini': 49.3, u'alpha3
Code': u'ECU', u'area': 276841.0, u'languages': [u'es'], u'capital': u'Quito', u
'relevance': u'0', u'borders': [u'COL', u'PER'], u'altSpellings': [u'EC', u'Repu
blic of Ecuador', u'Rep\xfablica del Ecuador'], u'currencies': [u'USD'], u'trans
lations': {u'fr': u'\xc9quateur', u'de': u'Ecuador', u'ja': u'\u30a8\u30af\u30a2
\u30c9\u30eb', u'es': u'Ecuador', u'it': u'Ecuador'}, u'nativeName': u'Ecuador',
 u'topLevelDomain': [u'.ec'], u'numericCode': u'218', u'population': 16027500, u
'callingCodes': [u'593'], u'name': u'Ecuador', u'region': u'Americas', u'_id': O
bjectId('59f6551c7fae3b1290e4f134'), u'latlng': [-2.0, -77.5]}, {u'timezones': [
u'UTC-06:00'], u'demonym': u'Salvadoran', u'subregion': u'Central America', u'al
pha2Code': u'SV', u'gini': 48.3, u'alpha3Code': u'SLV', u'area': 21041.0, u'lang
uages': [u'es'], u'capital': u'San Salvador', u'relevance': u'0', u'borders': [u
'GTM', u'HND'], u'altSpellings': [u'SV', u'Republic of El Salvador', u'Rep\xfabl
ica de El Salvador'], u'currencies': [u'SVC', u'USD'], u'translations': {u'fr':
u'Salvador', u'de': u'El Salvador', u'ja': u'\u30a8\u30eb\u30b5\u30eb\u30d0\u30c
9\u30eb', u'es': u'El Salvador', u'it': u'El Salvador'}, u'nativeName': u'El Sal
vador', u'topLevelDomain': [u'.sv'], u'numericCode': u'222', u'population': 6401
240, u'callingCodes': [u'503'], u'name': u'El Salvador', u'region': u'Americas',
 u'_id': ObjectId('59f6551c7fae3b1290e4f136'), u'latlng': [13.83333333, -88.9166
6666]}, {u'timezones': [u'UTC+10:00'], u'demonym': u'Guamanian', u'subregion': u
'Micronesia', u'alpha2Code': u'GU', u'gini': None, u'alpha3Code': u'GUM', u'area
': 549.0, u'languages': [u'en', u'ch', u'es'], u'capital': u'Hag\xe5t\xf1a', u'r
elevance': u'0', u'borders': [], u'altSpellings': [u'GU', u'Gu\xe5h\xe5n'], u'cu
rrencies': [u'USD'], u'translations': {u'fr': u'Guam', u'de': u'Guam', u'ja': u'
\u30b0\u30a2\u30e0', u'es': u'Guam', u'it': u'Guam'}, u'nativeName': u'Guam', u'
topLevelDomain': [u'.gu'], u'numericCode': u'316', u'population': 159358, u'call
ingCodes': [u'1671'], u'name': u'Guam', u'region': u'Oceania', u'_id': ObjectId(
'59f6551c7fae3b1290e4f14d'), u'latlng': [13.46666666, 144.78333333]}, {u'timezon
es': [u'UTC-05:00'], u'demonym': u'Haitian', u'subregion': u'Caribbean', u'alpha
2Code': u'HT', u'gini': 59.2, u'alpha3Code': u'HTI', u'area': 27750.0, u'languag
es': [u'fr', u'ht'], u'capital': u'Port-au-Prince', u'relevance': u'0', u'border
s': [u'DOM'], u'altSpellings': [u'HT', u'Republic of Haiti', u"R\xe9publique d'H
a\xefti", u'Repiblik Ayiti'], u'currencies': [u'HTG', u'USD'], u'translations':
{u'fr': u'Ha\xefti', u'de': u'Haiti', u'ja': u'\u30cf\u30a4\u30c1', u'es': u'Hai
ti', u'it': u'Haiti'}, u'nativeName': u'Ha\xefti', u'topLevelDomain': [u'.ht'],
u'numericCode': u'332', u'population': 10911819, u'callingCodes': [u'509'], u'na
me': u'Haiti', u'region': u'Americas', u'_id': ObjectId('59f6551c7fae3b1290e4f15
3'), u'latlng': [19.0, -72.41666666]}, {u'timezones': [u'UTC+12:00'], u'demonym'
: u'Marshallese', u'subregion': u'Micronesia', u'alpha2Code': u'MH', u'gini': No
ne, u'alpha3Code': u'MHL', u'area': 181.0, u'languages': [u'en', u'mh'], u'capit
al': u'Majuro', u'relevance': u'0.5', u'borders': [], u'altSpellings': [u'MH', u
'Republic of the Marshall Islands', u'Aolep\u0101n Aor\u014dkin M\u0327aje\u013c
'], u'currencies': [u'USD'], u'translations': {u'fr': u'\xceles Marshall', u'de'
: u'Marshallinseln', u'ja': u'\u30de\u30fc\u30b7\u30e3\u30eb\u8af8\u5cf6', u'es'
: u'Islas Marshall', u'it': u'Isole Marshall'}, u'nativeName': u'M\u0327aje\u013
c', u'topLevelDomain': [u'.mh'], u'numericCode': u'584', u'population': 56086, u
'callingCodes': [u'692'], u'name': u'Marshall Islands', u'region': u'Oceania', u
'_id': ObjectId('59f6551c7fae3b1290e4f17d'), u'latlng': [9.0, 168.0]}, {u'timezo
nes': [u'UTC+10:00', u'UTC+11'], u'demonym': u'Micronesian', u'subregion': u'Mic
ronesia', u'alpha2Code': u'FM', u'gini': None, u'alpha3Code': u'FSM', u'area': 7
02.0, u'languages': [u'en'], u'capital': u'Palikir', u'relevance': u'0', u'borde
rs': [], u'altSpellings': [u'FM', u'Federated States of Micronesia'], u'currenci
es': [u'USD'], u'translations': {u'fr': u'Micron\xe9sie', u'de': u'Mikronesien',
 u'ja': u'\u30df\u30af\u30ed\u30cd\u30b7\u30a2\u9023\u90a6', u'es': u'Micronesia
', u'it': u'Micronesia'}, u'nativeName': u'Micronesia', u'topLevelDomain': [u'.f
m'], u'numericCode': u'583', u'population': 101351, u'callingCodes': [u'691'], u
'name': u'Federated States of Micronesia', u'region': u'Oceania', u'_id': Object
Id('59f6551c7fae3b1290e4f183'), u'latlng': [6.91666666, 158.25]}, {u'timezones':
 [u'UTC+10:00'], u'demonym': u'American', u'subregion': u'Micronesia', u'alpha2C
ode': u'MP', u'gini': None, u'alpha3Code': u'MNP', u'area': 464.0, u'languages':
 [u'en', u'ch'], u'capital': u'Saipan', u'relevance': u'0.5', u'borders': [], u'
altSpellings': [u'MP', u'Commonwealth of the Northern Mariana Islands', u'Sankat
tan Siha Na Islas Mari\xe5nas'], u'currencies': [u'USD'], u'translations': {u'fr
': u'\xceles Mariannes du Nord', u'de': u'N\xf6rdliche Marianen', u'ja': u'\u531
7\u30de\u30ea\u30a2\u30ca\u8af8\u5cf6', u'es': u'Islas Marianas del Norte', u'it
': u'Isole Marianne Settentrionali'}, u'nativeName': u'Northern Mariana Islands'
, u'topLevelDomain': [u'.mp'], u'numericCode': u'580', u'population': 53883, u'c
allingCodes': [u'1670'], u'name': u'Northern Mariana Islands', u'region': u'Ocea
nia', u'_id': ObjectId('59f6551c7fae3b1290e4f198'), u'latlng': [15.2, 145.75]},
{u'timezones': [u'UTC+09:00'], u'demonym': u'Palauan', u'subregion': u'Micronesi
a', u'alpha2Code': u'PW', u'gini': None, u'alpha3Code': u'PLW', u'area': 459.0,
u'languages': [u'en'], u'capital': u'Ngerulmud', u'relevance': u'0.5', u'borders
': [], u'altSpellings': [u'PW', u'Republic of Palau', u'Beluu er a Belau'], u'cu
rrencies': [u'USD'], u'translations': {u'fr': u'Palaos', u'de': u'Palau', u'ja':
 u'\u30d1\u30e9\u30aa', u'es': u'Palau', u'it': u'Palau'}, u'nativeName': u'Pala
u', u'topLevelDomain': [u'.pw'], u'numericCode': u'585', u'population': 20901, u
'callingCodes': [u'680'], u'name': u'Palau', u'region': u'Oceania', u'_id': Obje
ctId('59f6551c7fae3b1290e4f19c'), u'latlng': [7.5, 134.5]}, {u'timezones': [u'UT
C-05:00'], u'demonym': u'Panamanian', u'subregion': u'Central America', u'alpha2
Code': u'PA', u'gini': 51.9, u'alpha3Code': u'PAN', u'area': 75417.0, u'language
s': [u'es'], u'capital': u'Panama City', u'relevance': u'0', u'borders': [u'COL'
, u'CRI'], u'altSpellings': [u'PA', u'Republic of Panama', u'Rep\xfablica de Pan
am\xe1'], u'currencies': [u'PAB', u'USD'], u'translations': {u'fr': u'Panama', u
'de': u'Panama', u'ja': u'\u30d1\u30ca\u30de', u'es': u'Panam\xe1', u'it': u'Pan
ama'}, u'nativeName': u'Panam\xe1', u'topLevelDomain': [u'.pa'], u'numericCode':
 u'591', u'population': 3764166, u'callingCodes': [u'507'], u'name': u'Panama',
u'region': u'Americas', u'_id': ObjectId('59f6551c7fae3b1290e4f19e'), u'latlng':
 [9.0, -80.0]}, {u'timezones': [u'UTC-04:00'], u'demonym': u'Puerto Rican', u'su
bregion': u'Caribbean', u'alpha2Code': u'PR', u'gini': None, u'alpha3Code': u'PR
I', u'area': 8870.0, u'languages': [u'es', u'en'], u'capital': u'San Juan', u're
levance': u'0', u'borders': [], u'altSpellings': [u'PR', u'Commonwealth of Puert
o Rico', u'Estado Libre Asociado de Puerto Rico'], u'currencies': [u'USD'], u'tr
anslations': {u'fr': u'Porto Rico', u'de': u'Puerto Rico', u'ja': u'\u30d7\u30a8
\u30eb\u30c8\u30ea\u30b3', u'es': u'Puerto Rico', u'it': u'Porto Rico'}, u'nativ
eName': u'Puerto Rico', u'topLevelDomain': [u'.pr'], u'numericCode': u'630', u'p
opulation': 3548397, u'callingCodes': [u'1787', u'1939'], u'name': u'Puerto Rico
', u'region': u'Americas', u'_id': ObjectId('59f6551c7fae3b1290e4f1a6'), u'latln
g': [18.25, -66.5]}, {u'timezones': [u'UTC+09:00'], u'demonym': u'East Timorese'
, u'subregion': u'South-Eastern Asia', u'alpha2Code': u'TL', u'gini': 31.9, u'al
pha3Code': u'TLS', u'area': 14874.0, u'languages': [u'pt'], u'capital': u'Dili',
 u'relevance': u'0', u'borders': [u'IDN'], u'altSpellings': [u'TL', u'East Timor
', u'Democratic Republic of Timor-Leste', u'Rep\xfablica Democr\xe1tica de Timor
-Leste', u'Rep\xfablika Demokr\xe1tika Tim\xf3r-Leste'], u'currencies': [u'USD']
, u'translations': {u'fr': u'Timor oriental', u'de': u'Timor-Leste', u'ja': u'\u
6771\u30c6\u30a3\u30e2\u30fc\u30eb', u'es': u'Timor Oriental', u'it': u'Timor Es
t'}, u'nativeName': u'Timor-Leste', u'topLevelDomain': [u'.tl'], u'numericCode':
 u'626', u'population': 1212107, u'callingCodes': [u'670'], u'name': u'East Timo
r', u'region': u'Asia', u'_id': ObjectId('59f6551c7fae3b1290e4f1d3'), u'latlng':
 [-8.83333333, 125.91666666]}, {u'timezones': [u'UTC-04:00'], u'demonym': u'Turk
s and Caicos Islander', u'subregion': u'Caribbean', u'alpha2Code': u'TC', u'gini
': None, u'alpha3Code': u'TCA', u'area': 948.0, u'languages': [u'en'], u'capital
': u'Cockburn Town', u'relevance': u'0.5', u'borders': [], u'altSpellings': [u'T
C'], u'currencies': [u'USD'], u'translations': {u'fr': u'\xceles Turques-et-Ca\x
efques', u'de': u'Turks- und Caicosinseln', u'ja': u'\u30bf\u30fc\u30af\u30b9\u3
0fb\u30ab\u30a4\u30b3\u30b9\u8af8\u5cf6', u'es': u'Islas Turks y Caicos', u'it':
 u'Isole Turks e Caicos'}, u'nativeName': u'Turks and Caicos Islands', u'topLeve
lDomain': [u'.tc'], u'numericCode': u'796', u'population': 31458, u'callingCodes
': [u'1649'], u'name': u'Turks and Caicos Islands', u'region': u'Americas', u'_i
d': ObjectId('59f6551c7fae3b1290e4f1db'), u'latlng': [21.75, -71.58333333]}, {u'
timezones': [u'UTC-12:00', u'UTC-11:00', u'UTC-10:00', u'UTC-09:00', u'UTC-08:00
', u'UTC-07:00', u'UTC-06:00', u'UTC-05:00', u'UTC-04:00', u'UTC+10:00', u'UTC+1
2:00'], u'demonym': u'American', u'subregion': u'Northern America', u'alpha2Code
': u'US', u'gini': 48.0, u'alpha3Code': u'USA', u'area': 9629091.0, u'languages'
: [u'en'], u'capital': u'Washington, D.C.', u'relevance': u'3.5', u'borders': [u
'CAN', u'MEX'], u'altSpellings': [u'US', u'USA', u'United States of America'], u
'currencies': [u'USD', u'USN', u'USS'], u'translations': {u'fr': u'\xc9tats-Unis
', u'de': u'Vereinigte Staaten von Amerika', u'ja': u'\u30a2\u30e1\u30ea\u30ab\u
5408\u8846\u56fd', u'es': u'Estados Unidos', u'it': u"Stati Uniti D'America"}, u
'nativeName': u'United States', u'topLevelDomain': [u'.us'], u'numericCode': u'8
40', u'population': 321645000, u'callingCodes': [u'1'], u'name': u'United States
', u'region': u'Americas', u'_id': ObjectId('59f6551c7fae3b1290e4f1e1'), u'latln
g': [38.0, -97.0]}, {u'timezones': [u'UTC+02:00'], u'demonym': u'Zimbabwean', u'
subregion': u'Eastern Africa', u'alpha2Code': u'ZW', u'gini': None, u'alpha3Code
': u'ZWE', u'area': 390757.0, u'languages': [u'en', u'sn', u'nd'], u'capital': u
'Harare', u'relevance': u'0', u'borders': [u'BWA', u'MOZ', u'ZAF', u'ZMB'], u'al
tSpellings': [u'ZW', u'Republic of Zimbabwe'], u'currencies': [u'USD'], u'transl
ations': {u'fr': u'Zimbabwe', u'de': u'Simbabwe', u'ja': u'\u30b8\u30f3\u30d0\u3
0d6\u30a8', u'es': u'Zimbabue', u'it': u'Zimbabwe'}, u'nativeName': u'Zimbabwe',
 u'topLevelDomain': [u'.zw'], u'numericCode': u'716', u'population': 13061239, u
'callingCodes': [u'263'], u'name': u'Zimbabwe', u'region': u'Africa', u'_id': Ob
jectId('59f6551c7fae3b1290e4f1eb'), u'latlng': [-20.0, 30.0]}]
'''
