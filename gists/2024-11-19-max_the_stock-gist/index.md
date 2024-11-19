# 2024-11-19-max_the_stock-gist

**Gist file**: [https://gist.github.com/athursto/fe647a113fd8f78a3cebfe4db4521b02](https://gist.github.com/athursto/fe647a113fd8f78a3cebfe4db4521b02)

**Description**: Cassidy's interview question of the week: a function to find the maximum profit you can achieve buying and selling a stock once

## max_the_stock.py

```Python

"""
11.19.2024
Given an array of integers representing the stock prices of a company in chronological order, write a function that determines the maximum profit you can achieve by buying and selling the stock once. If no profit can be made, return 0."""

def max_the_stock(arr):
    # buy as low as possible
    # sell as high as possible
    current_min_price, current_max_price = arr[0], arr[0]
    max_profit = -2
    for i in range(1, len(arr)):
        if arr[i] < current_min_price:
            current_min_price = arr[i]
        if arr[i] > current_max_price:
            current_max_price = arr[i]
        potential_profit = arr[i] - current_min_price
        if potential_profit > 0 and potential_profit > max_profit:
            #print(f"new best day to sell found at price {arr[i]}-- if bought at {current_min_price}")
            max_profit = potential_profit
    return max_profit if max_profit > 0 else 0


assert max_the_stock([7, 1, 5, 3, 6, 4]) == 5
assert max_the_stock([7, 6, 4, 3, 1]) == 0
```

```js
function maxTheStock(arr) {
    let currentMinPrice = arr[0]
    let currentMaxPrice = arr[0]
    let maxProfit = -2
    for (let i=1; i<arr.length; i++) {
      console.log(`checking ${arr[i]}`)
       if (arr[i] < currentMinPrice){
            currentMinPrice = arr[i]
       }
      if (arr[i] > currentMaxPrice){
            currentMaxPrice = arr[i]
       }
      potentialProfit = arr[i] - currentMinPrice
        
        if (potentialProfit > 0 && potentialProfit > maxProfit){
            console.log(`new best day to sell found at price ${arr[i]}-- if bought at ${currentMinPrice}`)
            maxProfit = potentialProfit
        }}
    if (maxProfit >0) {
      return maxProfit
    } else {
      return 0
    }
}

arr_test = [7, 1, 5, 3, 6, 4]
console.log(maxTheStock(arr_test))

```