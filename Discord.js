const { Client, GatewayIntentBits } = require("discord.js");

require("dotenv").config();
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.DirectMessages,
  ],
});

client.on("ready", () => {
  console.log("Bot is ready.");
  client.users.fetch("390137087363514373").then((user) => {
    user.send("a new message");
  });
});

client.login(process.env.TOKEN);
