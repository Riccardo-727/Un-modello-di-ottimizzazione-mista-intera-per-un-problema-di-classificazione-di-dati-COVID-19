set OSSERVAZIONI;
set FEATURES;
set BRANCH_NODES;
set LEAF_NODES;
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

/*parametro usato nella funzione obiettivo per tenere sotto controllo lacomplessità dell'albero*/
param alpha;

/*variabile temporanea usata nel calcolo degli antenati destri e sinistri */
param temp;


/*matrice osservazioni reali*/
#param x {1..150, 1..15};

/*vettore classi reali*/
#param y {1..150} binary;

/*paramero L tilda*/
#param L_tilda;

/*matrice che tiene traccia delle classi delle osservazioni*/
param Y {i in OSSERVAZIONI, k in CLASSI} = if y[i] == k then 1 else -1;

/*rappresenta l'antenato sinistro di valore massimo di una foglia*/
param a_l_max {t in LEAF_NODES diff {T}: t mod 2 != 0};




/* z(i,t) vale 1 se il vettore x(i) e' nel nodo t */
var z {OSSERVAZIONI, LEAF_NODES} binary ;

/* l(t) vale 1 se il nodo foglia t contiene almeno un punto */
var l {LEAF_NODES} binary;

/* d(t) vale 1 se il branch node t viene splittato */
var d {BRANCH_NODES} binary;

/* variabile che viene usata per il vincolo ax<b*/
var b {BRANCH_NODES}; 

/*rappresentano i vettori a che vengono combinati con le osservazioni x per determinare gli split*/
var a {FEATURES, BRANCH_NODES} binary;

/*rappresenta il numero di x(i) con etichetta k nel nodo t*/
var N_kt {k in CLASSI,t in LEAF_NODES} = 1/2 * sum {i in OSSERVAZIONI}((1 + Y[i,k])*z[i,t]);

/*rappresenta il numero totale di x(i) caduti nel nodo foglia t*/
var N_t {t in LEAF_NODES} = sum {i in OSSERVAZIONI} z[i,t];

/* c(k,t)=1 se la classe del nodo t è k*/
var c_kt {k in CLASSI, t in LEAF_NODES} binary;

/*rappresenta l errore di classificazione per ogni nodo foglia t*/
var L_t{t in LEAF_NODES} >=0;





#FUNZIONE OBIETTIVO
minimize obiettivo:
	(1/L_tilda) *sum {t in LEAF_NODES}  (L_t[t]) 
		+ alpha * sum{t in BRANCH_NODES} (d[t]);



#vincolo d(t) <= d_p(t) ovvero nodo figlio puo splittare solo se lo fa il padre
subject to eq1 {t in BRANCH_NODES diff {1}}: 
	d[t] <= d[floor(t/2)];

#impone il vincolo che se un nodo non viene splittato (d(t)=0) allora anche b(t)=0 perche si e obbligati a scegliere la diramazione dx ovvero 0<0 falso
#essendo che nel vincolo originale la parte sx e dx contengono variabili bisogna splitttare il vincolo in due
subject to eq2_1 {t in BRANCH_NODES}:
	b[t] <= d[t];

subject to eq2_2 {t in BRANCH_NODES}:
	b[t] >= 0;
	
#equazione che impone che sono 1 features viene usata nello split	
subject to eq5_5 {t in BRANCH_NODES}:
	sum {j in FEATURES} a[j,t] = d[t]; 
		
#se un nodo foglia contiene almeno un punto (l(t)=1) allora ci dovranno essere almeno N_min punti (prima equazione) altrimenti se l(t)=0 allora la variabile z(i,t)=0 ovvero nessun punto nel nodo foglia t
subject to eq6_1{t in LEAF_NODES}:
	sum {i in OSSERVAZIONI} z[i,t] >= N_min*l[t];

subject to eq6_2{i in OSSERVAZIONI, t in LEAF_NODES}:
	z[i,t] <= l[t];
	
#ovvero un' osservazione x(i) puo' cadere solo in nodo foglia
subject to eq7 {i in OSSERVAZIONI}:
	sum {t in LEAF_NODES} z[i,t] = 1;

#vincoli che impongono la struttura dell'albero
subject to eq8_1 {i in OSSERVAZIONI, t in LEAF_NODES, a_l in A_L[t]}:
	sum {j in FEATURES} ( a[j,a_l]*(x[i,j] + mu ) )  + (2 + mu )*(1-d[a_l])  <= b[a_l] + (2 + mu)*(1 - z[i,t]);
	
subject to eq8_2 {i in OSSERVAZIONI, t in LEAF_NODES, a_r in A_R[t]}:
	sum {j in FEATURES} ( a[j,a_r]*(x[i,j] ) ) >= b[a_r] - 2*(1 - z[i,t]);

#per ogni nodo foglia che contiene almeno un punto la previsione dovra ritornare esattamente una classe
subject to eq9 {t in LEAF_NODES}: 
	sum {k in CLASSI} c_kt[k,t] = l[t];

#equazioni che servono per linearizzare il vincolo L_t = N_t - max k=1..K {N_kt}
subject to eq10 {k in CLASSI, t in LEAF_NODES}:
	L_t[t] <= N_t[t] - N_kt[k,t] + N*c_kt[k,t];
	
subject to eq11 {k in CLASSI, t in LEAF_NODES}:
	L_t[t] >= N_t[t] - N_kt[k,t] - N*(1 - c_kt[k,t]);

#vincoli che legano la variabile d con la variabile l
subject to eq12_1 {t in LEAF_NODES: t mod 2 == 0}:
	l[t] = d[t/2];
	
subject to eq12_4 {t in LEAF_NODES diff {T} : t mod 2 != 0}:
	l[t] =  d[a_l_max[t]];
	
	
	