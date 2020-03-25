"""
`gauss.py` - Funktioner för Gauss-eliminering.
"""

import vectors as v

### Denna lilla kodsnutt ska man INTE ändra i.
class SingularMatrix(Exception):
    """En datatyp för felhantering,
    som bygger på Pythons egna felhanteringssystem.
    Man kan 'skapa' fel genom att skriva
    `raise SingularMatrix()`.
    """
    pass

############ TVÅ HJÄLPFUNKTIONER ########################
### Dessa ska man ändra i.

def find_pivot_row(matrix, col):
    """
    Hitta nästa pivot-element.

    Antag att matrisen `matrix` ser ut som följer på raderna [0, col):
    * Den har ettor på diagonalen, nollor till vänster om dessa.
    * Resten av raderna vet vi inget om.

    Vi vill hitta INDEX för nästa pivot-element, som ska ligga i kolumnen `col`.
    Leta på rad `col` och fortsätt nedåt. Återsänd index för den första raden som har 
    ett nollskilt element i kolumn `col`.

    Om inget pivot-element finns, fås felet `SingularMatrix`.
    """
    pass


def clean_rows(A, pivot_row_index, B):
    """'Städa' alla rader i matrisen `A`, om matrisen har pivot-elementet i rad 
    `pivot_row_index`.
    D.v.s. alla element i kolumnen där pivot-elementet finns, ska bli 0
    (utom pivot-elementet självt).
    Exakt samma radoperationer ska även appliceras på matrisen `B`.
    """
    pass


############ HUVUDFUNKTION ###################
### Denna funktion ska man ändra i.

def gauss_elim(A, B):
    """
    Löser det linjära ekvationssystemet AX=B genom Gauss-eliminering.
    A måste vara en kvadratisk matris (en n*n-matris).
    B måste vara en kolumnvektor (en n*1-matris).
    Återsänder lösningen X.

    Om ingen lösning finns, fås felet `SingularMatrix`.
    Observera att funktionen ändrar i ('förstör') matriserna A och B.
    """
    pass