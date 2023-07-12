import PySimpleGUI as sg

from pyclashbot.interface.theme import THEME

sg.theme(THEME)


def stat_box(stat_name: str, size=(5, 1)) -> sg.Text:
    return sg.Text(
        "0",
        key=stat_name,
        relief=sg.RELIEF_SUNKEN,
        text_color="blue",
        size=size,
    )


battle_stats_title: list[list[sg.Text]] = [
    [
        sg.Text("Wins: "),
    ],
    [
        sg.Text("Losses: "),
    ],
    [
        sg.Text("Cards Played: "),
    ],
    [
        sg.Text("1v1 Fights: "),
    ],
    [
        sg.Text("2v2 Fights: "),
    ],
    [
        sg.Text("War Fights: "),
    ],
]

battle_stats_values = [
    [
        stat_box("wins"),
    ],
    [
        stat_box("losses"),
    ],
    [
        stat_box("cards_played"),
    ],
    [
        stat_box("1v1_fights"),
    ],
    [
        stat_box("2v2_fights"),
    ],
    [
        stat_box("war_fights"),
    ],
]

battle_stats = [
    [
        sg.Column(battle_stats_title, element_justification="right"),
        sg.Column(battle_stats_values, element_justification="left"),
    ]
]

progress_stats_titles = [
    [
        sg.Text("Requests: "),
    ],
    [
        sg.Text("Chests Unlocked: "),
    ],
    [
        sg.Text("Card Mastery Rewards: "),
    ],
    [
        sg.Text("Cards Upgraded: "),
    ],
    [
        sg.Text("Account Switches: "),
    ],
    [
        sg.Text("Restarts b/c Failure: "),
    ],
]

progress_stats_values = [
    [
        stat_box("requests"),
    ],
    [
        stat_box("chests_unlocked"),
    ],
    [
        stat_box("card_mastery_reward_collections"),
    ],
    [
        stat_box("upgrades"),
    ],
    [
        stat_box("account_switches"),
    ],
    [
        stat_box("restarts_after_failure"),
    ],
]

progress_stats = [
    [
        sg.Column(progress_stats_titles, element_justification="right"),
        sg.Column(progress_stats_values, element_justification="left"),
    ]
]

collections_stats_titles = [
    [
        sg.Text(
            "Card Mastery Reward Collections: ",
        ),
    ],
    [
        sg.Text("Free Offer Collections: "),
    ],
]

collections_stats_values = [
    [
        stat_box("card_mastery_reward_collections"),
    ],
    [
        stat_box("free_offer_collections"),
    ],
]

collections_stats = [
    [
        sg.P(),
        sg.Column(collections_stats_titles, element_justification="right"),
        sg.Column(collections_stats_values, element_justification="left"),
    ],
]
