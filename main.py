import matplotlib.pyplot as plt

def investment_simulation(monthly_amounth, annual_profit_rate, years):
    total_investment = 200000
    years_investment_list = []
    for year in range(years):
        total_investment += (monthly_amounth * 12) 
        total_investment *= (1 + annual_profit_rate)
        years_investment_list.append(total_investment)

    return total_investment, years_investment_list

result, years_investment_list = (investment_simulation(monthly_amounth = 5000,
                    annual_profit_rate = 0.08,
                    years = 20))
result = round(result)
print(result)
# print(years_investment_list)

rounded_yeras_investments_list = []
for i in years_investment_list:
    rounded_yeras_investments_list.append(round(i))

# Chart 
def create_chart(data):
    
    # Create a line plot
    plt.figure(figsize=(10, 6))
    plt.plot(data, marker='o')

    # Adding labels and title
    plt.title("Investment")
    plt.xlabel("Years")
    plt.ylabel("Values")

    # Show the chart with grid
    plt.grid(True)
    plt.show()

create_chart(rounded_yeras_investments_list)

# 44520       42000
# 91711.2     84000
# 141733.872  126000

# 586808    420000      +  166 808   po 10 letech   pri 6% rocne     753895 pri pocatecni investici 93300
# 1637694   840000      +  797 694   po 20 letech   pri 6% rocne    1936920 pri pocatecni investici 93300
# 3519670   1260000     +2 259 670   po 30 letech   pri 6% rocne    4055538 pri pocatecni investici 93300

'''2393891 kc pri pocatecnim vkladu 200 000 a pravidelnem investovani 5000 kc po dobu 15 let.
5168231 kc za dalsich 10 v pripade ze nevkladame zadne financni prostredky.
5192889 kc po prvnim roce kdy si vyberu 360 000 kc na duchodek :)
5219520 po druhem roku, 5248282 po tretim roce, 5279345 po ctvrtem roce  '''

