check-language-> Aceasta functie imi verifica, la citire, daca o litera este
			deja in alfabet

state_exist_in_eps-> Imi verifica daca o stare anume are tranzitii directe cu
			o alta stare

epsilon_closure-> Imi creeaza un dictionar de liste in care retin pentru
			fiecare stare, toate starile in care pot ajunge, atat direct,
			cat si indirect(prin alte stari), doar prin epsilon-tranzitii
			
calculate_tranzition-> Imi calculeaza tranzita pentru fiecare caracter
			pentru o anumita stare

get_dfa_delta_index-> Imi returneaza index-ul atribuit unei stari
			pentru coloana
			
get_dfa_delta_lindex-> Imi returneaza index-ul pentru linia din dfa
			atribuit unei stari

check_exist_final_state_initial-> Imi returneaza 1 sau 0 daca trebuie
			initial sa adaug o stare finala
			
check_exist_final_state-> Returneaza 1 sau 0 daca ulterior mai trebuie
			sa adaug o stare finala in lista

compute_dfa_delta-> Imi calcueaza tabelul pentru dfa. Pentru o anumita
			stare, calculez tranzitia pentru fiecare caracter, verifica
			daca face parte dintr-o stare acoperita, adica pusa deja in
			tabel, daca nu face parte din aceasta categorie, o adaug in
			lista de cele acoperite, in coada pentru a o acoperi si cand
			"ii ajunge randul", o voi scoate din coada si o voi pune in 
			tabel cu tranzitiile calculate

main-> fac citirea din fisier, o data cu citirea imi creez si limbajul
	folosit in automat si il sortez
	-> apelez si functiile necesare pentru a crea epsilon-tranzitiile
	si tabelul pentru dfa apoi urmeaza scrierea in fisier