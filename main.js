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
let acorn = require("acorn");
let Queue = [];

let poeLog = new PathOfExileLog({
  logfile:
    "C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/client.txt",
  interval: 500,
});
//#region Declarations
let WhispName = "";
let kolko;
let kolkoArr = [];
let Remain;
let GreenInterval;
let OfferCurrencyType;
let OfferQuant;
let ReqCurrencyType;
let PriceCheckCurrency = "Exalted Orb";
let PriceData;
let PriceDataArr = [];
let CurrencyList = {
  Exalt: { name: "Exalted Orb", base: 10, price: 30 },
  Divine_Orb: { name: "Divine Orb", base: 10, price: 275 },
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
// console.log(CurrencyList.Alch);

//#endregion

poeLog.on("whisper", (whisper) => {
  if (
    whisper.direction === "From" &&
    whisper.message.includes("like to buy") &&
    Queue.length == 0
  ) {
    let mes = [];
    let namearray = [];
    let OfferQ = [];
    let RequestPoe = [];
    let Offer = [];
    kolkoArr = [];
    Queue.push(whisper.player.name);

    WhispName = whisper.player.name;
    const Invite = spawn("python", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Invite.py",
      WhispName,
    ]);
    //#region SplitMsg
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
      let ReqQuant = RequestPoe[0].match(/\d+/g);
      ReqCurrencyType = RequestPoe[0].replace(/\d+/g, "").replace(/\s/g, "");
      for (let i = 0; i < Offer.length; i++) {
        let split3 = Offer[i].split("in");
        OfferQ.push(split3[0]);
      }

      OfferCurrencyType = OfferQ[0].replace(/\d+/g, "").replace(/\s/g, "");

      OfferQuant = OfferQ[0].match(/\d+/g);
      console.log(OfferQuant / ReqQuant);
      console.log(CurrencyList[ReqCurrencyType]["price"] - 2);
      if (OfferQuant / ReqQuant >= CurrencyList[ReqCurrencyType]["price"] - 2) {
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

        //#endregion
      }
      setTimeout(() => {
        mes.push(whisper.message);
        FilterMsg();
        mes = [];
        namearray = [];
        OfferQ = [];
        RequestPoe = [];
        Offer = [];
      }, 2000);
    }
  }
});

poeLog.on("areaJoin", (area) => {
  let PlayerName = area.player.name;
  let HowMuch;
  if (WhispName == PlayerName) {
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
          console.log(OfferQuant[0], OfferCurrencyType);
          const Hover = spawn("python3", [
            "C:/Users/shacx/Documents/GitHub/Poe-trade/Hover.py",
            OfferQuant[0],
            OfferCurrencyType,
          ]);

          Hover.stdout.on("data", (data) => {
            console.log(data.toString());
            const Compare = spawn("python3", [
              "C:/Users/shacx/Documents/GitHub/Poe-trade/Compare.py",
              OfferQuant[0],
              OfferCurrencyType,
            ]);
            compare.stdout.on("data", (data) => {
              if (data.toString().includes("True")) {
                setTimeout(() => {
                  const AcceptOffer = spawn("python3", [
                    "C:/Users/shacx/Documents/GitHub/Poe-trade/AcceptOffer.py",
                  ]);
                }, 200);
              }
            });
          });
        }
      });
    }, 1500);
  }
});

poeLog.on("trade", (trade) => {
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
    console.log(CurrencyList);
  });
}, 900000);

poeLog.on("whisper", (whisper) => {
  if (whisper.direction == "To" && whisper.message.includes("t4t")) {
    Queue.shift;
  }
});
