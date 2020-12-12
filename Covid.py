import requests


# to get information about the international country
def by_country():
    name = input('Enter country: ')

    # url address of the API in question concatenated with the name of the country
    url = 'https://coronavirus-19-api.herokuapp.com/countries/' + (name)
    # Sending http request to get the data above into python script
    res = requests.get(url)

    # to get the data in JSON format
    data = res.json()

    #to get the desired data/ individual elements from the data
    cases = data['cases']
    recovered = data['recovered']
    active = data['active']
    critical = data['critical']
    deaths = data['deaths']

    todayCases = data['todayCases']
    todayDeaths = data['todayDeaths']


    print()
    print('Total Cases : {}'.format(cases))
    print('Total recovered : {}'.format(recovered))
    print('Total active : {}'.format(active))
    print('Total critical : {}'.format(critical))
    print('TOtal deaths : {}'.format(deaths))
    print()
    print('Cases registered today : {}'.format(todayCases))
    print('Deaths registered today : {}'.format(todayDeaths))




# to get information of the different states in USA itself
def by_USstate():
    state = input('Enter the state in USA: ')

    # url address of the API in question formatted with the state of the country
    url = 'https://api.covidtracking.com/v1/states/{0}/current.json'.format(state)

    # Sending http request to get the data above into python script
    res = requests.get(url)

    # to get the data in JSON format
    data = res.json()

    #to get the desired data/ individual elements from the data
    date = data['date']
    total = data['total']
    recovered = data['recovered']
    hospitalized = data['hospitalized']
    hospitalizedIncrease = data['hospitalizedIncrease']
    death = data['death']
    deathIncrease = data['deathIncrease']

    hospitalizedCurrently = data['hospitalizedCurrently']
    inIcuCurrently = data['inIcuCurrently']
    onVentilatorCurrently = data['onVentilatorCurrently']


    print()
    print('Date of the published data : {}'.format(date))
    print('Total Cases : {}'.format(total))
    print('Total recovered : {}'.format(recovered))
    print('Total hospitalized : {}'.format(hospitalized))
    print('Total hospitalized increase : {}'.format(hospitalizedIncrease))
    print('Total deaths : {}'.format(death))
    print('Total increase in deaths : {}'.format(deathIncrease))
    print()
    print('Total hospitalized today : {}'.format(hospitalizedCurrently))
    print('Total in ICU today : {}'.format(inIcuCurrently))
    print('Total on ventilator today : {}'.format(onVentilatorCurrently))


def main():
    print('Welcome.')
    print('This application uses two specific APIs to bring forth to you,')
    print('the information regarding COVID-19 status around us.')
        
    
    choice = ''

    while(choice != '3'):
        print()
        print('1. Get data by country')
        print('2. Get data by US state')
        print('3. Exit')
        print()

        choice = input('Enter your choice : ')
        
            
        if choice == '1':
            by_country()
            
        elif choice == '2':
            by_USstate()        
            
        elif choice == '3':
            print('Bye.')

        else:
            print('Try again.')

    print('Thank you.')


if __name__=='__main__':
    main()



