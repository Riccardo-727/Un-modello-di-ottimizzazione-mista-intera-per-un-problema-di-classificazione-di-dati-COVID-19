set OSSERVAZIONI;
set FEATURES;
set BRANCH_NODES;
set LEAF_NODES ;
set TOTAL_NODES;
set CLASSI;
set A_L {TOTAL_NODES};
set A_R {TOTAL_NODES};




/*numero osservazioni*/
param N;

/*numero caratteristiche*/
param P;

/*parametro che identifica il numero totale di nodi dell'albero*/
param T;

/*parametro che identifica l'altezza dell'albero*/
param D;

/*parametro che identifica il minimo numero di punti nelle foglie*/
param N_min;

/*parametro usato nelle due equazioni che impongono la struttura dell'albero*/
param mu;

/*serve pre normalizzare l'errore di clasificazione*/
param L_tilda;

/*variabile temporanea usata nel calcolo degli antenati destri e sinistri */
param temp;

/*matrice che ha per righe le osservazini x(i) per la fase di training*/
param x {OSSERVAZIONI, FEATURES};

/*matrice che ha per righe le osservazini x(i) per la fase di testing*/
param x_tes {OSSERVAZIONI_TEST, FEATURES};

/*vettore che rappresenta la classe di ogni osservazione per la fase di training*/
param y {OSSERVAZIONI} binary;

/*vettore che rappresenta la classe di ogni osservazione per la fase di testing*/
param y_tes {OSSERVAZIONI_TEST} binary;

/*matrice che tiene traccia delle classi delle osservazioni*/
param Y {i in OSSERVAZIONI, k in CLASSI} = if y[i] == k then 1 else -1;








/* z(i,t) vale 1 se il vettore x(i) e' nel nodo t */
var z {OSSERVAZIONI, TOTAL_NODES} binary ;

/* l(t) vale 1 se il nodo foglia t contiene almeno un punto */
var l {LEAF_NODES} binary;

/* s(j,t) vale 1 se la j-esima features e' usata nello split del branch node t*/
var s {FEATURES, BRANCH_NODES} binary;

/* d(t) vale 1 se il branch node t viene splittato */
var d {BRANCH_NODES} binary;

/* variabile che viene usata per il vincolo ax<b*/
var b {BRANCH_NODES};

/*rappresentano i vettori a che vengono combinati con le osservazioni x per determinare gli split*/
var a {FEATURES, BRANCH_NODES} <= 1 , >= -1;

/*sono usati per linearizzare il valore assoluto nel vincolo SUM{j=1 to p}abs(a(j,t)) <= d(t)*/
var a_capp {FEATURES, BRANCH_NODES} <= 1 , >= -1;

/*usata per linearizzare il valore assoluto di a*/
var bin {FEATURES, BRANCH_NODES} binary;

/*rappresenta il numero di x(i) con etichetta k nel nodo t*/
var N_kt {k in CLASSI,t in LEAF_NODES} = 1/2 * sum {i in OSSERVAZIONI}(1 + Y[i,k])*z[i,t];

/*rappresenta il numero totale di x(i) caduti nel nodo foglia t*/
var N_t {t in LEAF_NODES} = sum {i in OSSERVAZIONI} z[i,t];

/* c(k,t)=1 se la classe del nodo t è k*/
var c_kt {k in CLASSI, t in LEAF_NODES} binary;

/*rappresenta l errore di classificazione per ogni nodo foglia t*/
var L_t{t in LEAF_NODES} >=0;





#FUNZIONE OBIETTIVO
minimize obiettivo:
	(1/L_tilda) *sum {t in LEAF_NODES}  (L_t[t]) 
		+ alpha * sum{t in BRANCH_NODES, j in FEATURES} (s[j,t]);


#vincolo d(t) <= d_p(t) ovvero nodo figlio puo splittare solo se lo fa il padre
subject to eq1 {t in BRANCH_NODES diff {1}}: 
	d[t] <= d[floor(t/2)];

#impone il vincolo che se un nodo non viene splittato (d(t)=0) allora anche b(t)=0 perche si e obbligati a scegliere la diramazione dx ovvero 0<0 falso
#essendo che nel vincolo originale la parte sx e dx contengono variabili bisogna splitttare il vincolo in due
subject to eq2_1 {t in BRANCH_NODES}:
	b[t] <= d[t];

