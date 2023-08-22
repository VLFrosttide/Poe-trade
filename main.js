"use strict";
const path = require("path");
const { spawn } = require("child_process");
const PathOfExileLog = require("poe-log-monitor");
const { rejects } = require("assert");
const { resolve } = require("path");
const { type } = require("os");
const { trace, error } = require("console");
const { Invite } = require("discord.js");
const CurrencyList = require("C:/Users/shacx/Documents/GitHub/Poe-trade/JSDB/DB");

// console.log(CurrencyList.ChaosOrb);

let poeLog = new PathOfExileLog({
  logfile: "D:/logs/client.txt",
  interval: 500,
});
//#region Variable Declarations

let Pricestr;
let CurrencyPriceStr = "";
let EssencePriceData;
let ReqQuant;
let Queue = [];
let PlayerJoined = false;
let WhispName = "";
let kolko;
let NumberOfClicks;
let PriceCheck = false;
let mes = [];
let namearray = [];
let OfferQ = [];
let CompareOfferQuant;
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
//#endregion
//#region Child Process Declarations
function FromInventory(Quant, Type) {
  const FromInv = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/FromInventory.py",
    Quant,
    Type,
  ]);
  const FromInventoryOnStdout = (callback) =>
    FromInv.stdout.on("data", callback);
  const FromInventoryOnStderr = (callback) =>
    FromInv.stderr.on("data", callback);
  const FromInventoryOnClose = (callback) => FromInv.on("close", callback);

  return {
    FromInv,
    FromInventoryOnStdout,
    FromInventoryOnStderr,
    FromInventoryOnClose,
  };
}
function TradeInvite(Name) {
  const Invite = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/TradeRequest.py",
    Name,
  ]);
  const InviteOnStdOut = (callback) => {
    Invite.stdout.on("data", callback);
  };
  return { Invite, InviteOnStdOut };
}

