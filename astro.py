#!/usr/bin/env python3

import os
import datetime
import asyncio
from clypi import spinner
from simple_term_menu import TerminalMenu

# Variables for later

time = datetime.datetime.now()

def logo():
    print(r"""
            ,MMM8&&&.
        _...MMMMM88&&&&..._
     .::'''MMMMM88&&&&&&'''::.
    ::     MMMMM88&&&&&&     ::
    '::....MMMMM88&&&&&&....::'
       `''''MMMMM88&&&&''''`
       jgs   'MMM8&&&'
    """)
    print ("Astro - Astrophotography Helper")
    print (time)
    print ("")

def main():
    while True:
        options = ["Planning", "WebSites", "Applications", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        choice = options[menu_entry_index]
        print(f"[ DEBUG ] You have selected {choice}!")

        if choice == "Planning":
            planning()
        elif choice == "WebSites":
            websites()
        elif choice == "Applications":
            applications()
        elif choice == "Exit":
            break


def planning():
    while True:
        options = ["Open Stellarium", "Open LightPollutionmap", "TimeAndDate Astronomy", "Back"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        choice = options[menu_entry_index]
        print(f"[ DEBUG ] You have selected {choice}!")

        if choice == "Open Stellarium":
            @spinner("Opening Stellarium", capture=True)
            async def do_some_work():
                await asyncio.sleep(2)
                os.system("stellarium")
            asyncio.run(do_some_work())

            logo()
        if choice == "Open LightPollutionmap":
            print ("Opening LightPollutionmap")
            os.system("firefox https://www.lightpollutionmap.info/")
            logo ()

        if choice == "TimeAndDate Astronomy":
            print ("Opening TaDA")
            os.system("firefox https://www.timeanddate.com/astronomy")

        elif choice == "Back":
            break


def websites():
    print("websites")


def applications():
    print("applications")


if __name__ == "__main__":
    logo()
    main()

#@spinner("Doing work", capture=True)
#async def do_some_work():
#    await asyncio.sleep(2)
#
#asyncio.run(do_some_work())

