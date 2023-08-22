const fs = require("fs");
const CurrencyList = require("C:/Users/shacx/Documents/GitHub/Poe-trade/JSDB/DB");
ClassList = {};
fetch(
  "https://poe.ninja/api/data/currencyoverview?league=Ancestor&type=Currency"
)
  .then((response) => response.json())
  .then((data) => {
    const FilteredData = data.lines.filter((line) =>
      line.hasOwnProperty("currencyTypeName")
    );

    for (const Item in CurrencyList) {
      console.log(Item);
    }
    FilteredData.forEach((line) => {
      NewName = line.currencyTypeName.replaceAll(" ", "").replaceAll("'", "");
      NewPrice = line.receive.value;

      ClassList[NewName] = {
        Price: NewPrice,
      };
    });
    fs.appendFile(
      "C:/Users/shacx/Documents/GitHub/Poe-trade/JSDB/WriteHere",
      JSON.stringify(ClassList),
      (err) => {
        if (err) {
          console.error("Error writing to file:", err);
          return;
        }
        console.log("Data has been written to the file");
      }
    );
  });
