const fs = require("fs");
const CurrencyList = require("./DB"); // Use relative path
const Fraction = require("fraction.js");

function RoundUp(number, decimalPlaces) {
  const multiplier = Math.pow(10, decimalPlaces);
  return Math.ceil(number * multiplier) / multiplier;
}

ClassList = {};
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

      ClassList[NewName] = {
        Price: NewPrice,
        Name: NewName,
      };
    });
    for (const Item in ClassList) {
      let ClassListItem = ClassList[Item].Name;

      if (CurrencyList.hasOwnProperty(ClassListItem)) {
        console.log(
          ClassList[Item].Name + " New Price " + ClassList[Item].Price
        );
        console.log(
          CurrencyList[ClassListItem].Name +
            " Old Price " +
            CurrencyList[ClassListItem].Price
        );

        CurrencyList[ClassListItem].Price = ClassList[Item].Price;
      }
    }
    let DivPrice = CurrencyList.DivineOrb.Price;
    let ChaosPrice = `1/${DivPrice}`;
    CurrencyList.ChaosOrb.Price = ChaosPrice;
    let AltPrice = CurrencyList.OrbofAlteration.Price;
    AltPrice = Math.ceil(1 / AltPrice);
    AltPrice = AltPrice * DivPrice;
    AltPrice = `1/${AltPrice}`;
    CurrencyList.OrbofAlteration.Price = AltPrice;
    UnmakingPrice = RoundUp(CurrencyList.OrbofUnmaking.Price, 1);
    UnmakingPrice = Math.floor(DivPrice / UnmakingPrice);
    UnmakingPrice = `1/${UnmakingPrice}`;
    CurrencyList.OrbofUnmaking.Price = UnmakingPrice;

    console.log(CurrencyList.OrbofUnmaking.Price);
  });
