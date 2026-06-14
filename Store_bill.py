def main():
    print("=" * 50)
    print("SYSTEM INITIALIZATION: ORDER PROCESSING ENGINE")
    print("=" * 50)

    SYSTEM_KEY = "SECURE_AUTH_2026"
    MAX_LOGIN_ATTEMPTS = 3
    assigned= False

    for _ in range(1,4):
        key = input("Enter System Access Key: ")
        if key == SYSTEM_KEY:
            is_key = True
            break
        else:
            print("Invalid key.")

    if not is_key:
        print("Enter valid system key")
        return

    print("\n[SUCCESS] Authentication Verified. Loading transactional modules...\n")

    Current_Inventory_Item= "Enterprise AI Edge Compute Unit"
    Price_per_Unit = 1250.50
    Stock_Available = 15

    print(f"Current Inventory Item: {Current_Inventory_Item}")
    print(f"Price per Unit: ${Price_per_Unit} | Stock Available: {Stock_Available}")
    print("-" * 50)

    try:
        qty = int(input("Enter requested purchase quantity: "))
        discount = float(input("Enter applicable discount percentage (0-100): "))
    except ValueError:
        print("Invalid input.")
        return

    print("\nExecuting Transactional Validation Gates...")
    
    if qty <= 0:
        print("Validating Order Bounds... Fail.")
        return
    else:
        print("Validating Order Bounds... Pass.")

    if qty > Stock_Available:
        print("Verifying Warehouse Allocation Inventory... Fail.")
        return
    else:
        print("Verifying Warehouse Allocation Inventory... Pass.")

    subtotal = qty * Price_per_Unit
    discount = subtotal * (discount / 100)
    tax_amount = (subtotal - discount) * 0.08
    total_cost = (subtotal - discount) + tax_amount

    print("\n" + "=" * 50)
    print("FINAL TRANSACTION STATEMENT / RECEIPT")
    print("=" * 50)
    print(f"Item Profile:       {Current_Inventory_Item}")
    print(f"Quantity Processed: {qty}")
    print(f"Base Subtotal:      ${subtotal:,.2f}")
    print(f"Applied Discount:  -${discount:,.2f}")
    
    print(f"Tax Allocation(8%): ${tax_amount:,.2f}")
    print("-" * 50)
    print(f"Total Gross Amount: ${total_cost:,.2f}")
    print("=" * 50)

if __name__ == "__main__":
    main()