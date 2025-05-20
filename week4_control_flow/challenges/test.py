from ai import call_gpt
import time
import random
import textwrap

def main():
    """Milestone #1: Game presentation"""
    title = "\033[\x1b[101m" + "Kobayashi Maru".center(75) + "\033[0m"
    print("\n" + title)

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
    """
    Precondition:   title and ascii present
    Postcondition: Context with delay using time lib
    """
    # List of vessel data to display with delay
    vessel_data = [
        "CLASS: NEUTRONIC FUEL CARRIER - CLASS III",
        "REGISTRY: AMBER, TAU CETI III",
        "MASTER: KOJIRO, VANCE",
        "CREW: 81",
        "PASSANGERS: 300",
        "MASS: 147,943 MT",
        "LENGHT: 237 M",
        "BEAM: 111 M",
        "HEIGHT: 70 M",
        "MAX.CRUISE WF: 3",
        "EMERGENCY WF: 6"
    ]
    delay = 0.5
    for line in vessel_data:
        print("\033[\x1b[92m" + line + "\033[0m")
        time.sleep(delay)
    

    """Milestone #2: Player setup and Neutral Zone"""
    print("\n" + "=== Command Profile Setup ===" + "\n")
    commander_name = input("Commander enter your name: ")
    # Aks about NZ
    print("\nDo you wish to cross into the Neutral Zone to attempt a rescue?")
    print("1. Yes - Enter the Neutral Zone to help the Kobayashi Maru.")
    print("2. No - Remain outside and report the incident to Starfleet.")

    enter_choice = ""
    while enter_choice not in ["1", "2"]:
        enter_choice = input("Enter 1 or 2: ").strip()
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
        time.sleep(0.4)
        print("You send a priority-one transmission to Starfleet Command and await further orders.")
        print("The Kobayashi Maru continues to transmit distress signals... then falls silent.\n")
        time.sleep(1)

        # Crew Rebels
        print("\nA tense silence grips the bridge...")
        time.sleep(1)
        print("Suddenly, your First Officer stands up.")
        print("Commander, with all due respect... we can't just sit here!")
        time.sleep(1)
        print("The crew overrides your orders and sets course for the Neutral Zone.\n")
        time.sleep(2)
        print("Moments later, Klingon battle cruisers appear on sensors.\n")
        time.sleep(1)

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
        time.sleep(0.5)

        print("Your crew looks to you once more...\n")
        print("You're now back in command.")
        time.sleep(1)

    # Decision making
    print(f"How would you like to proceed, Commander {commander_name}? ")
    print("1. Engage the Klingon Ships in combat.")
    print("2. Attemp diplomacy - hail the Klingons.")
    print("3. Retreat and protect your crew.")

    action_choice = ""
    while action_choice not in ["1", "2", "3"]:
        action_choice = input("Enter 1,2 or 3: ").strip()

    action_map = {
        "1": "Engage in combat",
        "2": "Attemp diplomacy",
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
        )
    drink = beverage_options[drink_choice]
    
    """Milestone #3: Some context after the Klingon appeared"""
    print("\nProcessing your decission...\n")
    time.sleep(0.5)

    extra_context = ""

    # Engage in combat 
    if action_choice == "1":
        print("Tactical alert: Weapon system online.")
        print("Choose your combat strategy:")
        print("1. Focus fire on a single target.")
        print("2. Evasive manuevers and spread fire.")
        print("3. Use engineering tricks (decoys, overloading systems).")
        delay = 0.5
        for i in action_choice:
            time.sleep(0.5)


if __name__ == "__main__":
    main()
