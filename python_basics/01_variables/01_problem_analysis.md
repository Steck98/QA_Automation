# problem_analysis 01 — Character Data Model Analysis

Scenario

    You are designing the data model for a single RPG/MMORPG character.

    In the future, the game will support features such as:

    Inventory
    Guilds and Factions
    Quests
    Trading
    Crafting
    Achievements
    Rankings
    PvP
    Pets
    Reputation with different factions
    Standard and Premium Currencies
    Your Task

1. Data Categories

Divide all character information into logical categories.

Each category should represent one specific area of the character.

2. Fields

    For every field include:

    Field name (English)
    Suggested Python variable name
    Example value

    Example:

    Character Name

    Variable: character_name

    Example: "Aldren"

3. Justification

    For every category, write a short explanation (1–3 sentences):

    Why do these fields belong together?
    Why shouldn't they belong to another category?

4. Design Decisions

    Answer the following questions using your own reasoning.

    There are no predefined correct answers — the goal is to justify your decisions.

    Should reputation be represented as a single value or as separate values for each faction?
    Are runes a currency, a resource, or inventory items?
    Does the VIP level belong to the character or to the player's account?
    Should the portrait be considered character data or only a user interface element?
    Which fields are expected to change very frequently during gameplay?
    Which fields will most likely remain unchanged throughout the game?
    Goal

    The objective of this challenge is not to write Python code.

    Instead, focus on:

    analyzing the problem,
    organizing data logically,
    making design decisions,
    justifying your reasoning.

    Think like a software engineer before writing any code.




0.1

Data Categories:

    Inventory Managment: Every of this field i tied up to inventory managment, some currencies can be stored and occupy a slot in the inventory, or have a separate one, pets can be stored too in a personal inventory or have a separate storage for them, trading window has a separate inventory too usually.
        Trading,Inventory,Pets,Standard and Premium Currencies

        trading_window_inventory
        player_inventory
        pets_storage
        currency_storage

    Social: Every of this fields has interactions with the social aspect of a game, interactions between players like fighting, playing together, building guilds, reinforcing their factions and community
        Reputation with different factions, Guilds and Factions,PvP

        faction_reputation
        guild_window
        faction_window
        pvp_window


    Hall of Fame:Every field is tied up to the progress of a player, his achievement and his ranking, how far he gone and what goals he achieved, its a category to show off someone

        Achievements, Rankings
        achievement_window

    Skills: Category tied to skills and perks of a player, focused only on aspects of a character that are about personal developmentm trading here has been added again cuz it could go in 2 sections depending on the features of the game.
        Crafting,Trading

        crafting_perk
        trading_perk

    Progress:This fields are together cuz they both adress the mission category of a player, the quest that he has to do, he has done and he is doing, the overall campaign progress

        Quests,Your Task

        quests_list
        current_quest
