def car_chatbot():
    print("🤖 Welcome to Car Buying Assistant")
    print("-" * 40)

    
    buy = input("Are you looking to buy a car? (yes/no): ").lower()
    if buy != "yes":
        print("No problem! Visit us anytime 😊")
        return

    # Step 2: Budget
    budget = input("What is your budget (in lakhs)? ")

    # Step 3: Fuel type
    print("Fuel options: Petrol / Diesel / Electric")
    fuel = input("Which fuel type do you prefer?: ").lower()

    # Step 4: Car type
    print("Car types: Hatchback / Sedan / SUV")
    car_type = input("Which car type do you want?: ").lower()

    # Step 5: Engine
    engine = input("Preferred engine capacity (e.g. 1.2L, 1.5L, 2.0L): ")

    # Step 6: Transmission
    print("Transmission options: Manual / Automatic")
    transmission = input("Manual or Automatic?: ").lower()

    # Step 7: Mileage
    mileage = input("Expected mileage (km/l or km/charge): ")

    # Step 8: Features
    features = input("Any important features? (Sunroof, ABS, Airbags, Touchscreen): ")

    # Final Summary
    print("\n🧾 CUSTOMER REQUIREMENT SUMMARY")
    print("-" * 40)
    print(f"Budget: ₹{budget} Lakhs")
    print(f"Fuel Type: {fuel.capitalize()}")
    print(f"Car Type: {car_type.capitalize()}")
    print(f"Engine: {engine}")
    print(f"Transmission: {transmission.capitalize()}")
    print(f"Mileage Expectation: {mileage}")
    print(f"Key Features: {features}")

    print("\n✅ Thank you! Our sales executive will suggest best models for you.")


if __name__ == "__main__":
    car_chatbot()