function TradeIdentification() {
  const TradeId = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/TradeIdentifier.py",
  ]);
  const TradeIdOnStdOut = (callback) => {
    TradeId.stdout.on("data", callback);
  };
  return { TradeId, TradeIdOnStdOut };
}
function CompareCurrency(Quant, Type) {
  const Compare = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/Compare.py",
    Quant,
    Type.replace(/\s/g, ""),
  ]);
  const CompareStdout = (callback) => Compare.stdout.on("data", callback);
  const CompareStderr = (callback) => Compare.stderr.on("err", callback);
  return { Compare, CompareStdout, CompareStderr };
}
//#endregion
//#region Lists
// let CurrencyList = {
//   Exalt: { name: "Exalted Orb", base: 10, price: 30 },
//   Divine: { name: "Divine Orb", base: 10, price: 275 },
//   Annul: { name: "Orb of Annulment", base: 20, price: 8 },
//   Alt: { name: "Orb of Alteration", base: 20, price: 0.083 },
//   Regal: { name: "Regal Orb", base: 10, price: 1 },
//   Scour: { name: "Orb of Scouring", base: 30, price: 1 },
//   Unmaking: { name: "Orb of Unmaking", base: 40, price: 1 },
//   AncientOrb: { name: "Ancient Orb", base: 20, price: 1 },
//   VeiledChaos: { name: "Veiled Chaos Orb", base: 10, price: 1 },
//   VaalOrb: { name: "Vaal Orb", base: 10, price: 1 },
//   Chromatic: { name: "Chromatic Orb", base: 20, price: 1 },
//   Sextant: { name: "Awakened Sextant", base: 10, price: 1 },
//   Alch: { name: "Orb of Alchemy", base: 10, price: 1 },
//   Fusing: { name: "Orb of Fusing", base: 20, price: 1 },
//   Regret: { name: "Orb of Regret", base: 40, price: 1 },
// };

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
let LifeforceList = {
  Wild: { name: "Wild Crystallised Lifeforce", price: 1 / 65 },
  Vivid: { name: "Vivid Crystallised Lifeforce", price: 1 / 65 },
  Primal: { name: "Primal Crystallised Lifeforce", price: 1 / 65 },
};
//#endregion
function FilterMsg() {
  for (let i = 0; i < mes.length; i++) {
    let split = mes[i].split("your");
    namearray.push(split[1]);
  }
  // console.log(namearray);
  for (let i = 0; i < namearray.length; i++) {
    let split2 = namearray[i].split("for my");
    RequestPoe.push(split2[0]);
    Offer.push(split2[1]);
  }

  ReqQuant = RequestPoe[0].match(/\d+/g);
  CurrencyMatch = RequestPoe[0].replace(/\d+/g, "").trim();
  ReqCurrencyType = RequestPoe[0].replace(/\d+/g, "").replace(/\s/g, "");
  for (let i = 0; i < Offer.length; i++) {
    let split3 = Offer[i].split("in");
    OfferQ.push(split3[0]);
  }

  OfferCurrencyType = OfferQ[0].replace(/\d+/g, "").replace(/\s/g, "");
  OfferQuant = OfferQ[0].match(/\d+/g);
  CompareOfferQuant = OfferQuant[0];
  if (OfferCurrencyType.includes("Divine")) {
    CompareOfferQuant = CompareOfferQuant / CurrencyList.Divine.price;
  }

  if (OfferCurrencyType.trim() == "Div") {
    OfferCurrencyType = "Divine Orb";
    OfferQuant = [OfferQuant[0] * CurrencyList.Divine.price];
  }
  if (ReqCurrencyType.includes("Orb") || ReqCurrencyType.includes("Sextant")) {
    for (const keys in CurrencyList) {
      if (CurrencyList[keys]["Name"] == CurrencyMatch) {
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
  } else if (CurrencyMatch.includes("Lifeforce")) {
    for (const keys in LifeforceList) {
      if (LifeforceList[keys]["name"] == CurrencyMatch) {
        ComparePrice = LifeforceList[keys]["price"];
      }
    }
  }
  // if (OfferQuant[0] / ReqQuant[0] >= ComparePrice - 1) {
  // if (true) {
  // }
  PriceCheck = true;
  const Invite = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/Invite.py",
    WhispName,
  ]);
  Invite.stdout.on("data", (data) => {
    //#region Currency
    if (ReqCurrencyType.includes("Orb") || ReqCurrencyType.includes("Sex")) {
      console.log("currency");
      const OpenCurrencyTab = spawn("python", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenCurrencyTab.py",
      ]);
      const GetCurrency = spawn("python", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/GetCurrency.py",
        ReqQuant,
        ReqCurrencyType,
      ]);
      GetCurrency.stdout.on("data", (data) => {
        console.log(data.toString());
        // kolko = RequestCurrencyQuant/RequestTypeCurrency.base
        kolko = data.toString();
        kolkoArr.push(kolko);
        NumberOfClicks = kolkoArr[0].match(/\d+/g);
        console.log("This is NumberOfClicks: ", NumberOfClicks);
        console.log("This is kolko: ", kolko);
        console.log("This is KolkoArr: ", kolkoArr);
        for (let i = 0; i < kolkoArr.length; i++) {
          if (kolkoArr[i].includes("remain")) {
            Remain = "True";
          } else {
            Remain = "False";
          }
        }
      });
      GetCurrency.stderr.on("error", (error) => {
        console.log(`std: ${error}`);
      });
    }
    //#endregion
    //#region Essence
    else if (ReqCurrencyType.includes("Essence")) {
      console.log("essence");
      Queue.length == 0;
      console.log("Queue length:", Queue.length);

      const OpenEssenceTab = spawn("python", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenEssenceTab.py",
      ]);
      const LoadEssence = spawn("python", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/GetEssence.py",
        ReqQuant,
        ReqCurrencyType,
      ]);
      LoadEssence.stdout.on("data", (data) => {
        kolko = data.toString();
        kolkoArr.push(kolko);
        NumberOfClicks = kolkoArr[0].match(/\d+/g);
        for (let i = 0; i < kolkoArr.length; i++) {
          if (kolkoArr[i].includes("remain")) {
            Remain = "True";
          } else {
            Remain = "False";
          }
        }
      });
    }
    //#endregion
    //#region Lifeforce
    else if (ReqCurrencyType.includes("Lifeforce")) {
      const OpenLifeforceTab = spawn("python", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenLifeforceTab.py",
      ]);
      OpenLifeforceTab.stdout.on("data", (data) => {
        console.log(data.toString());
        console.log("Currency type: ", ReqCurrencyType);
        const GetLifeforce = spawn("python", [
          "C:/Users/shacx/Documents/GitHub/Poe-trade/GetLifeforce.py",
          ReqQuant,
          ReqCurrencyType,
        ]);

        GetLifeforce.stdout.on("data", (data) => {
          console.log(data.toString());
          Remain = true;
          NumberOfClicks = 0;
        });
      });
      Queue.length == 0;
      console.log("Queue length:", Queue.length);
    }
    //#endregion
  });
}

