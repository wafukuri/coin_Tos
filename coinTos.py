import random

def coin_toss():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

def main():
    user_name = input("Who are you?\n> ")
    print(f"Hello, {user_name}!")
    print("Tossing a coin...")

    heads_count = 0
    tails_count = 0
    results = []

    for round in range(1, 4):
        result = coin_toss()
        results.append(result)
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
        print(f"Round {round}: {result}")

    print(f"Heads: {heads_count}, Tails: {tails_count}")

if __name__ == "__main__":
    main()
