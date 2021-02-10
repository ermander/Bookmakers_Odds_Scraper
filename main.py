# Importing all scraping functions
from Betaland.seriaA import serieA
from Betaland.serieB import serieB
from Betaland.premierLigue import premierLigue
from Betaland.laLiga import laLiga
from Betaland.ligue1 import ligue1
from Betaland.bundesLiga import bundesLiga
from Betaland.nba import nba


def main():
    serieA()
    serieB()
    premierLigue()
    bundesLiga()
    laLiga()
    ligue1()
    nba()


main()