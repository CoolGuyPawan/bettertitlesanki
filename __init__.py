#

from anki.hooks import addHook
from aqt import mw

class DeckNamer:
    def card_title(self):
        """Set the window title to display the name of the deck (subdeck) that is currently being studied"""
        current_card = mw.reviewer.card
        
        # Get the full deck name associated with the card
        full_deck_name = mw.col.decks.get(current_card.did)['name']
        # Extract the current subdeck name
        subdeck_name = full_deck_name.split("::")[-1].strip()

        # Determine if you're in a custom study session
        if current_card.odid != current_card.did:
            # Get the original deck name
            original_deck_name = mw.col.decks.get(current_card.odid)['name']
            original_subdeck_name = original_deck_name.split("::")[-1].strip()
            title = f"{subdeck_name}: {original_subdeck_name}"
        else:
            title = subdeck_name

        # Clean the title by removing ": Default" if present
        title = title.replace(': Default', '').strip()

        # Set the window title
        mw.setWindowTitle(title)

deck_namer = DeckNamer()
addHook('showQuestion', deck_namer.card_title)
