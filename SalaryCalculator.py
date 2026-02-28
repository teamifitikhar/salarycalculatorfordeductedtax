def reverse_salary_from_tax(tax_deducted):
    """
    Reverse engineer the total salary from the deducted tax
    based on the updated Pakistani salaried tax slabs (explicit if-else style).
    """

    # Slab 1
    if tax_deducted == 0:
        return "Salary is between 0 and 600,000 (no tax)."

    # Slab 2
    if 0 < tax_deducted <= (1200000 - 600000) * 0.05:
        salary = tax_deducted / 0.05 + 600000
        return salary+1

    # Slab 3
    if (1200000 - 600000) * 0.05 < tax_deducted <= 30000 + (2200000 - 1200000) * 0.15:
        salary = (tax_deducted - 30000) / 0.15 + 1200000
        return salary+1

    # Slab 4
    if 180000 < tax_deducted <= 430000 + (3200000 - 2200000) * 0.25:
        salary = (tax_deducted - 180000) / 0.25 + 2200000
        return salary+1

    # Slab 5
    if 430000 < tax_deducted <= 700000 + (4100000 - 3200000) * 0.30:
        salary = (tax_deducted - 430000) / 0.30 + 3200000
        return salary+1

    # Slab 6
    if tax_deducted > 700000:
        salary = (tax_deducted - 700000) / 0.35 + 4100000
        return salary+1

    return "Tax amount does not fit in the given slabs."


# Loop for repeated inputs
while True:
    user_input = input("Enter deducted tax amount (or 'exit' to quit): ").strip().lower()
    if user_input in ("exit", "quit", "q"):
        print("Exiting...")
        break

    try:
        tax_input = float(user_input)
        salary = reverse_salary_from_tax(tax_input)
        print("Estimated annual salary:", salary)
    except ValueError:
        print("Invalid input! Please enter a number or 'exit'.")
