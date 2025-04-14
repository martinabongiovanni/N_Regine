import copy
from time import time

class NRegine():

    def __init__(self):
        self.n_soluzioni = 0 # contatore per tenere traccia delle possibili soluzioni che trovo
        self.n_chiamate = 0 # per tenere traccia di quante volte entro nella funzione ricorsiva
        self.soluzioni = [] # per tenere traccia delle soluzioni che ho già trovato ed evitare duplicati
                            # regine certe in posizioni ma salvate in indici diversi.

    def solve(self, N):
        '''
        qui faccio partire la ricorsione
        :param N:
        :return:
        '''
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self.ricorsione([], N)

    def is_admissible(self, regina1, regina2) -> bool: # -> bool serve all'editor per indicare che la funzione restituirà un booleano
        # 1) verifico riga: se non va bene return false
        if regina1[0] == regina2[0]:
            return False
        # 2) verifico colonna: se non va bene return false
        if regina1[1] == regina2[1]:
            return False
        # 3) verifico diagonale (somma): se non va bene return false
        if (regina1[0] + regina1[1]) == (regina2[0] + regina2[1]):
            return False
        # 4) verifico diagonale (differenza): se non va bene return false
        if (regina1[0] - regina1[1]) == (regina2[0] - regina2[1]):
            return False
        # 5) ho passato tutti i controlli: return true
        return True

    def is_soluzione(self, parziale):
        # per ogni regina devo andare a verificare tutte le altre regine
        for i in range(len(parziale)-1):
            for j in range(i+1, len(parziale)):
                result = self.is_admissible(parziale[i], parziale[j])
                if result is False:
                    return False
        return True

    def is_valid(self, nuova_regina, parziale):
        for regina in parziale:
            if not self.is_admissible(nuova_regina, regina):
                return False
        return True

    def ricorsione(self, parziale, N):
        '''
        questo è il metodo effettivamente ricorsivo, chiamato più volte
        :param parziale: è una lista in cui andrò a inserire le coppie R-C che caratterizzano le regine
        :return:
        '''
        self.n_chiamate += 1
        # condizione terminale: se parziale ha lunghezza N
        if len(parziale)==N:
            # => verifico se questa è una soluzione parziale
            print(parziale)
            self.soluzioni.append(copy.deepcopy(parziale))
            self.n_soluzioni += 1 # trovata una soluzione, aggiorno il contatore
        # caso ricorsivo:
        else:
            for riga in range(N):
                for col in range(N):
                    # => Check sulla regina che vado ad aggiungere
                    nuova_regina = [riga, col]
                    # provo nuova ipotesi aggiungendo una regina
                    if self.is_valid(nuova_regina, parziale):
                        parziale.append([riga, col])
                        # vado avanti nella ricorsione
                        self.ricorsione(parziale, N)
                        # backtracking se mi accorgo che non posso inserire la regina in quella posizione
                        parziale.pop()



if __name__ == '__main__':
    start_time = time()
    n_regine = NRegine()
    n_regine.solve(4)
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}")
    print(f"Ho trovato {n_regine.n_soluzioni} (possibili) soluzioni.")
    print(f"N. chiamate ricorsione: {n_regine.n_chiamate}")