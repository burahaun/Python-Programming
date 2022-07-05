sales = int(input("Enter the total sales for the month: "))
state_tax = float(sales * 0.04)
country_tax = float(sales * 0.02)
total_tax = state_tax + country_tax
print("Monthly sales: $",sales)
print("State tax: $", state_tax)
print("Country tax: $", country_tax)
print("Total tax: $", total_tax)

