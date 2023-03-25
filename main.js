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
const { trace } = require("console");

let poeLog = new PathOfExileLog({
  logfile:
    "C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/client.txt",
  interval: 500,
});
//#region Declarations
let Pricestr;
let EssencePriceData;
let Queue = [];
let PlayerJoined = false;
let WhispName = "";
let kolko;
let HowMuch;
let PriceCheck = false;
let mes = [];
let namearray = [];
let OfferQ = [];
let CompareOffer;
let RequestPoe = [];
let Offer = [];
let kolkoArr = [];
let ComparePrice;
let Remain;
let GreenInterval;
let OfferCurrencyType;
let OfferQuant;
let CurrencyMatch = "";
let ReqCurrencyType;
let PriceData;
let CurrencyList = {
  Exalt: { name: "Exalted Orb", base: 10, price: 30 },
  Divine: { name: "Divine Orb", base: 10, price: 275 },
  // Annul: { name: "Orb of Annulment", base: 20, price: 8 },
  // Alt: { name: "Orb of Alteration", base: 20, price: 0.083 },
  Regal: { name: "Regal Orb", base: 10, price: 1 },
  Scour: { name: "Orb of Scouring", base: 30, price: 1 },
  Unmaking: { name: "Orb of Unmaking", base: 40, price: 1 },
  // AncientOrb: { name: "Ancient Orb", base: 20, price: 1 },
  VeiledChaos: { name: "Veiled Chaos Orb", base: 10, price: 1 },
  VaalOrb: { name: "Vaal Orb", base: 10, price: 1 },
  Chromatic: { name: "Chromatic Orb", base: 20, price: 1 },
  Sextant: { name: "Awakened Sextant", base: 10, price: 1 },
  Alch: { name: "Orb of Alchemy", base: 10, price: 1 },
  // Fusing: { name: "Orb of Fusing", base: 20, price: 1 },
  Regret: { name: "Orb of Regret", base: 40, price: 1 },
};
let EssenceList = {
  Greed: { name: "Deafening Essence of Greed", price: 1 },
  Contempt: { name: "Deafening Essence of Contempt", price: 1 },
  Hatred: { name: "Deafening Essence of Hatred", price: 1 },
  Woe: { name: "Deafening Essence of Woe", price: 1 },
  Fear: { name: "Deafening Essence of Fear", price: 1 },
  Anger: { name: "Deafening Essence of Anger", price: 1 },
  Torment: { name: "Deafening Essence of Torment", price: 1 },
  Sorrow: { name: "Deafening Essence of Sorrow", price: 1 },
  Rage: { name: "Deafening Essence of Rage", price: 1 },
  Suffering: { name: "Deafening Essence of Suffering", price: 1 },
  Wrath: { name: "Deafening Essence of Wrath", price: 1 },
  Doubt: { name: "Deafening Essence of Doubt", price: 1 },
  Loathing: { name: "Deafening Essence of Loathing", price: 1 },
  Zeal: { name: "Deafening Essence of Zeal", price: 1 },
  Anguish: { name: "Deafening Essence of Anguish", price: 1 },
  Spite: { name: "Deafening Essence of Spite", price: 1 },
  Scorn: { name: "Deafening Essence of Scorn", price: 1 },
  Envy: { name: "Deafening Essence of Envy", price: 1 },
  Misery: { name: "Deafening Essence of Misery", price: 1 },
  Dread: { name: "Deafening Essence of Dread", price: 1 },
  Insanity: { name: "Essence of Insanity", price: 1 },
  Horror: { name: "Essence of Horror", price: 1 },
  Delirium: { name: "Essence of Delirium", price: 1 },
  Hysteria: { name: "Essence of Hysteria", price: 1 },
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

  let ReqQuant = RequestPoe[0].match(/\d+/g);
  CurrencyMatch = RequestPoe[0].replace(/\d+/g, "").trim();
  ReqCurrencyType = RequestPoe[0].replace(/\d+/g, "").replace(/\s/g, "");
  for (let i = 0; i < Offer.length; i++) {
    let split3 = Offer[i].split("in");
    OfferQ.push(split3[0]);
  }

  OfferCurrencyType = OfferQ[0].replace(/\d+/g, "").replace(/\s/g, "");
  OfferQuant = OfferQ[0].match(/\d+/g);
  CompareOffer = OfferQuant[0];
  if (OfferCurrencyType.includes("Divine")) {
    CompareOffer = CompareOffer / CurrencyList.Divine.price;
  }

  if (OfferCurrencyType.trim() == "Div") {
    OfferCurrencyType = "Divine Orb";
    OfferQuant = [OfferQuant[0] * CurrencyList.Divine["price"]];
  }
  if (ReqCurrencyType.includes("Orb") || ReqCurrencyType.includes("Sextant")) {
    for (const keys in CurrencyList) {
      if (CurrencyList[keys]["name"] == CurrencyMatch) {
        ComparePrice = CurrencyList[keys]["price"];
      } else if (CurrencyMatch.includes("Chaos")) {
        ComparePrice = 1;
      }
    }
  } else if (CurrencyMatch.includes("Essence")) {
    for (const keys in EssenceList) {
      if (EssenceList[keys]["name"] == CurrencyMatch) {
        ComparePrice = EssenceList[keys]["price"];
      }
    }
  }
  if (OfferQuant[0] / ReqQuant[0] >= ComparePrice - 2) {
    PriceCheck = true;
    const Invite = spawn("python", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Invite.py",
      WhispName,
    ]);
    Invite.stdout.on("data", (data) => {
      if (
        //if currency
        ReqCurrencyType.includes("Orb") ||
        ReqCurrencyType.includes("Sex")
      ) {
        const OpenCurrencyTab = spawn("python3", [
          "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenCurrencyTab.py",
        ]);
        const GetCurrency = spawn("python3", [
          "C:/Users/shacx/Documents/GitHub/Poe-trade/GetCurrency.py",
          ReqQuant,
          ReqCurrencyType,
        ]);
        GetCurrency.stdout.on("data", (data) => {
          kolko = data.toString();
          kolkoArr.push(kolko);
        });
        GetCurrency.stderr.on("error", (error) => {
          console.log(`std: ${error}`);
        });
      } //end if currency
      else if (ReqCurrencyType.includes("Essence")) {
        const OpenEssenceTab = spawn("python3", [
          "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenEssenceTab.py",
        ]);
        const LoadEssence = spawn("python3", [
          "C:/Users/shacx/Documents/GitHub/Poe-trade/GetEssence.py",
          ReqQuant,
          ReqCurrencyType,
        ]);
        LoadEssence.stdout.on("data", (data) => {
          kolko = data.toString();
          kolkoArr.push(kolko);
          HowMuch = kolkoArr[0].match(/\d+/g);
          for (let i = 0; i < kolkoArr.length; i++) {
            if (kolkoArr[i].includes("remain")) {
              Remain = "True";
            } else {
              Remain = "False";
            }
          }
        });
      }
    });
  }
}

