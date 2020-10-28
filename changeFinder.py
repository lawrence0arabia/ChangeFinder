desiredAmount = float(input("How much change do you need?\n"))
currentAmount = 0.0

def coinFinder(coinValue, coinName):
    global currentAmount
    coinCount = 0
    while currentAmount + coinValue <= desiredAmount:
        currentAmount = currentAmount + coinValue
        coinCount = coinCount + 1
    print(str(coinName) + ": " + str(coinCount))

coinFinder(100, "Hundred Dollars")
coinFinder(50, "Fifty Dollars")
coinFinder(20, "Twenty Dollars")
coinFinder(10, "Ten Dollars")
coinFinder(5, "Five Dollars")
coinFinder(2, "Two Dollars")
coinFinder(1, "One Dollars")
coinFinder(.50, "Fifty Cents")
coinFinder(.20, "Twenty Cents")
coinFinder(.10, "Ten Cents")
coinFinder(.05, "Five Cents")
