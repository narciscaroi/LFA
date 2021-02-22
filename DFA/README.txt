read_word_from_file-> imi ia ca parametru fisierul, citeste prima linie si 
				separa '\n' de cuvantul de care aveam nevoie, cuvant care
				este pattern-ul

read_string_from_file-> are ca parametru fisierul, citeste prima linie intr-un
					auxiliar, apoi citeste a doua linie separand "\n", aceasta
					reprezentand textul
					
write_in_file-> Aceasta functie ia fiecare valoare din lista in care pastrez
			   rezultatul si il scrie in fisier.

check_is_next -> caz de baza : verifica daca caracterul pe care trebuie sa il verific
			este urmatorul din pattern
			
check_suffix_prefix -> Aici verific daca prefixul este si sufix. Cum caracterul primit
				nu trece automatul in starea urmatoarea (asta verifica functia 
				de mai sus), pornesc de la starea precedenta starii curente si verific
				toate posibilitatile de sufixe si prefixe pentru a verifica care este
				cel mai lung sufix care sa fie si prefix.
				
compute_delta -> Initializez o matrice care este un dictionar de liste
				 Prima "etapa" este cea in care initializez prima linie a acesstei
				matrici si anume linia "epsilon". In aceasta etapa, verific daca
				pe coloana x (caracterul 65+x) este primul caracter din pattern si
				pun 1 in caz pozitiv, daca nu 0.
				 Etapa 2, pentru urmatoarele linii care reprezinta 1 pentru prima 
				litera apoi "concatenarea" urmatoarelor caractere in functie de linia
				respectiva, iau fiecare caracter de pe coloana si verific cu 
				check_is_next daca caracterul este chiar urmatorul din pattern, 
				iar daca nu, verific cu check_suffix_prefix starea in care ma duce 
				litera pe care o analizez.

automata_matcher-> Este functia din curs care imi concateneaza intr-o lista
				fiecare index la care incepe pattern-ul in text.