poeLog.on("whisper", (whisper) => {
  // console.log(whisper.message, Offer);
  kolkoArr.length = 0;
  if (whisper.message.includes("like to buy")) {
    mes.push(whisper.message);
  }
  console.log("Queue length:", Queue.length);
  if (
    whisper.direction === "From" &&
    whisper.message.includes("like to buy") &&
    Queue.length === 0
  ) {
    Queue.push("awd");
    console.log("QueueLenght:", Queue.length);

    WhispName = whisper.player.name;

    //#region Return items to inventory if player doesnt join
    setTimeout(() => {
      if (PlayerJoined == false) {
        Queue.length = 0;
        FromInventory(ReqQuant, ReqCurrencyType);
      }
    }, 45000);
    //#endregion
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
  if (WhispName == PlayerName && PlayerJoined == true) {
    //Send a trade request
    setTimeout(() => {
      TradeInvite(PlayerName);
    }, 1500);
    // Identify if the trade window is opened
    const TradeIder = TradeIdentification(PlayerName);

    TradeIder.TradeIdOnStdOut((data) => {
      console.log("Trade identifier: ", data.toString());
      if (data.toString().trim() == "Found") {
        const InvProcess = FromInventory(ReqQuant, ReqCurrencyType);
        InvProcess.FromInventoryOnStdout((data) => {
          const CompareFinish = CompareCurrency(
            CompareOfferQuant,
            OfferCurrencyType
          );
          console.log(data.toString());
          console.log("This is CompareOfferQuant: ", CompareOfferQuant);
          console.log("This is OfferCurrencyType: ", OfferCurrencyType);
          CompareFinish.CompareStdout((data) => {
            console.log("From Compare: ", data.toString());
            if (data.toString().includes("True")) {
              setTimeout(() => {
                const AcceptOffer = spawn("python", [
                  "C:/Users/shacx/Documents/GitHub/Poe-trade/AcceptOffer.py",
                ]);
              }, 200);

              // Otherwise cancel the offer
            } else {
              const CancelOffer = spawn("python", [
                "C:/Users/shacx/Documents/GitHub/Poe-trade/CancelOffer.py",
              ]);
            }
          });
          CompareFinish.CompareStderr((err) => {
            console.log("Compare Error: ", err.toString());
          });
        });
        InvProcess.FromInventoryOnStderr((err) => {
          console.log("FromInventory error: ", err.toString());
        });
      }
    });

    // TradeIdentification.InviteOnStdOut((data) => {

    //   Tradeid.TradeIdOnStdOut((data) => {-p

    //     }
    //   });
    // });

    //If its opened , send items from inventory to the trade window.
    // TradeId.stdout.on("data", (data) => {});
    //#region Useless code
    // const Compare = spawn("python", [
    //   "C:/Users/shacx/Documents/GitHub/Poe-trade/Compare.py",
    //   CompareOfferQuant,
    //   OfferCurrencyType.replace(/\s/g, ""),
    // ]);

    // If comparison is true , accept the offer
    ////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Compare.stdout.on("data", (data) => {
    //   console.log("Compare data:" + data.toString());
    //   if (data.toString().includes("True")) {
    //     setTimeout(() => {
    //       const AcceptOffer = spawn("python", [
    //         "C:/Users/shacx/Documents/GitHub/Poe-trade/AcceptOffer.py",
    //       ]);
    //     }, 200);

    //     // Otherwise cancel the offer
    //   } else {
    //     const CancelOffer = spawn("python", [
    //       "C:/Users/shacx/Documents/GitHub/Poe-trade/CancelOffer.py",
    //     ]);
    //   }
    // });
    //#endregion
  }
});

poeLog.on("trade", (trade) => {
  PriceCheck == false;
  PlayerJoined = false;
  if (trade.accepted == false) {
    const Kick = spawn("python", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Kick.py",
    ]);
    Queue.length = 0;
    console.log("Queue length:", Queue.length);
  }
  if (trade.accepted == true) {
    const OpenStash = spawn("python", [
      "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenStash.py",
    ]);
    setTimeout(() => {
      const Dump = spawn("python", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/FromInventory.py",
        OfferQuant,
        OfferCurrencyType,
      ]);
    }, 3000);
    setTimeout(() => {
      const Kick = spawn("python", [
        "C:/Users/shacx/Documents/GitHub/Poe-trade/Kick.py",
        WhispName,
      ]);

      Queue.length = 0;
      console.log("Queue length:", Queue.length);
    }, 6500);
  }
});

