// given an array, find the highest, lowest, average, and mode of that array
// return an object with the key being highest, lowest etc, and the value being the value form the array

// take in an array
// iterate the array
// find the highest value, and lowest value
// add up all items in the array and divide by the amount of items for average
// track how many times each value shows up, and the highest amount is the mode

function findStuff(arr) {
  // Iterate the array
  // this will hold the sum of all values
  let sum = 0;
  // we need to track highest and lowest
  // we start at the first value so we can account for all negatives and positives
  let highest = arr[0];
  let lowest = arr[0];
  let map = {};
  // for each value in the array the value as the key
  // each associated value will be the count
  for (var i = 0; i < arr.length; i++) {
    // check if we have seen the value before
    if (map.hasOwnProperty(arr[i])) {
      // if we have seen the value we increase the count by 1
      map[arr[i]] += 1;
    } else {
      // if we haven't seen the value we set the count to 1 (since it's now appearing for the first time)
      map[arr[i]] = 1;
    }
    // we need to keep a running tally of sum
    sum += arr[i];
    // we need to check for highest and lowest and see if our current value is either higher or lower
    if (arr[i] > highest) {
      highest = arr[i];
    }
    if (arr[i] < lowest) {
      lowest = arr[i];
    }
  }
  // need to find the highest value in the map object
  // start at the first value in the array
  let mode = arr[0];
  // iterate the object
  for (const value in map) {
    // check if the count is higher then the count of the first value in the array
    // we need to check the value(count) associated with each value in the array against the previous highest count
    if (map[value] > map[mode]) {
      // if the count is higher, we replace the mode with that key (which is the value in the array)
      mode = value;
    }
  }
  // our return object with the results
  let finalStuff = {};
  finalStuff["Average"] = sum / (arr.length + 1);
  finalStuff["Highest"] = highest;
  finalStuff["Lowest"] = lowest;
  finalStuff["Mode"] = mode;
  return finalStuff;
}

console.log(findStuff([1, 3, 5, 5, 7, 5, 3, 1, 1, 1, 7, 1, 1, 1]));
