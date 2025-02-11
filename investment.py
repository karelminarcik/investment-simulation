import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

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

# Custom number formatter to add spaces in large numbers
def format_with_spaces(x, _):
    return f"{int(x):,}".replace(",", " ")  # Replace comma with space

# Chart 
def create_chart(investment_values, invested_values, years, monthly_amount, annual_profit_rate):
    plt.figure(figsize=(10, 6))

    # Set window title (Renames "Figure 1" to "Investment Simulation")
    plt.gcf().canvas.manager.set_window_title("Investment Simulation")

    # Investment growth line
    plt.plot(investment_values, marker='o', linestyle='-', color='b', label="Investment Growth")

    # Total invested line
    plt.plot(invested_values, marker='s', linestyle='--', color='r', label="Total Invested")

    # Title with second line showing assignment values
    title_text = "Investment Growth vs. Total Invested\n"
    title_text += f"Investment: {format_with_spaces(monthly_amount, None)} CZK/month | Profit Rate: {annual_profit_rate * 100:.1f}% | Years: {years}"
    
    plt.title(title_text, fontsize=14, fontweight='bold')

    # Labels & Titles
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("Amount (CZK)", fontsize=12)

    # Ensure Y-axis values are in full numbers with spaces
    plt.gca().get_yaxis().set_major_formatter(mticker.FuncFormatter(format_with_spaces))

    # Set X-axis labels to "Year 1, Year 2, ..." instead of just numbers
    plt.xticks(range(years), [f"Y {i}" for i in range(1, years + 1)])

    # Show legend
    plt.legend()

    # Display grid for better readability
    plt.grid(True, linestyle='--', alpha=0.6)

    # Annotate the final values at the end of each line (moved higher)
    final_year = years - 1
    plt.text(final_year, investment_values[-1] + 5000, f"{format_with_spaces(investment_values[-1], None)} CZK",  
             verticalalignment='bottom', horizontalalignment='left', fontsize=10, color='b', fontweight='bold')

    plt.text(final_year, invested_values[-1] + 5000, f"{format_with_spaces(invested_values[-1], None)} CZK",  
             verticalalignment='bottom', horizontalalignment='left', fontsize=10, color='r', fontweight='bold')

    plt.show()

def investment_app(monthly_amount, annual_profit_rate, years):
    final_value, years_investment_list, years_total_invested_list = investment_simulation(
        monthly_amount, annual_profit_rate, years
    )

    print(f"Final Investment Value: {format_with_spaces(final_value, None)} CZK")
    print(f"Total Amount Invested Over {years} Years: {format_with_spaces(years_total_invested_list[-1], None)} CZK")

    create_chart(years_investment_list, years_total_invested_list, years, monthly_amount, annual_profit_rate)

# Run the simulation
investment_app(5000, 0.08, 15)
