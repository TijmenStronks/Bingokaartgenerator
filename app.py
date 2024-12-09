import random
import matplotlib.pyplot as plt
from textwrap import fill
import streamlit as st

def generate_bingo_card(terms, size=5):
    selected_terms = random.sample(terms, size * size)
    bingo_card = [selected_terms[i:i + size] for i in range(0, len(selected_terms), size)]
    return bingo_card

def save_bingo_card_as_png(bingo_card, filename="bingo_card.png"):
    size = len(bingo_card)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.axis('off')

    # Draw grid
    for x in range(size + 1):
        ax.plot([x, x], [0, size], color='black', linewidth=2)
    for y in range(size + 1):
        ax.plot([0, size], [y, y], color='black', linewidth=2)

    # Add text to each cell with wrapping
    for i, row in enumerate(bingo_card):
        for j, term in enumerate(row):
            wrapped_text = fill(term, width=15)
            ax.text(
                j + 0.5, size - i - 0.5,
                wrapped_text,
                fontsize=14,
                weight='bold',
                ha='center', va='center'
            )

    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()

# Streamlit app
st.title("Kantoortaal Bingo Generator")
st.write("Klik op de knop hieronder om een bingokaart te genereren en te downloaden.")

if st.button("Genereer Bingokaart"):
    office_terms = [
        "Inspireren", "Inschieten", "Aanvliegroute", "Scherpe focus", "Helikopterview",
        "Out of the box", "Agile", "We nemen het mee", "Lessons learned", "De stip op de horizon",
        "Quick win", "Het laaghangend fruit", "Het fundament verstevigen", "Synergie", "Kort door de bocht",
        "Stakeholdermanagement", "Iedereen in zijn kracht zetten", "Dat moeten we even parkeren",
        "Samen optrekken", "Deep dive", "Transparant zijn", "Schouders eronder", "Roadmap",
        "Strategisch belang", "Hands-on mentaliteit", "Duurzaam inzetten", "Best practices",
        "Doorklinken naar de operatie", "De lijnen kort houden", "Risico mitigerende maatregelen",
        "Even afstemmen", "Klant centraal stellen", "Procesoptimalisatie", "Op de radar houden",
        "Ownership (eigenaarschap) nemen", "Groeien als persoon", "In de driver’s seat zitten",
        "Spin in het web", "Future-proof maken", "Escaleren waar nodig", "Efficiëntie vergroten",
        "De stip op de horizon", "Terugkoppelen", "Het momentum pakken", "In het vizier houden",
        "Commitment vragen", "De ruis wegnemen", "Change management", "Disruptief denken",
        "Value for money", "Stakeholder alignment", "Performance verbeteren", "Korte klap maken",
        "Impact maken", "Stroomlijnen", "Kennis borgen", "Benchmarken", "Integraal werken",
        "Strategische pijlers", "Scherp aan de wind varen", "Co-creatie", "Lean", "Value stream",
        "Doorontwikkelen", "Eilandjes doorbreken", "Duurzaam verankeren", "Het speelveld in kaart brengen",
        "Voeten in de klei", "Plannen en resources matchen", "Een haakje vinden", "De business case bewaken",
        "Met de neuzen dezelfde kant op", "Focus aanbrengen", "Data-driven werken", "Zichtbaarheid vergroten",
        "Inregelen", "Voortgang monitoren", "Escalatiemoment", "Capaciteit vrijmaken", "Op de kaart zetten",
        "Extraheren", "Overvragen (daar overvraag je me)", "Over de schutting (gooien)", "Samenwerking evalueren",
        "Levend document"
    ]

    bingo_card = generate_bingo_card(office_terms)
    save_bingo_card_as_png(bingo_card)

    with open("bingo_card.png", "rb") as file:
        st.download_button(
            label="Download Bingokaart",
            data=file,
            file_name="bingo_card.png",
            mime="image/png"
        )
