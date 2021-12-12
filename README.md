# Fangamer Restock Scraper

Simple scraper, that sends a notif on the server after specific item goes available on Fangamer.

## Configuration

To get a config file you need to start a scraper first, it will create a default config, after that stop it and edit the config to your likeness.

```yml
Collection:                                                # For this part you'll need to get the parts of product URL in the order.
  Game: va-11-hall-a                                       # For example: https://www.fangamer.com/collections/va-11-hall-a/products/valhalla-dog-plush
  Product: va-11-hall-a-complete-sound-collection-box-set  # For example: https://www.fangamer.com/collections/{GAME}/products/{PRODUCT}
Misc:                                                      #
  CheckOnTimer: 120                                        # How long it'll sleep after getting the availability.
  ConfigVer: 1                                             # Do not edit.
  Motd: true                                               # Dumb Motd
Notification:                                              #
  CustomRequest: ''                                        # If you host own webhook
  DiscordWebhook: ''                                       # Discord's webhook, that you can get in settings of a channel

```

## Installation

```console

jill@bar:~$ git clone https://github.com/LMNYX/fangamer-restock.git
jill@bar:~$ pip install -r requirements.txt
jill@bar:~$ python3 restock.py

```

## Warning

This project was made basically just to get Vallhalla's vinyl set, so I do not guarantee that it will work in the future and that it won't get you blocked off Fangamer's webiste.
I also had [Jill Plush scraper Discord bot](https://github.com/LMNYX/jillplush) (it's not user-friendly).
