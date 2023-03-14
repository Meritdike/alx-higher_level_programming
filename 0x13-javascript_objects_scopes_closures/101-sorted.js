#!/usr/bin/node
const dict = require('./101-data').dict;
const dictValues = Object.values(dict).filter((elem, index, self) => self.indexOf(elem) === index);
const newObj = {};
for (let i = 0; i < dictValues.length; i++) {
  const dictKeys = Object.keys(dict).filter((elem, index) => dict[elem] === dictValues[i]);
  newObj[dictValues[i]] = dictKeys;
}
console.log(newObj);