//#endregion

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
      if (PlayerJoined == false) {
        Queue.length = 0;
        const FromInventory = spawn("python3", [
          "C:/Users/shacx/Documents/GitHub/Poe-trade/FromInventory.py",
          HowMuch,
          Remain,
        ]);
      }
    }, 15000);
    setTimeout(() => {
      FilterMsg();

      mes.length = 0;
      namearray.length = 0;
      OfferQ.length = 0;
      RequestPoe.length = 0;
      Offer.length = 0;
    }, 1000);
  }
});

poeLog.on("areaJoin", (area) => {
  let PlayerName = area.player.name;

  if (WhispName == PlayerName && PriceCheck == true) {
    PlayerJoined = true;
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
            CompareOffer,
            OfferCurrencyType.replace(/\s/g, ""),
          ]);

          Hover.stdout.on("data", (data) => {
            const Compare = spawn("python3", [
              "C:/Users/shacx/Documents/GitHub/Poe-trade/Compare.py",
              CompareOffer,
              OfferCurrencyType.replace(/\s/g, ""),
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
                const Kick = spawn("python3", [
                  "C:/Users/shacx/Documents/GitHub/Poe-trade/Kick.py",
                  WhispName,
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
  PriceCheck == false;
  PlayerJoined = false;
  Queue.length = 0;
  if (trade.accepted == false) {
    clearInterval(GreenInterval);
    const Kick = spawn("python3", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Kick.py",
      WhispName,
    ]);
  }
  if (trade.accepted == true) {
    const OpenStash = spawn("python3", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenStash.py",
    ]);
    setTimeout(() => {
      const Dump = spawn("python3", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/AfterTradeFromInv.py",
        OfferQuant,
        OfferCurrencyType,
      ]);
    }, 2000);
    setTimeout(() => {
      const Kick = spawn("python3", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/Kick.py",
        WhispName,
      ]);
      Kick.stdout.on("data", (data) => {
        console.log(data.toString());
      });
    }, 5500);
  }
});

function GetCurrencyPrice() {
  const OpenCurrencyTab2 = spawn("python3", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenCurrencyTab.py",
  ]);
  OpenCurrencyTab2.stdout.on("data", (data) => {
    console.log("Currency running");
    // console.log(data.toString());
    const GetPrices = spawn("python3", [
      "-u",
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Pricing.py",
      "Currency",
    ]);
    const UpdateCurrencyPrice = spawn("python3", [
      "-u",
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Currency.py",
    ]);

    GetPrices.stdout.on("data", (data) => {
      PriceData = data.toString().replaceAll("'", '"');
      let Str = JSON.parse(PriceData);

      for (const keys in CurrencyList) {
        CurrencyList[keys]["price"] = Str[CurrencyList[keys]["name"]];
      }
      const SetCurrencyPrices = spawn("python3", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/SetCurrencyPrice.py",
        CurrencyList.Divine.price,
      ]);
      SetCurrencyPrices.stdout.on("data", (data) => {
        // console.log(data.toString());
        Queue.length = 0;
      });
    });
  });
}
function GetEssence() {
  Queue.push("awd");
  console.log("Essence running");
  const OpenEssenceTab = spawn("python3", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenEssenceTab.py",
  ]);
  const UpdateEssencePrice = spawn("python3", [
    "-u",
    "C:/Users/shacx/Documents/GitHub/Poe-trade/Pricing.py",
    "Essence",
  ]);

  UpdateEssencePrice.stdout.on("data", (data) => {
    EssencePriceData = data.toString().replaceAll("'", '"');
    let EssenceStr = JSON.parse(EssencePriceData);
    let Pricestr = "";

    for (const keys in EssenceList) {
      if (EssenceList[keys]["price"] == EssenceStr[EssenceList[keys]["name"]]) {
        Pricestr = Pricestr + "0 ";
      } else {
        Pricestr = Pricestr + "1 ";
      }

      EssenceList[keys]["price"] = EssenceStr[EssenceList[keys]["name"]];
      // Pricestr = Pricestr + ` ${EssenceList[keys]["price"]}`;
    }
    console.log(Pricestr);
    const SetEssencePrice = spawn("python3", [
      "-u",
      "C:/Users/shacx/Documents/GitHub/Poe-trade/SetEssencePrice.py",
      Pricestr,
    ]);
    // SetEssencePrice.stderr.on("error", (error) => {
    //   console.log(error);
    // });
    SetEssencePrice.stdout.on("data", (data) => {
      console.log(data.toString());
      if (data.toString().includes("start")) {
        Queue.push("awd");
      }
      if (data.toString().includes("finish")) {
        GetCurrencyPrice();
      }
    });
  });
}

GetEssence();

setInterval(() => {
  GetEssence();
}, 720000);
