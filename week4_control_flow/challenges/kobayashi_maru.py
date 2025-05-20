from ai import call_gpt
import time
import random
import textwrap

def main():
    """Milestone #1: Game presentation and player name"""
    title = "\033[\x1b[101m" + "Kobayashi Maru".center(75) + "\033[0m"
    print("\n" + title)

    print("\n" + "=== Command Profile Setup ===" + "\n")
    
    # Possible fallback Star Trek names
    default_names = [
        "T'Varis", 
        "Kira Dax", 
        "S'Rell", 
        "Gral", 
        "N'vek", 
        "Threx of Andor", 
        "Zelora Dax", 
        "Meowlox"
    ]

    commander_name = input("Commander, enter your name: ").strip()

    if not commander_name:
        commander_name = random.choice(default_names)
        print(f"\nNo name entered. Assigning identity: \033[93m{commander_name}\033[0m\n")
    else:
        print(f"\nWelcome aboard, Commander \033[96m{commander_name}\033[0m.\n")

    extra_context = ""

    # ASCII art of the USS Enterprise NCC-1701
    intro_art = r"""
        _______________________          _-_             
       \________________|)____.---'---`---._______
                        ||    \----._________.----/     
                        ||     / ,'   `---'               
                     ___||_,--'  -._                     
                    /___          ||(-                        
                        `---._____-'

    """
    print("\033[\x1b[96m" + intro_art + "\033[0m")
    print("")

    scenario_intro = (
        "You are seated in the command chair of a Constitution-class starship. "
        "The lights dim. The simulation begins."
        "This is the Kobayashi Maru — a Starfleet training scenario designed to test "
        "the character of its commanders under impossible conditions. "
        "Your ship is patrolling the edge of the Neutral Zone, a fragile boundary "
        "between the Federation, the Klingon Empire, and the Romulan Star Empire. "
        "Suddenly, a distress call pierces the silence. The Kobayashi Maru, "
        "a civilian fuel carrier, has struck a gravitic mine and was dragged inside the Neutral Zone. "
        "Its hull is breached. Hundreds of lives hang in the balance. "
        "To cross the border is to risk war. To ignore the call is to abandon innocents. "
    )
    # Formatting setup top to bottom
    width = 70
    border = "   +" + "-" * (width - 2) + "+" 
    # Process the text
    wrapped_text = textwrap.fill(scenario_intro, width=width-6)
    box_lines = wrapped_text.split('\n')

    print(border)
    for line in box_lines:
        print(f"    | {line.ljust(width-6)} |")
    print(border)
    
    
    mission_summary = (
        "\nMISSION SUMMARY: \n"
        "A Federation civilian vessel, the Kobayashi Maru, has sent out a distress signal from within the Neutral Zone.\n"
        "Your task is to assess the situation and attempt a rescue operation under unknown and potentially hostile conditions.\n"
        "Proceed with extreme caution — any violation of treaty borders could provoke a confrontation with the Klingon Empire."
    )

    print("\033[\x1b[92m" + mission_summary + "\033[0m")
    print("")

    # List of vessel data to display with delay
    vessel_data = [
        "CLASS: NEUTRONIC FUEL CARRIER - CLASS III",
        "REGISTRY: AMBER, TAU CETI III",
        "MASTER: KOJIRO, VANCE",
        "CREW: 81",
        "PASSENGERS: 300",
        "MASS: 147,943 MT",
        "LENGTH: 237 M",
        "BEAM: 111 M",
        "HEIGHT: 70 M",
        "MAX.CRUISE WF: 3",
        "EMERGENCY WF: 6"
    ]
    delay = 0.5
    for line in vessel_data:
        print("\033[\x1b[92m" + line + "\033[0m")
        time.sleep(delay)
    

    """Milestone #2: Neutral zone, choices"""
    # Ask about NZ
    print("\nDo you wish to cross into the Neutral Zone to attempt a rescue?")
    print("1. Yes - Enter the Neutral Zone to help the Kobayashi Maru.")
    print("2. No - Remain outside and report the incident to Starfleet.")

    enter_choice = ""
    while enter_choice not in ["1", "2"]:
        enter_choice = input("\033[\x1b[92m" + "Enter 1 or 2: " + "\033[0m" ).strip()
    entered_neutral_zone = "yes" if enter_choice == "1" else "no"
    # says yes:
    if entered_neutral_zone == "yes":
        # Klingon ships ASCII
        klingon_ship =r"""
                        //-n-\\
                _____---=======---_____
            ====____\   /.. ..\   /____====
        //           ---\__O__/---         \\
        \_\                             /_/

                                                __                             __
                                                / /                             \ \
                                                \\           ___/~~O~~\___         //
                                                    ====____/   \.. ../   \____====
                                                        -----___=======___-----
                                                                \\-u-//
        """
        time.sleep(0.5)
        print("\033[\x1b[92m" + klingon_ship +"\033[0m")
        time.sleep(0.5)
        print(
        "\nHostile Klingon battle cruisers begin to appear on sensors...\n"
        "This is not a test of victory — it is a test of who you choose to be.\n"
        )
    else:
        print("\nYou remain outside the Neutral Zone.")
        time.sleep(1)
        print("You send a priority-one transmission to Starfleet Command and await further orders.")
        print("The Kobayashi Maru continues to transmit distress signals... then falls silent.\n")
        time.sleep(2)


        # Crew Rebels
        print("\nA tense silence grips the bridge...")
        time.sleep(2)
        print("Suddenly, your First Officer stands up.")
        print("Commander, with all due respect... we can't just sit here!")
        time.sleep(2)
        print("The crew overrides your orders and sets course for the Neutral Zone.\n")
        time.sleep(3)
        print("Moments later, Klingon battle cruisers appear on sensors.\n")
        time.sleep(4)

        # Klingon ships ASCII
        klingon_ship =r"""

                        //-n-\\
                _____---=======---_____
            ====____\   /.. ..\   /____====
        //           ---\__O__/---         \\
        \_\                               /_/

                                            __                             __
                                            / /                             \ \
                                            \\           ___/~~O~~\___       //
                                                ====____/   \.. ../   \____====
                                                    -----___=======___-----
                                                            \\-u-//

        """
        print("\033[\x1b[92m" + klingon_ship + "\033[0m")
        time.sleep(5)

        print("Your crew looks to you once more...\n")
        print("You're now back in command.")
        time.sleep(1)

    """Milestone #3: Decision after Klingons appear"""
    # Decision making
    print(f"How would you like to proceed, Commander {commander_name}? ")
    print("1. Engage the Klingon Ships in combat.")
    print("2. Attempt diplomacy - hail the Klingons.")
    print("3. Retreat and protect your crew.")

    action_choice = ""
    while action_choice not in ["1", "2", "3"]:
        action_choice = input("\033[\x1b[92m" + "Enter 1,2 or 3: "+ "\033[0m" ).strip()

    action_map = {
        "1": "Engage in combat",
        "2": "Attempt diplomacy",
        "3": "Retreat"
    }

    action = action_map[action_choice]

    beverage_options = {
        "1": "Raktajino",
        "2": "Earl Grey",
        "3": "Romulan Ale"
    }

    drink_choice = ""
    while drink_choice not in beverage_options:
        drink_choice = input(
            "\nWhat is your beverage of choice, Commander?\n"
            "1. Raktajino - Klingon coffee, strong and bold\n"
            "2. Earl Grey - Hot - Captain Picard's classic tea\n"
            "3. Romulan Ale - Illegal but very, very blue\n"
            "Enter 1, 2 or 3: "
        ).strip()
    drink = beverage_options[drink_choice]
    
    print("\nProcessing your decision...\n")
    time.sleep(0.5)

    # Engage in combat 
    if action_choice == "1":
        print("Tactical alert: Weapon system online.")
        print("Choose your combat strategy:")
        print("1. Focus fire on a single target.")
        print("2. Evasive maneuvers and spread fire.")
        print("3. Use engineering tricks (decoys, overloading systems).")
        
        combat_choice = ""
        while combat_choice not in ["1", "2", "3"]:
            combat_choice = input("\033[\x1b[92m" + "Enter 1, 2 or 3: " + "\033[0m").strip()

        combat_map = {
            "1": "Focused fire on one Klingon cruiser.",
            "2": "Executed evasive maneuvers with wide phaser spread.",
            "3": "Used engineering to deploy decoys and reroute power."
        }
        extra_context = combat_map[combat_choice]

    # Attempt diplomacy
    if action_choice == "2":
        print("Opening hailing frequencies to Klingon battle cruisers...\n")
        time.sleep(1)
        print("Choose your diplomatic strategy:")
        print("1. Propose a cooperative rescue mission.")
        print("2. Seek a diplomatic solution through negotiation.")
        print("3. Deliver a professional ultimatum warning.")

        diplomacy_choice = ""
        while diplomacy_choice not in ["1", "2", "3"]:
            diplomacy_choice = input("\033[\x1b[92m" + "Enter 1, 2 or 3: " + "\033[0m").strip()

        diplomacy_map = {
            "1": "Proposed a cooperative rescue mission with shared honor and effort.",
            "2": "Initiated diplomatic negotiation, offering data and appealing to peace.",
            "3": "Issued a firm ultimatum while preparing for defensive measures."    
        }

        extra_context = diplomacy_map[diplomacy_choice]

    # Retreat
    if action_choice == "3":
        print("Initiating retreat protocol...")
        time.sleep(1)

        print("\nYou order a full withdrawal from the Neutral Zone perimeter.")
        print("Sensors scan for the safest escape route while shields come online.")
        time.sleep(1)

        print("\nHow do you want to handle the retreat?")
        print("1. Contact Starfleet for backup and inform the Kobayashi Maru.")
        print("2. Use evasive maneuvers through a nebula to avoid detection.")
        print("3. Deploy decoys and jam signals to distract the Klingons.")

        retreat_choice = ""
        while retreat_choice not in ["1", "2", "3"]:
            retreat_choice = input("\033[\x1b[92m" + "Enter 1, 2 or 3: " + "\033[0m").strip()

        retreat_map = {
            "1": "Requested Starfleet assistance and informed the Kobayashi Maru of your decision.",
            "2": "Executed evasive maneuvers through a nearby nebula to ensure a stealthy retreat.",
            "3": "Deployed decoy drones and disrupted Klingon sensors during withdrawal."
        }
        extra_context = retreat_map[retreat_choice]

    """Milestone #4: Stored player data"""
    player_data = {
        "name": commander_name,
        "entered_neutral_zone": entered_neutral_zone,
        "action": action,
        "beverage": drink,
        "strategy": extra_context
    }

    """Milestone #5: IA endings"""
    story_prompt = f"""
    You're a comedic Starfleet simulation narrator from the year 2400.
    The player has just decided their strategy choices for the legendary Kobayashi Maru test - a no win scenario.
    Your job is to generate a completely absurd, scientifically-flavored, catastrophic ending to the mission,
    based on the player's decisions, while keeping the tone in-universe, overly dramatic, and hilarious.
    
    Commander Profile:
    - Name: {player_data['name']}
    - Neutral Zone Decision: {player_data['entered_neutral_zone']}
    - Final Action Taken: {player_data['action']}
    - Beverage of Choice: {player_data['beverage']}
    - Strategy Chosen: {player_data['strategy']}

    Instructions:
    1. Begin by summarizing what appeared to be a promising moment of hope or tactical success.
    2. Immediately follow with an outrageous, catastrophic event (e.g., space whales, interdimensional pie storms, Klingon karaoke virus outbreak, warp core meltdown caused by a banana peel).
    3. End with a short, funny, *inspirational quote* about the importance of failure, delivered in the tone of a wise old Vulcan or a malfunctioning AI.
    4. It must sound like it's part of the official Starfleet training logs — overly formal, but absolutely ridiculous.

    Make it brief, punchy, and laugh-out-loud weird.
    """
    response = call_gpt(story_prompt)
    print(response)

if __name__ == "__main__":
    main()
