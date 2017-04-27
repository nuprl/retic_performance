;; This file was generated by the `with-cache` library on 2017-04-26
(((stats ("anova.py" "d49acb9135a64ba7458baa468dd0b4b5") ("central_tendency.py" "9bf63d51cfdca94179f96154471df4dc") ("correlation.py" "c6fe1655f68efb7a6dc10c2e09a34856") ("frequency.py" "d6a4131e0b0cfcd99f547c00fadce58f") ("inferential.py" "cecd3656dee55438211cfadaec3cc0df") ("main.py" "86b0f92e4acc98c922bfbde2382f9df2") ("moment.py" "36799bd5c984f821aca1547cb45b43ff") ("probability.py" "59fbe582f37b1c7c31e3b1774d3cb00c") ("pstat.py" "112f091719fe4c9f19ba427195677c08") ("support.py" "a707dcc00e939a266385d2325ce6280d") ("trimming.py" "59658a4531db5f9bfc0b0b70e313759d") ("typed_math.py" "c1b3983f85ccfc44270ff04a3dd33505") ("variability.py" "8941c4932675d25379aa1d90d4364026"))) (3) 0 () 0 () () (f python-info stats (c (f module-info anova (c (f function-info F_oneway (c (f field-info lists (u . "List(List(float))"))) (u . "[float,float]")) c (f function-info F_value (c (f field-info ER (u . "float")) c (f field-info EF (u . "float")) c (f field-info dfnum (u . "float")) c (f field-info dfden (u . "float"))) (u . "float"))) ()) c (f module-info central_tendency (c (f function-info geometricmean (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info harmonicmean (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info mean (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info median (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info medianscore (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info mode (c (f field-info inlist (u . "List(float)"))) (u . "[int,List(float)]"))) ()) c (f module-info correlation (c (f function-info pearsonr (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "[float,float]")) c (f function-info lincc (c (f field-info x (u . "float")) c (f field-info y (u . "float"))) (u . "float")) c (f function-info spearmanr (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "[float,float]")) c (f function-info pointbiserialr (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "[float,float]")) c (f function-info kendalltau (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "[float,float]")) c (f function-info linregress (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "[float,float,float,float,float]"))) ()) c (f module-info frequency (c (f function-info itemfreq (c (f field-info inlist (u . "List(float)"))) (u . "List(List(float))")) c (f function-info scoreatpercentile (c (f field-info inlist (u . "List(float)")) c (f field-info percent (u . "float"))) (u . "float")) c (f function-info percentileofscore (c (f field-info inlist (u . "List(float)")) c (f field-info score (u . "int"))) (u . "float")) c (f function-info histogram (c (f field-info inlist (u . "List(float)")) c (f field-info numbins (u . "int")) c (f field-info defaultreallimits (u . "[float,float]"))) (u . "[List(int),float,float,int]")) c (f function-info cumfreq (c (f field-info inlist (u . "List(float)"))) (u . "[List(int),float,float,int]")) c (f function-info relfreq (c (f field-info inlist (u . "List(float)"))) (u . "[List(float),float,float,int]"))) ()) c (f module-info inferential (c (f function-info ttest_1samp (c (f field-info a (u . "List(float)")) c (f field-info popmean (u . "int"))) (u . "[float,float]")) c (f function-info ttest_ind (c (f field-info a (u . "List(float)")) c (f field-info b (u . "List(float)"))) (u . "[float,float]")) c (f function-info ttest_rel (c (f field-info a (u . "List(float)")) c (f field-info b (u . "List(float)"))) (u . "[float,float]")) c (f function-info chisquare (c (f field-info f_obs (u . "List(float)"))) (u . "[float,float]")) c (f function-info ks_2samp (c (f field-info data1 (u . "List(float)")) c (f field-info data2 (u . "List(float)"))) (u . "[float,float]")) c (f function-info mannwhitneyu (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "[float,float]")) c (f function-info tiecorrect (c (f field-info rankvals (u . "List(float)"))) (u . "float")) c (f function-info ranksums (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "[float,float]")) c (f function-info wilcoxont (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "[float,float]")) c (f function-info kruskalwallish (c (f field-info args (u . "List(List(float))"))) (u . "[float,float]")) c (f function-info friedmanchisquare (c (f field-info args (u . "List(List(float))"))) (u . "[float,float]"))) ()) c (f module-info main (c (f function-info print_noop () #f)) ()) c (f module-info moment (c (f function-info moment (c (f field-info inlist (u . "List(float)")) c (f field-info moment (u . "int"))) (u . "float")) c (f function-info variation (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info skew (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info kurtosis (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info describe (c (f field-info inlist (u . "List(float)"))) (u . "[int,[float,float],float,float,float,float]"))) ()) c (f module-info probability (c (f function-info ex (c (f field-info x (u . "float")) c (f field-info BIG (u . "float"))) (u . "float")) c (f function-info chisqprob (c (f field-info chisq (u . "float")) c (f field-info df (u . "int"))) (u . "float")) c (f function-info erfcc (c (f field-info x (u . "float"))) (u . "float")) c (f function-info zprob (c (f field-info _z (u . "float"))) (u . "float")) c (f function-info ksprob (c (f field-info alam (u . "float"))) (u . "float")) c (f function-info fprob (c (f field-info dfnum (u . "float")) c (f field-info dfden (u . "float")) c (f field-info F (u . "float"))) (u . "float")) c (f function-info betacf (c (f field-info a (u . "float")) c (f field-info b (u . "float")) c (f field-info x (u . "float"))) (u . "float")) c (f function-info gammln (c (f field-info xx (u . "float"))) (u . "float")) c (f function-info betai (c (f field-info a (u . "float")) c (f field-info b (u . "float")) c (f field-info x (u . "float"))) (u . "float"))) ()) c (f module-info pstat (c (f function-info abut (c (f field-info source (u . "Dyn")) c (f field-info tgt (u . "Dyn"))) (u . "List(Dyn)")) c (f function-info simpleabut (c (f field-info source (u . "List(Dyn)")) c (f field-info addon (u . "List(Dyn)"))) (u . "List(Dyn)")) c (f function-info colex (c (f field-info listoflists (u . "List(List(Dyn))")) c (f field-info cnums (u . "Dyn"))) (u . "Dyn")) c (f function-info linexand (c (f field-info listoflists (u . "List(List(Dyn))")) c (f field-info columnlist (u . "Dyn")) c (f field-info valuelist (u . "Dyn"))) (u . "List(List(Dyn))")) c (f function-info recode (c (f field-info inlist (u . "Dyn")) c (f field-info listmap (u . "Dyn")) c (f field-info cols (u . "Dyn"))) (u . "List(Dyn)")) c (f function-info unique (c (f field-info inlist (u . "List(float)"))) (u . "List(float)"))) ()) c (f module-info support (c (f function-info sum (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info cumsum (c (f field-info inlist (u . "List(int)"))) (u . "List(int)")) c (f function-info ss (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info summult (c (f field-info list1 (u . "List(float)")) c (f field-info list2 (u . "List(float)"))) (u . "float")) c (f function-info sumdiffsquared (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "float")) c (f function-info square_of_sums (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info shellsort (c (f field-info inlist (u . "List(float)"))) (u . "[List(float),List(int)]")) c (f function-info rankdata (c (f field-info inlist (u . "List(float)"))) (u . "List(float)"))) ()) c (f module-info trimming (c (f function-info trimboth (c (f field-info l (u . "List(float)")) c (f field-info proportiontocut (u . "float"))) (u . "List(float)")) c (f function-info trim1 (c (f field-info l (u . "List(float)")) c (f field-info proportiontocut (u . "float"))) (u . "List(float)"))) ()) c (f module-info typed_math (c (f function-info pow (c (f field-info x (u . "float")) c (f field-info y (u . "float"))) (u . "float")) c (f function-info sqrt (c (f field-info x (u . "float"))) (u . "float")) c (f function-info exp (c (f field-info x (u . "float"))) (u . "float")) c (f function-info abs (c (f field-info x (u . "float"))) (u . "float")) c (f function-info fabs (c (f field-info x (u . "float"))) (u . "float")) c (f function-info log (c (f field-info x (u . "float"))) (u . "float")) c (f function-info round (c (f field-info n (u . "float")) c (f field-info d (u . "float"))) (u . "float"))) ()) c (f module-info variability (c (f function-info obrientransform (c (f field-info args (u . "List(List(float))"))) (u . "List(List(float))")) c (f function-info samplevar (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info samplestdev (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info cov (c (f field-info x (u . "List(float)")) c (f field-info y (u . "List(float)"))) (u . "float")) c (f function-info var (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info stdev (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info sterr (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info sem (c (f field-info inlist (u . "List(float)"))) (u . "float")) c (f function-info z (c (f field-info inlist (u . "List(float)")) c (f field-info score (u . "float"))) (u . "float")) c (f function-info zs (c (f field-info inlist (u . "List(float)"))) (u . "List(float)"))) ()))))
