/* 7 kyu "Number of People in the Bus" by Aryan-firouzian 
There is a bus moving in the city which takes and drops some people at each bus stop.
You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.
Take a look on the test cases.
Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.
The second value in the first pair in the array is 0, since the bus is empty in the first bus stop. */

var number = function(busStops) {
    let peopleInBus = 0 
    for (let cont = 0; cont < busStops.length; cont++) {
      peopleInBus += busStops[cont][0]
      peopleInBus -= busStops[cont][1]
    }
    return peopleInBus
}
  