"use strict";
const path = require("path");
const { spawn } = require("child_process");
const PathOfExileLog = require("poe-log-monitor");
let poeLog = new PathOfExileLog({
  logfile:
    "C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/client.txt",
  interval: 500,
});

poeLog.on("whisper", (whisper) => {
  if (whisper.direction === "From") {
    let mes = [];
    let namearray = [];
    let OfferQ = [];
    let RequestPoe = [];
    let Offer = [];
    let WhispName = whisper.player.name;

    const Invite = spawn("python", [
      "C:/Users/shacx/Documents/GitHub/Poe-Trade-Bot/Invite.py",
      WhispName,
    ]);
    //#region SplitMsg
    function FilterMsg() {
      for (let i = 0; i < mes.length; i++) {
        let split = mes[i].split("your");
        namearray.push(split[1]);
      }
      console.log(namearray);
      for (let i = 0; i < namearray.length; i++) {
        let split2 = namearray[i].split("for my");
        RequestPoe.push(split2[0]);
        Offer.push(split2[1]);
      }
      let ReqQuant = RequestPoe[0].match(/\d+/g);
      let ReqCurrencyType = RequestPoe[0]
        .replace(/\d+/g, "")
        .replace(/\s/g, "");
      console.log(ReqCurrencyType);
      for (let i = 0; i < Offer.length; i++) {
        let split3 = Offer[i].split("in");
        OfferQ.push(split3[0]);
      }

      let OfferCurrencyType = OfferQ[0].replace(/\d+/g, "").replace(/\s/g, "");

      let OfferQuant = OfferQ[0].match(/\d+/g);
      const FromStash = spawn("python", [
        "C:/Users/shacx/Documents/GitHub/Poe-Trade-Bot/FromStash.py",
        ReqQuant,
        ReqCurrencyType,
        OfferQuant,
        OfferCurrencyType,
        WhispName,
      ]);
      FromStash.stdout.on("data", (data) => {
        console.log(`stdout: ${data}`);
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
    }, 1000);
  }
});
poeLog.on("areaJoin", (area) => {
  let PlayerName = area.player.name;
  const TradeRequest = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-Trade-Bot/TradeRequest.py",
    PlayerName,
  ]);
  const TradeReqId = spawn("python", [
    "C:/Users/shacx/Documents/GitHub/Poe-Trade-Bot/TradeRequestIdentifier.py",
  ]);
  console.log(TradeReqId.pid);
  TradeReqId.stdout.on("data", (data) => {
    console.log(data);
  });
  TradeReqId.stderr.on("error", (error) => {
    console.log(error);
  });
});
