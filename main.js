"use strict";
const path = require("path");
const { spawn } = require("child_process");
// const Locate = spawn("python3", [
//   "C:/Users/shacx/Documents/GitHub/Poe-trade/LocateStash.py",
// ]);
const PathOfExileLog = require("poe-log-monitor");
const { rejects } = require("assert");
const { resolve } = require("path");
const { type } = require("os");
let Queue = [];

let poeLog = new PathOfExileLog({
  logfile:
    "C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/client.txt",
  interval: 500,
});
//#region Declarations
let WhispName = "";
let kolko;
let Check = false;
let mes = [];
let namearray = [];
let OfferQ = [];
let RequestPoe = [];
let Offer = [];
let kolkoArr = [];
let ComparePrice;
let Remain;
let GreenInterval;
let OfferCurrencyType;
let OfferQuant;
let CurrencyMatch;
let ReqCurrencyType;
let PriceCheckCurrency = "Exalted Orb";
let PriceData;
let PriceDataArr = [];
let CurrencyList = {
  Exalt: { name: "Exalted Orb", base: 10, price: 30 },
  Divine: { name: "Divine Orb", base: 10, price: 275 },
  Annul: { name: "Orb of Annulment", base: 20, price: 8 },
  Alt: { name: "Orb of Alteration", base: 20, price: 0.083 },
  Regal: { name: "Regal Orb", base: 10, price: 1 },
  Scour: { name: "Orb of Scouring", base: 30, price: 1 },
  Unmaking: { name: "Orb of Unmaking", base: 40, price: 1 },
  AncientOrb: { name: "Ancient Orb", base: 20, price: 1 },
  VeiledChaos: { name: "Veiled Chaos Orb", base: 10, price: 1 },
  VaalOrb: { name: "Vaal Orb", base: 10, price: 1 },
  Chromatic: { name: "Chromatic Orb", base: 20, price: 1 },
  Sextant: { name: "Awakened Sextant", base: 10, price: 1 },
  Alch: { name: "Orb of Alchemy", base: 10, price: 1 },
  Fusing: { name: "Orb of Fusing", base: 20, price: 1 },
  Regret: { name: "Orb of Regret", base: 40, price: 1 },
};
function FilterMsg() {
  for (let i = 0; i < mes.length; i++) {
    let split = mes[i].split("your");
    namearray.push(split[1]);
  }
  for (let i = 0; i < namearray.length; i++) {
    let split2 = namearray[i].split("for my");
    RequestPoe.push(split2[0]);
    Offer.push(split2[1]);
  }
  console.log(RequestPoe);

  let ReqQuant = RequestPoe[0].match(/\d+/g);
  CurrencyMatch = RequestPoe[0].replace(/\d+/g, "").trim();
  ReqCurrencyType = RequestPoe[0].replace(/\d+/g, "").replace(/\s/g, "");

  for (let i = 0; i < Offer.length; i++) {
    let split3 = Offer[i].split("in");
    OfferQ.push(split3[0]);
  }

  OfferCurrencyType = OfferQ[0].replace(/\d+/g, "").replace(/\s/g, "");

  OfferQuant = OfferQ[0].match(/\d+/g);

  for (const keys in CurrencyList) {
    if (CurrencyList[keys]["name"] == CurrencyMatch) {
      ComparePrice = CurrencyList[keys]["price"];
    }
  }
  if (OfferQuant[0] / ReqQuant[0] >= ComparePrice - 2) {
    Check = true;
    const Invite = spawn("python", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Invite.py",
      WhispName,
    ]);
    Invite.stdout.on("data", (data) => {
      const FromStash = spawn("python3", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/FromStash.py",
        ReqQuant,
        ReqCurrencyType,
        OfferQuant,
        OfferCurrencyType,
        WhispName,
      ]);
      FromStash.stdout.on("data", (data) => {
        kolko = data.toString();
        kolkoArr.push(kolko);
      });
      FromStash.stderr.on("error", (error) => {
        console.log(`std: ${error}`);
      });
    });
  }
}

