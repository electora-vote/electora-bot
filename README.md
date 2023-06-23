# electora-bot

## Running the Bot

### Prerequisites

* Install the Docker Engine and Docker Compose:

  https://docs.docker.com/engine/install/

* Create a Discord Application and Bot and invite it into a server. Step 1 of:

  https://discord.com/developers/docs/getting-started

  This bot does not require any privileged intents.

### Setup

* Copy env.example to .env and enter your bot's token and discord server id.

* Run `docker compose up --detach`

  You should see your bot appear online in your discord server

* In discord, type `/` to see the bot's available commands listed.
