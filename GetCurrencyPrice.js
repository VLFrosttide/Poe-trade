let NewName;
let NewPrice;
const mysql = require("mysql");
console.log("This the arg " + process.argv[2]); // Just checking how args are passed
const con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "poetrade",
});
con.connect();

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
function RoundUp(number, decimalPlaces) {
  const multiplier = Math.pow(10, decimalPlaces);
  return Math.ceil(number * multiplier) / multiplier;
}

let AllCurrenciesList = {};
fetch(
  "https://poe.ninja/api/data/currencyoverview?league=Ancestor&type=Currency"
)
  .then((response) => response.json())
  .then((data) => {
    const FilteredData = data.lines.filter((line) =>
      line.hasOwnProperty("currencyTypeName")
    );
    FilteredData.forEach((line) => {
      NewName = line.currencyTypeName.replaceAll(" ", "").replaceAll("'", "");
      NewPrice = line.receive ? line.receive.value : 0;

      AllCurrenciesList[NewName] = {
        Price: NewPrice,
        Name: NewName,
      };
    });
    for (const Item in AllCurrenciesList) {
      let AllCurrenciesListItem = AllCurrenciesList[Item].Name;

      if (CurrencyList.hasOwnProperty(AllCurrenciesListItem)) {
        CurrencyList[AllCurrenciesListItem].Price =
          AllCurrenciesList[Item].Price;
      }
    }
    let DivPrice = CurrencyList.DivineOrb.Price;
    let AltPrice = CurrencyList.OrbofAlteration.Price;
    let UnmakingPrice;
    console.log("This is alt price: ", AltPrice);
    AltPrice = Math.ceil(1 / AltPrice);
    AltPrice = AltPrice * DivPrice;
    AltPrice = `1/${AltPrice}`;
    CurrencyList.OrbofAlteration.Price = AltPrice;
    UnmakingPrice = RoundUp(CurrencyList.OrbofUnmaking.Price, 1);
    UnmakingPrice = Math.floor(DivPrice / UnmakingPrice);
    UnmakingPrice = `1/${UnmakingPrice}`;
    CurrencyList.OrbofUnmaking.Price = UnmakingPrice;
    CurrencyList.ChaosOrb = {
      Base: 20,
      Quant: 10,
      MinQuant: 50,
      MaxQuant: 500,
      Name: "ChaosOrb",
      Price: `1/${CurrencyList.DivineOrb.Price}`,
    };
    for (const Item in CurrencyList) {
      con.query(
        `UPDATE currency 
        SET Base ="${CurrencyList[Item].Base}",
            CurrentQuant = 0, 
            MinQuant = "${CurrencyList[Item].MinQuant}",
            MaxQuant ="${CurrencyList[Item].MaxQuant}",
            Price ="${CurrencyList[Item].Price}"
        WHERE Name = "${CurrencyList[Item].Name}"`
      );
    }
  });
