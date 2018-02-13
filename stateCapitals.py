import random

states = [
    'Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming'
    ]
state_capital_dictionary = {'Alabama':{'capital':'Montgomery','correct':0,'wrong':0},'Alaska':{'capital':'Juneau','correct':0,'wrong':0},'Arizona':{'capital':'Phoenix','correct':0,'wrong':0},'Arkansas':{'capital':'Little Rock','correct':0,'wrong':0},'California':{'capital':'Sacramento','correct':0,'wrong':0},'Colorado':{'capital':'Denver','correct':0,'wrong':0},
                            'Connecticut':{'capital':'Hartford','correct':0,'wrong':0},'Delaware':{'capital':'Dover','correct':0,'wrong':0},'Florida':{'capital':'Tallahassee','correct':0,'wrong':0},'Georgia':{'capital':'Atlanta','correct':0,'wrong':0},
                   'Hawaii':{'capital':'Honolulu','correct':0,'wrong':0},'Idaho':{'capital':'Boise','correct':0,'wrong':0},'Illinois':{'capital':'Springfield','correct':0,'wrong':0},'Indiana':{'capital':'Indianapolis','correct':0,'wrong':0},'Iowa':{'capital':'Des Moines','correct':0,'wrong':0},'Kansas':{'capital':'Topeka','correct':0,'wrong':0},
                            'Kentucky':{'capital':'Frankfurt','correct':0,'wrong':0},'Louisiana':{'capital':'Baton Rouge','correct':0,'wrong':0},'Maine':{'capital':'Augusta','correct':0,'wrong':0},'Maryland':{'capital':'Annapolis','correct':0,'wrong':0},
                   'Massachusetts':{'capital':'Boston','correct':0,'wrong':0},'Michigan':{'capital':'Lansing','correct':0,'wrong':0},'Minnesota':{'capital':'Saint Paul','correct':0,'wrong':0},'Mississippi':{'capital':'Jackson','correct':0,'wrong':0},'Missouri':{'capital':'Jefferson City','correct':0,'wrong':0},'Montana':{'capital':'Helena','correct':0,'wrong':0},
                            'Nebraska':{'capital':'Lincoln','correct':0,'wrong':0},'Nevada':{'capital':'Carson City','correct':0,'wrong':0},'New Hampshire':{'capital':'Concord','correct':0,'wrong':0},'New Jersey':{'capital':'Trenton','correct':0,'wrong':0},
                   'New Mexico':{'capital':'Santa Fe','correct':0,'wrong':0},'New York':{'capital':'Albany','correct':0,'wrong':0},'North Carolina':{'capital':'Raleigh','correct':0,'wrong':0},'North Dakota':{'capital':'Bismarck','correct':0,'wrong':0},'Ohio':{'capital':'Columbus','correct':0,'wrong':0},
                            'Oklahoma':{'capital':'Oklahoma City','correct':0,'wrong':0},'Oregon':{'capital':'Salem','correct':0,'wrong':0},'Pennsylvania':{'capital':'Harrisburg','correct':0,'wrong':0},'Rhode Island':{'capital':'Providence','correct':0,'wrong':0},'South Carolina':{'capital':'Columbia','correct':0,'wrong':0},
                   'South Dakota':{'capital':'Pierre','correct':0,'wrong':0},'Tennessee':{'capital':'Nashville','correct':0,'wrong':0},'Texas':{'capital':'Austin','correct':0,'wrong':0},'Utah':{'capital':'Salt Lake City','correct':0,'wrong':0},'Vermont':{'capital':'Montpelier','correct':0,'wrong':0},'Virginia':{'capital':'Richmond','correct':0,'wrong':0},
                            'Washington':{'capital':'Olympia','correct':0,'wrong':0},'West Virginia':{'capital':'Charleston','correct':0,'wrong':0},'Wisconsin':{'capital':'Madison','correct':0,'wrong':0},'Wyoming':{'capital':'Cheyenne','correct':0,'wrong':0}
                   }
accuracy_tracker = {'correct':0,'wrong':0,'totalCorrect':0,'totalWrong':0}


print('Let\'s play a game of guessing state capitals')
print('Do you want to play?  Y or N?')
res = input()
while res.lower() == 'y':
    random.shuffle(states)
    for i in range(len(states)):
        print('What is the capital of ' + states[i] + '?')
        guess = input()
        if guess.lower() == state_capital_dictionary[states[i]]['capital'].lower():
            print(guess + ' is correct!')
            accuracy_tracker['correct'] += 1
            state_capital_dictionary[states[i]]['correct'] += 1
            print('This capital has been guessed correctly ' + str(state_capital_dictionary[states[i]]['correct']) + ' out of ' + str(state_capital_dictionary[states[i]]['correct'] + state_capital_dictionary[states[i]]['wrong']) + ' times.') 
        else:
            print('The correct answer was ' + state_capital_dictionary[states[i]]['capital'])
            accuracy_tracker['wrong'] += 1
            state_capital_dictionary[states[i]]['wrong'] += 1
            print('This capital has been guessed correctly ' + str(state_capital_dictionary[states[i]]['correct']) + ' out of ' + str(state_capital_dictionary[states[i]]['correct'] + state_capital_dictionary[states[i]]['wrong']) + ' times.')
    print('Your accuracy this game was ' + str(accuracy_tracker['correct']) + ' right of 50')
    accuracy_tracker['totalCorrect'] = accuracy_tracker['totalCorrect']  + accuracy_tracker['correct']
    accuracy_tracker['totalWrong'] = accuracy_tracker['totalWrong'] + accuracy_tracker['wrong']
    accuracy_tracker['wrong'] = 0
    accuracy_tracker['correct'] = 0
    guessAccuracy = (accuracy_tracker['totalCorrect'] / (accuracy_tracker['totalCorrect'] + accuracy_tracker['totalWrong'])) * 100
    guessAccuracy = round(guessAccuracy, 2)
    print('Your cumulative guess accuracy is ' + str(guessAccuracy) + '%.')
    print('Do you want to play again? Y or N?')
    res = input()
print('Ok, let\'s play another time!')    

        
    
