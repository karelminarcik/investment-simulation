import matplotlib.pyplot as plt

def investment_simulation(monthly_amount, annual_profit_rate, years, initial_investment=200000):
    total_investment = initial_investment
    total_invested = initial_investment
    years_investment_list = []
    years_total_invested_list = []

    for year in range(1, years + 1):
        total_investment += (monthly_amount * 12)  # Add yearly investment
        total_investment *= (1 + annual_profit_rate)  # Apply growth

        total_invested += (monthly_amount * 12)  # Track total invested separately

        years_investment_list.append(round(total_investment))
        years_total_invested_list.append(total_invested)  # Track yearly invested amount

    return round(total_investment), years_investment_list, years_total_invested_list

# Chart 
def create_chart(investment_values, invested_values, years):
    plt.figure(figsize=(10, 6))

    # Investment growth line
    plt.plot(investment_values, marker='o', linestyle='-', color='b', label="Investment Growth")

    # Total invested line
    plt.plot(invested_values, marker='s', linestyle='--', color='r', label="Total Invested")

    # Labels & Titles
    plt.title("Investment Growth vs. Total Invested", fontsize=14)
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("Amount (CZK)", fontsize=12)

    # Set X-axis labels to "Year 1, Year 2, ..." instead of just numbers
    plt.xticks(range(years), [f"Y {i}" for i in range(1, years + 1)])

    # Show legend
    plt.legend()

    # Display grid for better readability
    plt.grid(True, linestyle='--', alpha=0.6)

    # Annotate the final values at the end of each line (moved slightly up)
    final_year = years - 1
    plt.text(final_year, investment_values[-1], f"{investment_values[-1]:,} CZK", 
             verticalalignment='bottom', horizontalalignment='left', fontsize=10, color='b', fontweight='bold', 
             va='bottom', ha='left')

    plt.text(final_year, invested_values[-1], f"{invested_values[-1]:,} CZK", 
             verticalalignment='bottom', horizontalalignment='left', fontsize=10, color='r', fontweight='bold', 
             va='bottom', ha='left')

    plt.show()

def investment_app(monthly_amount, annual_profit_rate, years):
    final_value, years_investment_list, years_total_invested_list = investment_simulation(
        monthly_amount, annual_profit_rate, years
    )

    print(f"Final Investment Value: {final_value:,} CZK")
    print(f"Total Amount Invested Over {years} Years: {years_total_invested_list[-1]:,} CZK")

    create_chart(years_investment_list, years_total_invested_list, years)

# Run the simulation
investment_app(5000, 0.08, 20)
