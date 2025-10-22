def main():
    print("Amount due: 50")
    input_coin = int(input("Insert Coin: "))
    coke = 50

    while input_coin not in [50,25,10,5]:
        print("Amount due: 50")
        input_coin = int(input("Insert Coin: "))

    while coke - input_coin != 0:
        coke = coke - input_coin
        print(f"Amount due: {coke}")
        input_coin = int(input("Insert Coin: "))

    print("Amount due: 0")

if __name__ == "__main__":
    main()
        

        
