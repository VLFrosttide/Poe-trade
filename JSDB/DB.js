"use strict";

class Currency {
  constructor({ Base, Quant, MinQuant, MaxQuant, Price, Name }) {
    this.Base = Base;
    this.Quant = Quant;
    this.MinQuant = MinQuant;
    this.MaxQuant = MaxQuant;
    this.Price = Price;
    this.Name = Name;
  }
}

let ChaosOrb = new Currency({
  Base: 20,
  Quant: 10,
  MinQuant: 50,
  MaxQuant: 1000,
  Name: "Chaos Orb",
});
let DivineOrb = new Currency({
  Base: 10,
  Quant: 0,
  MinQuant: 5,
  MaxQuant: 10,
  Name: "Divine Orb",
});
let ExaltedOrb = new Currency({
  Base: 10,
  Quant: 2,
  MinQuant: 5,
  MaxQuant: 15,
  Name: "Exalted Orb",
});
let AnnulOrb = new Currency({
  Base: 20,
  Quant: 1,
  MinQuant: 5,
  MaxQuant: 25,
  Name: "Orb of Annulment",
});
let AlterationOrb = new Currency({
  Base: 20,
  Quant: 447,
  MinQuant: 200,
  MaxQuant: 2000,
  Name: "Alteration Orb",
});
let UnmakingOrb = new Currency({
  Base: 40,
  Quant: 1,
  MinQuant: 10,
  MaxQuant: 150,
  Name: "Orb of Unmaking",
});

let CurrencyList = {
  ChaosOrb,
  DivineOrb,
  ExaltedOrb,
  AlterationOrb,
  AnnulOrb,
  UnmakingOrb,
};
console.log(CurrencyList);
module.exports = CurrencyList;