subject to eq2_2 {t in BRANCH_NODES}:
	-d[t] <= b[t];
	
#impongono i vincoli che d(t)=1 se almeno una futures nel nodo t e' stata usata per eseguire lo split
# e s(j,t)=0 se il nodo t non viene splittato
subject to eq3_1 {t in BRANCH_NODES}:
	sum{j in FEATURES} s[j,t] >= d[t];
	
subject to eq3_2 {j in FEATURES, t in BRANCH_NODES}:
	s[j,t] <= d[t];
	
#vincoli che servono per rendere a(j,t) e s(j,t) compatibili, infatti la features j-esima non puo' assumere valori diversi da zero in un nodo t se la variabile s(j,t)=0
subject to eq4_1 {j in FEATURES, t in BRANCH_NODES}:
	a[j,t] <= s[j,t];

subject to eq4_2 {j in FEATURES, t in BRANCH_NODES}:
	-s[j,t] <= a[j,t];

#rappresenta il vincolo SUM{j=1 to p}abs(a(j,t)) <= d(t), che viene linearizzato mediante l'ausilio delle variabili a_capp
subject to eq5_1 {j in FEATURES, t in BRANCH_NODES}:
	a_capp[j,t] >= a[j,t];

subject to eq5_2 {j in FEATURES, t in BRANCH_NODES}:
	a_capp[j,t] >= -a[j,t];

#questi due vincoli	servono per dire che a_capp è una delle due variabili (a o -a) altrimenti avrei un intervallo di valori che può assumere a ovvero a_capp
subject to eq5_3 {j in FEATURES, t in BRANCH_NODES}:
	a_capp[j,t] <= -a[j,t] + 2*(1-bin[j,t]); 
	
subject to eq5_4 {j in FEATURES, t in BRANCH_NODES}:
	a_capp[j,t] <= a[j,t] + 2*(bin[j,t]); 

subject to eq5_5 {t in BRANCH_NODES}:
	sum {j in FEATURES} a_capp[j,t] <= d[t];
		
#se un nodo foglia contiene almeno un punto (l(t)=1) allora ci dovranno essere almeno N_min punti (prima equazione) altrimenti se l(t)=0 allora la variabile z(i,t)=0 ovvero nessun punto nel nodo foglia t
subject to eq6_1{t in LEAF_NODES}:
	sum {i in OSSERVAZIONI} z[i,t] >= N_min*l[t];

subject to eq6_2{i in OSSERVAZIONI, t in LEAF_NODES}:
	z[i,t] <= l[t];
	
#ovvero un' osservazione x(i) puo' cadere solo in nodo foglia
subject to eq7 {i in OSSERVAZIONI}:
	sum {t in LEAF_NODES} z[i,t] = 1;

#vincoli che impongono la struttura dell'albero(!! t l'ho messo in total node, senno cosi si salta l' ultimo livello) chiedere alla prof se va bene, il modello faceva t in BRANCH_NODES
subject to eq8_1 {i in OSSERVAZIONI, t in LEAF_NODES, a_l in A_L[t]}:
	sum {j in FEATURES} (a[j,a_l]*x[i,j]) + mu <= b[a_l] + (2 + mu)*(1 - z[i,t]);
	
subject to eq8_2 {i in OSSERVAZIONI, t in LEAF_NODES, a_r in A_R[t]}:
	sum {j in FEATURES} (a[j,a_r]*x[i,j]) >= b[a_r] - 2*(1 - z[i,t]);

#per ogni nodo foglia che contiene almeno un punto la previsione dovra ritornare esattamente una classe
subject to eq9 {t in LEAF_NODES}: 
	sum {k in CLASSI} c_kt[k,t] = l[t];

#equazioni che servono per linearizzare il vincolo L_t = N_t - max k=1..K {N_kt}
subject to eq10 {k in CLASSI, t in LEAF_NODES}:
	L_t[t] <= N_t[t] - N_kt[k,t] + N*(1 - c_kt[k,t]);#questo vincolo è stato modificato rispetto all'originale, chiedere alla prof se è giusto
	
subject to eq11 {k in CLASSI, t in LEAF_NODES}:
	L_t[t] >= N_t[t] - N_kt[k,t] - N*(1 - c_kt[k,t]);