//#region  Price Updates
function GetCurrencyPrice() {
  const OpenCurrencyTab2 = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenCurrencyTab.py",
  ]);

  OpenCurrencyTab2.stdout.on("data", (data) => {
    console.log("Currency running", data.toString());
    const GetPrices = spawn("python", [
      "-u",
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Pricing.py",
      "Currency",
    ]);

    GetPrices.stdout.on("data", (data) => {
      PriceData = data.toString().replaceAll("'", '"');
      let Str = JSON.parse(PriceData);
      console.log("this is str ", JSON.parse(PriceData));
      for (const keys in CurrencyList) {
        console.log("this is KeysName", Str[CurrencyList[keys]["Name"]]);
        // console.log("this is keys price");
        if (CurrencyList[keys]["Price"] == Str[CurrencyList[keys]["Name"]]) {
          CurrencyPriceStr = CurrencyPriceStr + "0 ";
        } else {
          CurrencyPriceStr = CurrencyPriceStr + "1 ";
        }
        CurrencyList[keys]["Price"] = Str[CurrencyList[keys]["name"]];
      }

      try {
        console.log("Divine Price = " + CurrencyList.DivineOrb.Price);
        const SetCurrencyPrices = spawn("python", [
          "C:/Users/shacx/Documents/GitHub/Poe-trade/SetCurrencyPrice.py",
          CurrencyList.DivineOrb.Price,
          CurrencyPriceStr,
        ]);

        SetCurrencyPrices.stdout.on("data", (data) => {
          console.log(data.toString());
          Queue.length = 0;
          console.log(Queue.length);
        });
        SetCurrencyPrices.on("error", (err) => {
          console.log("l1: " + err);
        });
      } catch (err) {
        console.log("exception: " + err);
      }
    });
  });
}
function GetEssence() {
  Queue.push("awd");
  console.log("Essence running");
  const OpenEssenceTab = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-trade/OpenEssenceTab.py",
  ]);
  OpenEssenceTab.stdout.on("data", (data) => {
    const UpdateEssencePrice = spawn("python", [
      "-u",
      "C:/Users/shacx/Documents/GitHub/Poe-trade/Pricing.py",
      "Essence",
    ]);

    UpdateEssencePrice.stdout.on("data", (data) => {
      EssencePriceData = data.toString().replaceAll("'", '"');
      let EssenceStr = JSON.parse(EssencePriceData);
      Pricestr = "";

      for (const keys in EssenceList) {
        if (
          EssenceList[keys]["price"] ==
          Math.ceil(EssenceStr[EssenceList[keys]["name"]] + 1)
        ) {
          Pricestr = Pricestr + "0 ";
        } else {
          Pricestr = Pricestr + "1 ";
        }

        // console.log(
        //   EssenceList[keys]["name"],
        //   EssenceStr[EssenceList[keys]["name"]],
        //   Math.ceil(EssenceStr[EssenceList[keys]["name"]] + 1)
        // );
        EssenceList[keys]["price"] = Math.ceil(
          EssenceStr[EssenceList[keys]["name"]] + 1
        );
      }
      const SetEssencePrice = spawn("python", [
        "-u",
        "C:/Users/shacx/Documents/GitHub/Poe-trade/SetEssencePrice.py",
        Pricestr,
      ]);
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
  });
}
setTimeout(() => {
  GetEssence();
}, 2000);

// setInterval(() => {
//   GetEssence();
// }, 600000);

//#endregion