//#endregion
// console.log(CurrencyList.Alch["price"]);

poeLog.on("whisper", (whisper) => {
  kolkoArr.length = 0;
  mes.push(whisper.message);

  if (
    whisper.direction === "From" &&
    whisper.message.includes("like to buy") &&
    Queue.length == 0
  ) {
    Queue.push(whisper.player.name);

    WhispName = whisper.player.name;
    setTimeout(() => {
      FilterMsg();

      mes.length = 0;
      namearray.length = 0;
      OfferQ.length = 0;
      RequestPoe.length = 0;
      Offer.length = 0;
      Queue.length = 0;
    }, 1000);
  }
});

poeLog.on("areaJoin", (area) => {
  let PlayerName = area.player.name;
  let HowMuch;
  if (WhispName == PlayerName && Check == true) {
    HowMuch = kolkoArr[0].match(/\d+/g);
    for (let i = 0; i < kolkoArr.length; i++) {
      if (kolkoArr[i].includes("remain")) {
        Remain = "True";
      } else {
        Remain = "False";
      }
    }
  }
  let Green;

  if (WhispName == PlayerName) {
    setTimeout(() => {
      const TradeRequest = spawn("python3", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/TradeRequest.py",
        PlayerName,
      ]);
    }, 1500);
    const TradeReqId = spawn("python3", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/TradeReqIdentifier.py",
    ]);
    TradeReqId.stdout.on("data", (data) => {
      const FromInventory = spawn("python3", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/FromInventory.py",
        HowMuch,
        Remain,
      ]);
      FromInventory.stdout.on("data", (data) => {});
      FromInventory.stderr.on("error", (error) => {
        console.log(error);
      });
    });
    GreenInterval = setInterval(() => {
      Green = spawn("python3", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/GreenTrade.py",
      ]);
      Green.stdout.on("data", (data) => {
        if (data.toString().includes("44")) {
          clearInterval(GreenInterval);
          const Hover = spawn("python3", [
            "C:/Users/shacx/Documents/GitHub/Poe-trade/Hover.py",
            OfferQuant[0],
            OfferCurrencyType,
          ]);

          Hover.stdout.on("data", (data) => {
            const Compare = spawn("python3", [
              "C:/Users/shacx/Documents/GitHub/Poe-trade/Compare.py",
              OfferQuant[0],
              OfferCurrencyType,
            ]);
            Compare.stdout.on("data", (data) => {
              if (data.toString().includes("True")) {
                setTimeout(() => {
                  const AcceptOffer = spawn("python3", [
                    "C:/Users/shacx/Documents/GitHub/Poe-trade/AcceptOffer.py",
                  ]);
                }, 200);
              } else {
                const CancelOffer = spawn("python3", [
                  "C:/Users/shacx/Documents/GitHub/Poe-trade/CancelOffer.py",
                ]);
              }
            });
          });
        }
      });
    }, 1500);
  }
});

poeLog.on("trade", (trade) => {
  Check == false;
  if (trade.accepted == false) {
    clearInterval(GreenInterval);
  }
  if (trade.accepted == true) {
    const OpenStash = spawn("python3", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenStash.py",
    ]);
    const t4t = spawn("python3", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/t4t.py",
    ]);

    setTimeout(() => {
      const Dump = spawn("python3", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/AfterTradeFromInv.py",
        OfferQuant,
        OfferCurrencyType,
      ]);
    }, 1000);
  }
});
setInterval(() => {
  const GetPrices = spawn("python3", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/Pricing.py",
    `${PriceCheckCurrency}`,
  ]);
  GetPrices.stdout.on("data", (data) => {
    // PriceData = data.toString();
    PriceData = data.toString().replaceAll("'", '"');
    let Str = JSON.parse(PriceData);

    for (const keys in CurrencyList) {
      CurrencyList[keys]["price"] = Str[CurrencyList[keys]["name"]].toFixed(2);
    }
  });
}, 900000);

poeLog.on("whisper", (whisper) => {
  if (whisper.direction == "To" && whisper.message.includes("t4t")) {
    Queue.shift;
  }
});
