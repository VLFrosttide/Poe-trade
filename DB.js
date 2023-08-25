"use strict";

// let ChaosOrb = ({
//   Base: 20,
//   Quant: 10,
//   MinQuant: 50,
//   MaxQuant: 1000,
//   Name: "ChaosOrb",
//   Price: 1,
// });
let DivineOrb = {
  Base: 10,
  Quant: 0,
  MinQuant: 5,
  MaxQuant: 10,
  Name: "DivineOrb",
  Price: 100,
};
let ExaltedOrb = {
  Base: 10,
  Quant: 2,
  MinQuant: 5,
  MaxQuant: 15,
  Name: "ExaltedOrb",
  Price: 10,
};
let OrbofAnnulment = {
  Base: 20,
  Quant: 1,
  MinQuant: 5,
  MaxQuant: 25,
  Name: "OrbofAnnulment",
  Price: 7,
};
let OrbofAlteration = {
  Base: 20,
  Quant: 447,
  MinQuant: 200,
  MaxQuant: 2000,
  Name: "OrbofAlteration",
  Price: 0.3,
};
let OrbofUnmaking = {
  Base: 40,
  Quant: 1,
  MinQuant: 10,
  MaxQuant: 150,
  Name: "OrbofUnmaking",
  Price: 2,
};

let CurrencyList = {
  DivineOrb,
  ExaltedOrb,
  OrbofAlteration,
  OrbofAnnulment,
  OrbofUnmaking,
};
module.exports = CurrencyList;
