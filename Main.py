import random

import matplotlib.pyplot as plt

print("=== RetireSmart AI ===")

# Client Information
current_age = 25
retirement_age = 65
current_savings = 50000
annual_contribution = 25000

retirement_goal = 1000000
inflation_rate = 0.03
simulations = 10000

# Optional Portfolio Allocation

stocks = 60
bonds = 40

# Choose:
# Conservative
# Moderate
# Aggressive

risk_profile = "moderate"

# Allocation override

if stocks is not None and bonds is not None:

    mean_return = (
        (stocks / 100) * 0.10 +
        (bonds / 100) * 0.04
    )

    volatility = (
        (stocks / 100) * 0.15 +
        (bonds / 100) * 0.05
    )

# Otherwise use risk profile

elif risk_profile == "Conservative":
    mean_return = 0.05
    volatility = 0.08

elif risk_profile == "Moderate":
    mean_return = 0.07
    volatility = 0.12

else:
    mean_return = 0.09
    volatility = 0.18


# Years to retirement
years = retirement_age - current_age

# Run simulations
results = []

for simulation in range(simulations):

    balance = current_savings

    for year in range(years):

        annual_return = random.normalvariate(
            mean_return,
            volatility
        )

        balance *= (1 + annual_return)
        balance += annual_contribution

    results.append(balance)

# Statistics
results.sort()

median_balance = results[len(results) // 2]
worst_case = results[int(len(results) * 0.10)]
best_case = results[int(len(results) * 0.90)]

# Success calculation
# Inflation assumptions
inflation_rate = 0.03

# Inflate today's $1M goal into future dollars
target = retirement_goal * ((1 + inflation_rate) ** years)

successes = 0

for result in results:
    if result >= target:
        successes += 1

success_rate = (successes / len(results)) * 100

# Retirement readiness score

if success_rate >= 90:
    summary = "Your retirement plan appears very strong."

elif success_rate >= 75:
    summary = "Your retirement plan is on track but could be improved."

elif success_rate >= 50:
    summary = "Your retirement plan has a moderate chance of success."

else:
    summary = "Consider increasing contributions, delaying retirement, or adjusting investment risk."

print("\n=== AI SUMMARY ===")
print(summary)

# Allocation message

if stocks is not None and bonds is not None:

    print("\n=== PORTFOLIO ALLOCATION ===")
    print("Stocks:", stocks, "%")
    print("Bonds:", bonds, "%")

    print("\nAllocation Override Active")
    print("RetireSmart AI is using your portfolio allocation instead of the risk profile.")

else:

    print("\n=== PORTFOLIO ALLOCATION ===")
    print("No allocation provided.")
    print("Using Risk Profile:", risk_profile)


# Report
print("\n=== CLIENT REPORT ===")
print("Risk Profile:", risk_profile)
print("Current Age:", current_age)
print("Retirement Age:", retirement_age)
print("Years Until Retirement:", years)

print("\n=== RESULTS ===")
print("Median Outcome: $", round(median_balance, 2))
print("Worst 10% Outcome: $", round(worst_case, 2))
print("Best 10% Outcome: $", round(best_case, 2))

print("Inflation-Adjusted Goal: $", round(target, 2))
print("\nSuccess Rate:", round(success_rate, 1), "%")
print("Retirement Readiness:", rating)
print("Simulations Run:", simulations)


plt.hist(results, bins=30)
plt.title("RetireSmart AI Simulation Results")
plt.xlabel("Portfolio Value at Retirement")
plt.ylabel("Number of Simulations")
plt.show()

# Create Retirement Outcome Chart

plt.figure(figsize=(10, 6))

# Histogram
plt.hist(
    results,
    bins=30,
    color="skyblue",
    edgecolor="black"
)

# Retirement Goal Line
plt.axvline(
    target,
    color="red",
    linestyle="--",
    linewidth=3,
    label="Retirement Goal"
)

# Median Outcome Line
plt.axvline(
    median_balance,
    color="green",
    linestyle="-",
    linewidth=3,
    label="Median Outcome"
)

# Titles and Labels
plt.title(
    "RetireSmart AI\nRetirement Outcome Distribution"
)

plt.xlabel("Portfolio Value at Retirement ($)")
plt.ylabel("Number of Simulations")

# Legend
plt.legend()

# Grid
plt.grid(True, alpha=0.3)

# Show Chart
plt.show()
