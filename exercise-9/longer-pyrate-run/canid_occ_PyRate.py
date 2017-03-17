#!/usr/bin/env python
from numpy import * 


data_1=[array([14.235679,14.979582,14.955892,9.435919,14.855906,9.663919,15.167357,14.542908,14.97589,13.781019,13.845433,9.784426,11.326821]),
array([17.608859,19.84682,14.531149,15.918081,14.065031,15.107856,15.18819,13.967939,15.45636,13.973008,15.517114]),
array([13.990866,16.148402,14.510826,14.987342,13.546624,11.366474,14.210133,14.661719,13.666854,13.810984,9.358939,12.710877,14.484385,14.35591,15.661905,13.336677,18.938779,14.414694,14.720688,15.089565,10.552461,13.073296,13.767345,10.833292,15.796911,14.758294,10.303425,13.900391,9.549202,15.474772,14.912402,16.18086,13.668195,14.382701,15.646814,15.065452,13.222875,14.889713,14.00097,15.394944,14.388532,7.566509,14.446247,10.384717,13.597579,22.082865,15.074682,14.122151,8.807679,19.573067,15.789666]),
array([14.599344,15.696255,14.253093,6.439497,15.595612,15.121613,15.350013,15.272467,14.706465]),
array([14.47126]),
array([11.991107,15.948262,11.201394,12.977813,12.759895,12.166377,13.243905,5.452405,14.81736]),
array([11.63203,10.635888,11.260159,13.553664,6.354937,10.53537,7.63261,18.990519,12.133954,12.950432,10.375962,11.425459,11.188134,19.8918,11.164639,10.644446,7.002738,22.017494,8.51869,13.125375,17.113706,13.043748,11.566795,12.638961,10.374224,10.591813,11.998631,13.47414,8.211136,12.050827,10.787717,7.492779,11.719519,10.774019,12.330425,10.544159,10.810071,11.900199,5.294814,11.092224,12.132621,11.399491,10.307133,11.710521,12.807923,12.700218,12.566881,13.419805,10.886543,10.415228,10.322895,12.635827,12.761859,5.675397,12.09691,9.643651,13.180802,10.533235,12.586363,8.457308,11.058897,13.028407]),
array([18.083076]),
array([5.316283]),
array([1.40271,1.198337,0.049474,0.05685,0.113638,0.113933,0.00963,0.060922,0.001323,0.00384,0.005436]),
array([24.987739]),
array([31.106281,31.922278,24.306905,21.012468,26.532105,25.97123,26.529411,29.230068,25.238718,30.578644,26.607004,21.560489,27.680596,27.534975,27.421772,27.572542,27.188396,29.051896,27.934878,29.741046,29.488833,29.961917,27.006682,27.323323,24.103635,26.660573,29.340624]),
array([32.38104,31.315822,32.822779,31.776751,32.792441,32.282841,32.135504,28.220231,30.167056]),
array([23.283936,20.979376,22.941238,18.353847,18.067101,15.533598,14.108755,10.802736,10.665926,13.041137,15.793997,10.775418,14.597274,10.481701,14.670887,11.182249,11.596329,10.878828,9.827102,13.140847,12.238435,15.768755,14.968471,13.072257,19.080146,13.651825,7.661789,14.668098,18.61074,6.482605,5.530439,12.369578,10.392342,19.515,19.202075,18.459893,7.12685,20.421612,20.299747,18.845808,19.855472,20.197766,18.031195,18.175145,8.087572,14.764747,14.356078,13.500564,11.727241,10.702345,13.32191,12.913253,11.438629,13.033458,14.904585,14.053581,13.822534,17.096429]),
array([7.813177,6.970304,6.931549,6.414063,9.685784,5.561249,5.533218,4.910633,4.717536,4.931633,5.723773,9.923917,9.608453,9.610611,11.810076,7.856213,6.458831,6.665896,10.138433,4.985006,10.147111,5.307772,2.174404,2.213177,2.500142,3.495705,1.999017,3.256544,1.921026,2.273041,3.307974,4.287288,8.926689]),
array([2.745301,2.093635,2.790581,1.85218,2.687327,2.257042,3.211972,4.011599,3.379707,4.770146,3.071989,4.351302,4.207818,4.409741,4.557463,3.148971,3.277314,3.54836,2.65814,1.878779,4.658025,2.546387,2.02004,4.48977,1.995609,2.784488,3.257655,4.793278]),
array([3.870601]),
array([5.207136,10.162239,7.732824,7.001121,16.064337,7.862625,14.089411,5.00751,8.61236,4.353734,3.574715,2.809763,2.478458,3.150645,4.575851,2.420738]),
array([12.386994,5.720748,12.550302,12.324758,11.333928,12.250566,10.176041,11.209583]),
array([8.346534,6.899495,3.618692]),
array([8.790768,6.748534,8.687273]),
array([7.596932,7.439803,12.966279,6.830039,9.504435,9.893788,10.052938,13.262091,15.117957,10.114588,16.79238,8.104989,13.082384,8.20457,7.17253,8.686835,13.172848,11.052104]),
array([5.430068,11.517755,9.870029,5.540495,7.173644,8.231256,10.141292,5.457191,8.841225,9.9087,5.054527,14.286582,17.781148,10.236586,19.090023,9.53474,20.423329,6.015242,17.073489,22.185697,13.42399,7.875751,5.408015,8.628963,7.375301,5.835503,6.812034,8.986095,8.716952]),
array([23.970075]),
array([36.519303,36.494474,35.762905,33.823571,31.063805,29.836935,26.083933,22.497967,23.49632,22.803363,20.433709,25.260907,26.195658,30.508284,21.206208,24.863059,23.099891,16.248009,20.291601,17.995322,13.462917,10.491987,7.236775,14.235925,11.137052,11.064012,11.109006,5.864959,9.838777,10.382022,13.860917,14.041307,7.107496,14.734963,16.626458,4.949051,13.678204,15.221465,14.030923,19.840555,13.886355,17.629155,15.750393,14.656788,14.449327,5.333067,18.939213,4.029075,2.627032,4.250057,3.96438,2.510981,4.506882,3.435865,3.169276,2.386814,4.285556,1.348202,1.250552,1.527842,0.752991,1.751579,1.354939,1.501981,5.166847,7.067571,7.236647,13.642246,2.775388,1.09325,0.08842,3.334749,2.893245,1.101056,0.102372,0.801836,1.408021,0.581358,0.688204,0.551303,0.307392,0.677006,15.332254,8.264205,16.366502,4.853117,12.641452,5.446282,0.486281,1.646044,2.987864,2.676351,24.025997,3.50131,4.25383,7.248144,4.981675,0.284385,19.807974,0.312169,6.669118,0.731239,1.903598,4.020208,0.05474,0.04537,0.022965,1.990618,0.028446,0.118772,0.122096,0.081973,0.087574,5.688133,0.867304,2.921727,0.040287,0.029211,0.055578,28.489558,24.270957,20.530754,26.780483,5.450946,2.151017]),
array([25.740513,7.730652,7.407517,13.275959,11.113887,11.871113,11.804021,5.568607,15.851353,5.684244,13.157844,12.349625,12.881574,10.090973,11.735018,7.727245,7.318703,11.409323,13.211674,11.909621,12.981165,13.528118,13.354593,12.004535,12.554878,3.089085,0.021185,0.019858,0.31561]),
array([9.195263,8.794319,6.964754,2.035201,2.915406,3.303171,3.696005,2.496523,2.399775,1.926424]),
array([6.810717,7.729511,8.190483,4.857299,3.331224,3.989757,1.85527,2.897755,3.108152,2.637386,0.906786,0.59107,1.474233,0.963887,1.627762,0.371969,0.686574,0.035065,0.688133,0.842576,0.727136,1.771255,1.272316,0.081113,2.903434,3.352191,2.926156,2.603418,2.191061,2.925464,3.394312,3.106909,3.797275,2.755539,3.087676,1.081485,0.006923,0.294174,0.122732,2.815502,4.391335,0.290932,0.009355,0.002493,0.003751,1.486481,0.005476,0.003709,0.001319,0.43165,0.292201,2.130606,1.410699,0.828699,0.007184,0.002734,0.00264,0.005637,1.299709,0.008338,1.725729,0.269838,0.005473,14.77625,3.145073,3.730944,0.755748,4.975326,4.314791,2.097485,1.687582,2.56175,0.849502,2.188782,2.363766,0.176665,0.242203,0.16411,4.85832,0.04038,0.691044,3.653595,3.83108,2.363471,0.876858,0.444696,1.70921,0.812395,1.770181,2.411322,1.296195,1.48525,1.42028,1.352702,1.867811,1.427411,1.009919,1.211524,2.074326,1.677863,1.336812,0.468305,2.655805,0.740541,0.347104,2.549271,1.544812,2.769377,2.688852,2.838253,2.867625,1.376004,2.269321,1.443461,2.189315,0.470933,0.503747,4.363505,4.060326,1.975658,0.986458,0.806839,2.141573,1.545524,2.451938,0.012874,0.205913,1.108428,3.691763,4.744463,4.880707,0.878728,0.78489,2.978622,4.247725,3.798718,4.992528,0.632159,1.891598,2.36455,3.978405,3.97406,0.566647,7.500671,5.219275,2.245603,0.85614,1.025569,2.416193,2.011918,2.08892,0.655603,0.886696,0.168275,0.40328,0.371168,0.689795,0.451192,1.181401,0.288632,0.568295,0.188127,1.177577,2.365506,2.443079,3.932487,3.135922,2.705998,2.526073,2.518788,1.41061,0.918586,2.301875,0.681286,0.347806,0.176785,0.343152,0.685152,0.543631,0.170102,0.653428,0.386743,5.108612,4.010969,1.874742,0.954488,1.830509,0.317599,2.493635,0.638387,1.938246,1.507513,4.476893,4.360794,3.76077,4.081114,3.616618,3.508508,3.745462,4.258545,4.874468,2.448724,0.817831,1.335755,0.6184,0.102684,0.043133,0.04345,2.114273,1.625394,0.01299,0.029828,0.008698,0.123934,1.302863,3.598705,3.219487,2.190754,2.129307,2.255006,0.021004,0.020284,0.046348,0.078861,0.125499,0.100402,0.548516,0.653282,14.601373,4.612844,0.059175,0.081967,2.246444,0.074024,3.325564,0.021736,0.009214,1.616359,0.193865,0.011222,0.001871,0.009377,0.007375,2.457064]),
array([0.452255,0.589283,0.512918,0.115795,0.076648,0.209826,1.15659]),
array([0.004542,0.006715,0.249527,0.75477,3.059652,1.839204,0.609397,0.473057,0]),
array([0.226043,1.427663,0]),
array([0.781915]),
array([3.800991,1.689257,1.213394,1.573063,0.610942,1.014814,1.772365,1.613455,1.009343,1.796808,0.554975,1.762015,0.973244,0.044878,1.782052,1.080002,0.459888,0.925378]),
array([0.001794,1.674288,0.881856,1.232766,0.989509,0.010226,1.395254,0.315022,2.315765,3.155599,0.780699,0.524479,0.17483,0.007601,0]),
array([1.220167]),
array([0.603452,0.383448,0.666876,1.072663,1.068849,1.00736,0.883914,1.267031,0.857731,0.284606,1.011486,0.102801,0.45506,1.123297,1.207241,0.087284,0.073403,0.110185,0.109767,0.034985,0.075678,0.113751,0.166435,0.050701,0.012354,0.106681,0.051343,0.062571,0.099472,0.66695,0.196536,1.164551,0.084,0.029736,0.112513,0.057845,0.02743,1.926255,0.071549,0.01563,0.079634,0.021337,2.470139,0.024004,0.080936,0.203911,0.087039,0.042335,0.043061,0.056909,0.543679,0.037986,0.09419,0.118732,0.117478,0.121899,0.066609,0.069541,0.078359,0.19579,0.117591,0.124831,0.037846,0.053274,0.014838,0.08787,0.044624,0.075178,0.102299,0.746431,1.563659]),
array([4.006503,4.135473,0.989312,0.962399,1.279217,0.67767,4.290086,1.459394,1.729663,0.885029,1.283124,1.104913,2.076459,1.119444,0.676827,0.843525,0.599349,1.753138,2.74742,3.328121,2.520673,4.779824,1.769179,0.883087,1.184852,0.68215,1.76884,0.302287,1.524299,13.631704,3.136862]),
array([0.010698,2.219093,0.001193,0.00242,0.004511,0.010418,0.010845,0.00797,0.009799,0.080985,0.006689,0.001876,0.011301,0.001545,0.001663,0.008581,0]),
array([7.713719,5.805691,8.700635,6.763234,1.829646,4.313148,2.105729,4.31386,4.303054,2.782747,1.959088,4.687417,5.639662,7.78822,7.257939,5.714363,1.870994]),
array([1.057959,3.51793,4.713331,4.460678,3.931668,4.796958,4.396292,2.337242,3.532727,4.199175,0.384382,0.785315,1.15442,0.746312,0.852382,1.55385,0.528687,0.908519,1.300876,1.138039,1.516369,1.473634,1.679472,0.376944,0.979005,0.946737,1.53916,0.832145,0.552964,1.242122,0.862667,0.725285,1.417432,0.386612,0.469412,1.397971,0.323975,1.200718,0.233378,1.068488,0.743689,1.541632,0.591369,1.728732,1.693909,0.049618,0.055063,0.040653,0.07776,0.045088,0.079571,0.05511,0.058862,0.064861,0.025236,0.070845,0.028534,0.124078,0.034181,0.105962,0.001032,0.044141,0.101542,0.023077,0.010427,1.967919,0.089936,0.058068,0.11657,0.077139,0.119499,0.039339,0.054461,0.078647,0.121134,0.092155,0.017593,0.095494,0.020591,0.03065,0.119982,0.091265,0.29334,0.099516,0.063122,0.045078,0.050824,0.012689,0.042668,0.305606,0.571783,2.230963,1.20426,1.704338,0.008078,0]),
array([5.143721,4.203465,3.38963,1.846542,2.600899,3.872525,4.200777,4.043412,4.717833,2.849271,2.27789,3.187165,4.768396,3.666529,3.525363,2.331306,4.79943,1.863769,2.966892,3.663593,2.478556,3.739686,2.333083,4.831371,4.761514,2.779088,3.718891,3.566072,3.406489,2.259247,2.347611,2.665014,2.321502,3.412176,4.455092,0.092835]),
array([1.595649,1.104697,1.377603,1.516458,0.082438,0.117617,0.072114,0.108506,0.111808,1.075321,1.73903,1.322466,0.127074,0.364045,2.908745,1.537642,1.921419,0.243671,0.545199,1.018417,0.732886,0.394886,0.652008,0.021776,0.125055,0.796159,0.71473,0.343925,0.521624,0.385622,0.105345,0.064412,0.016847,0.034672,0.0373,1.322443,0.441411,0.246074,0.583084,0.358951,0.380343,1.592668,0.26919,0.07591,0.742873,0.202065,0.217283,0.219866,0.065996,0.22719,0.658462,0.179107,0.60703,0.409658,0.477401,0.297985,0.864331,0.470619,0.233114,0.23776,1.590848,0.336972,0.010976,0.00836,1.470747,0.566643,3.241057,0.09798,0.11027,0.039659,0.057588,0.121422,0.042854,0.093341,0.088092,0.045696,0.093726,0.122551,0.038119,0.068074,2.09038,0.020443,0.044144,0.020329,0.069381,0.028598,0.037646,0.063977,0.067634,0.232946,0.15356,0.075198,0.125454,0.035002,0.009883,0.011442,0.002183,1.513755,0.109543,0]),
array([1.044998,2.250837,4.941531,0.005077,0.004409,3.192165,2.184465,1.339032,3.155815,1.826825,0.811593,0.005438,2.104357,0.633788,0.005159,1.863133,0.391506,1.33284,1.514494,0.569451,0.261315,0.185469,1.037679,2.471359,0.963306,0.949366,1.40208,0.450425,1.346412,2.043795,5.236082,0.733138,0.523216,0.771092,1.249663,2.121079,1.151605,3.988328,0.101384,3.62551,2.033339,1.018961,0.004316,0.046116,0.117922,1.362869,2.093336,0.113924,0.067372,0.240466,1.544235,0.191281,0]),
array([1.983023]),
array([3.462759,3.997683,3.247195,1.573802,0.513879,0.906671,0.080279,0]),
array([2.497677]),
array([13.829651,12.217128,14.855436]),
array([11.774869,12.149535,15.420469,15.361215,15.394687,14.302628,15.792278,14.383219,15.050947,15.784219,10.576373,14.441518,15.004044,14.939694,11.647809,15.140451,14.604194]),
array([7.330808,5.384263,4.933553]),
array([10.414831,11.23565,10.860026,10.597072,13.242979,11.026893,11.322885,13.060747,11.036158,13.331198,7.178678,13.147774]),
array([12.477287,11.013939,11.478725,10.391007,11.212274,12.695921,10.353277,12.623962,5.561109,14.519102,14.841203]),
array([3.840252,4.640356]),
array([7.71139,2.698202]),
array([0.007297,0.067749,0.012402]),
array([47.716987]),
array([1.663792]),
array([1.974859,2.177556]),
array([1.883434,3.363562]),
array([30.402154]),
array([28.122107,27.870901,26.272494,22.431993,23.547774,19.591258,12.531315,27.036386,25.96541,25.233946]),
array([27.411967,24.025358,20.485969,21.412874,23.120875]),
array([1.33517]),
array([0.691939,0.332672,0.324313,0.734096,0.293087,0.568272,0.535042,0.446193,0.586178,0.382328,0.285106,0.050993,0.684682]),
array([0.573747,0.64104,0.018083]),
array([20.518687,24.182695,20.512069,22.685005,22.770236,23.684137,17.828174,18.681866,19.105856,19.343706,18.499466,16.227108,18.830767,16.923933,19.175603,19.167626,16.029024,19.55943,19.011217,19.451395,17.452771,18.071279,16.920096,18.294383,18.619796,16.221138,19.277758,16.182574,14.464805,18.159943,18.121883,16.30511,16.479719,20.002551,17.376156,19.028796,17.426979,17.57847,16.702567,19.283173,17.049965,20.057894,15.797534,13.863706,14.677009,14.602946,23.744919]),
array([17.008974,16.613262]),
array([15.139223,16.500048]),
array([21.793739]),
array([27.868036,23.234458,24.246746,29.665538,29.786357,24.427965]),
array([23.494157,21.186227,24.450062,29.255778]),
array([26.504703,30.590958,28.490784,30.684932,26.642993,28.670123,28.996602,26.63743,27.651485]),
array([18.906781,20.280316]),
array([13.35399,13.752405,11.443695]),
array([10.452982,10.483252,7.501449,10.471232,12.175456,12.897541,11.275449,11.334926,12.997428,12.809199,14.850935,10.341694,11.085049,12.747572,9.093567,6.266891]),
array([15.86486,14.336296,15.411231]),
array([14.168404,20.095764]),
array([14.805065,15.550147,14.400545,15.309998,15.823628,15.759167,15.216159]),
array([11.660113,12.491786,11.658007]),
array([13.623371]),
array([27.816771]),
array([32.82181,31.123241,31.350198,31.956463,32.878324,33.172156,31.635906,32.502186,21.748159,30.477208,27.405239,29.902227,20.698433,27.950793]),
array([29.223481,30.835232,30.58298,41.776867,36.977739,36.916672,36.169508,52.938746,32.162121]),
array([35.705315,36.806282,36.874392,37.453291,37.385206]),
array([1.618173,0.017406,0.250469,0.192911,0.076296,1.120372]),
array([0.024168,0.15366,2.548235,0.05059]),
array([23.234984]),
array([18.128089,20.247981,17.177245,18.327528,19.722583,17.472232,16.241325,19.581085]),
array([20.611033,21.243041,23.167448,21.83276,24.484806,20.528245,22.978705,21.689627,25.043773,22.06781,21.010716,23.59057,21.389145,23.398564,23.082995,23.07781,21.714794,20.775206,20.678616,24.3956,21.290751,16.394613,16.012337,19.353727,18.528702,19.332258,17.961639,17.909288,18.113789,18.76609,25.805799,21.18223,18.626583]),
array([0.007083,0.007334,0.017466,1.730972,0.004204,0.004396,1.639445,0.079528]),
array([0.090888,0.11494,0.074631,0.118748,0.100812,0.095186,0.592393]),
array([0.928178]),
array([0.314036]),
array([32.660319,27.251333]),
array([24.392375]),
array([19.316122,19.32239,20.347977]),
array([32.744398,24.994789,21.375642,23.53134,30.294008,25.055246]),
array([20.852829]),
array([28.382951,20.849343,25.871593,27.122983,22.668209,23.390407,23.956295,23.757612]),
array([30.198177,25.636136,27.580526,25.04017,24.818496,30.500955,26.351039,29.405317,23.330346,24.933989]),
array([24.643114,28.973025]),
array([6.998525,5.497545,13.323606,5.106602,7.363921]),
array([5.043229]),
array([17.477395,8.855559,7.860114,12.289124,5.352982,6.461691,6.532287,10.791305,12.519028,10.41343,21.829912,4.972393,6.722371,13.322213,13.056681,13.571778,8.462201,10.769132,6.490419,12.007952,10.472092,12.265598,9.968843,7.003329,9.451283,11.516829,13.287941,18.981002,5.731908,9.932625,10.84966,16.307264,12.523117,12.533475,10.425717,6.56683,10.439474,9.599918,11.371481,9.072842,9.386419,9.17864,12.308423,9.871365,5.809062,5.338589,13.502955,12.282768,15.992446,12.909792,6.767197,13.248405,10.251521,9.549861,12.545427,13.024387,9.384832,10.6181,8.18779,16.834634,13.299592,10.700247,10.929989,10.506154,14.75959,7.94772,7.360415]),
array([12.124022,9.040099,9.627241,12.510115,13.335492,11.737611,10.52711,13.027029,6.072303,9.668882,12.909644,12.163793,11.742496,12.239334,11.26671,11.665148,13.375689,11.887173,10.673031,11.428294,12.687691,13.242402,12.230128,13.563515,12.540147,11.673893,11.234432,8.341523,8.833759,21.657444,10.185691,12.249285,13.434306,6.667611,11.873108,7.774475,12.288815,12.719957,13.52133,8.902369,12.080248,8.548331,13.29845,12.015976,20.510861,10.065158,6.703868,12.16793,12.787031,12.389406,13.248972,13.119136,13.55289,7.503401,13.032349,13.724655,14.281565,15.221109,15.396081,15.881252,14.218672,13.462783,10.508054,13.52834,6.343892,6.399943,12.68104,10.765707,6.013249,12.548382,12.033646,12.610681,13.033449,14.359658,9.244512,6.673031]),
array([6.228539,3.627908,7.938154]),
array([4.971832,6.402059,10.281663,9.857721,8.439566,5.89353,8.439002,5.775628,7.869591,17.461994,7.433811,6.657493,4.961393,7.074057,8.179689,7.874586,9.052378,2.092502,4.299611,8.145315,5.643579,8.712498,10.288362,9.983096,5.79825,6.410093,8.795967,4.963797]),
array([10.505961]),
array([14.961928,17.688857,18.036165,14.583989,14.741507,13.645592]),
array([19.782085]),
array([15.64741,13.557096]),
array([42.508877,38.692012,34.303351,36.502955,34.65186,34.649974,34.838222,34.292773,35.375656,34.501912,35.807894,34.351242,35.636698,34.328739,35.937501,35.677472,36.509671,33.407683,33.466643,33.65499,33.886748,33.406691,33.649022,33.372469,33.415698,33.808047,33.362798,25.074314,30.840198,32.722341,32.797713,32.56861,31.310742,28.555329]),
array([33.846188,33.360374]),
array([39.612848,34.734317,35.227392,35.982192,35.105708,35.534651,36.536134,36.446442,34.983459,34.156709,36.136117,33.950818,35.145656,34.573173,36.560238,36.334913,37.085778,35.244134,34.704038,35.970035,34.627936,35.716046,36.621817,33.950394,33.951268,34.460345,35.12512,35.536427,35.599923,35.570782,36.169816,33.952783,34.661128,36.251894,35.538401,35.880257,35.662946,36.358424,33.417259,33.877972,33.716608,33.335179,33.413112,33.33402,33.637778,33.700314,33.898449,33.413092,33.72626,33.714835,33.673759,33.383566,33.872742,33.436554,33.877179,33.548918,33.748808,33.425858,33.600842,33.397836,33.619286,33.603594,33.530404,33.715733,33.74213,33.390361,33.780568,33.760063,33.599717,33.549609,33.581715,33.672154,33.524127,33.573164,33.600081,33.396892,33.58532,33.493916,33.685546,33.630006,33.465467,33.643449,33.453537,33.563962,33.616783,33.48231,33.304389,33.748064,33.410605,33.61228,33.460927,33.348449,33.342499,33.440575,33.435276,33.455824,33.378651,33.75904,33.747701,33.696273,33.603519,33.705932,33.712318,33.743133,33.448932,33.508571,33.621549,33.608663,33.459094,33.315134,33.852306,33.343601,33.351938,33.883496,33.319191,33.611187,33.51232,33.701412,33.897925,33.799939,33.404249,33.819981,33.362216,33.217551,31.65196,33.086821,31.776256,30.824902,32.137196,32.82759,34.038055,35.845656,33.470058]),
array([27.656974,23.000854]),
array([20.493239,21.323173,15.483717,14.497575,15.374894,11.061626,11.45204,15.83411,15.712289,11.307569,10.29652,27.210264,15.681956]),
array([20.686302]),
array([26.769174,29.58163,30.332825,29.480198,21.54527]),
array([23.938865,23.263812,23.248032,23.918545,22.415495,21.551536]),
array([14.175974,16.157029,16.008591,17.093916,17.664653,24.503269,16.953247,19.049284,20.365655,19.103761,19.955573,17.984917,20.188279,18.169456,14.158483,13.881027,14.301476,14.826606,15.864774,14.245937,14.788357,14.513012,15.53671,14.433422]),
array([11.750722,13.188291,13.446919,11.04548,11.806743,10.730647,12.429172,12.033943,12.870859,4.984565,12.480034,10.691112,11.498179,13.271555,13.384814,10.940421,13.273795,11.496247]),
array([23.337504]),
array([13.15697]),
array([13.892797,15.861479,11.994828,13.417636,15.932314,13.896486,13.439937,15.635278,14.940732,13.960061,14.010255,15.800289,15.705712,15.288139,15.010048,15.376728,14.509916,13.403401,15.712559,15.246095,15.334263,11.88674,15.748114,11.523433,13.078816,13.895586,11.121637,11.808093,12.799176,15.188735,15.730949,13.664583,15.6545,15.580598,13.821625,11.295292,12.667747,10.306937,12.61694,13.471554,15.583765,12.718125,13.726595,9.496779,7.714591,17.678488,11.099332,6.181183,8.494502,11.408708,10.844618]),
array([21.942601,20.117614,21.719251,19.265338,19.52587,30.161271]),
array([0.591081,2.116145,0.842858,2.938445,2.535699,0.454511,2.923537]),
array([0.005266,1.545177,1.355213,0.162346,0.876887,0.983294,0.326578,1.286595,1.693522,0.067983]),
array([29.850003]),
array([27.710736,23.394796,21.469137,30.123016,23.348144]),
array([29.983188,26.366191]),
array([33.809502,31.677753,32.511997,31.238756,32.269547,31.932453,31.447063,32.30519,33.254884,32.363906,31.031015,31.541985,32.472399,32.406424,28.103353,26.93023,26.931235,27.938195,28.876691,25.894853,23.618812]),
array([6.474515]),
array([13.484221,9.841053,20.671231]),
array([7.602341,10.012386,15.186272,9.708281,11.149827,20.69961]),
array([18.211564]),
array([16.293405,19.395381,18.145728,18.27028,19.396801,18.280604,17.082531,19.609819,19.028182,19.527004,18.030434,19.425376,16.032122,19.432238,19.146243,19.818513,20.067873,19.401228,16.533261,17.081257,19.913512,22.304494,19.151443,19.13079,20.166547]),
array([20.398034,15.671051,20.033351,17.375453,17.339572,20.258417,19.85636,17.891818,15.056804,7.177807,9.282693,20.775918,14.117946,14.7879,14.64773,14.322204,14.583907,15.420967,14.018993,6.924859,15.703032,15.19907,15.239999,15.330232,14.263697,15.733377,15.559748,14.506656,14.774437,15.316303,14.392078,14.622068,15.46976,15.424325]),
array([45.487207]),
array([4.366953,1.990996,4.121902,3.038334,0.841152,3.106635,2.991348,2.472165,2.886685,5.279109,5.28202,2.669931,1.950628,4.58333,3.354391,3.09036,2.024452,2.769371,6.626166,4.070104,3.488877,3.246263,4.351239,2.678459,2.120478,1.829695,2.119538,2.114637,2.931049,2.301393,4.018852,2.209642,1.991312,4.679623,5.185607,5.258218,1.365544,1.346015]),
array([3.215644,2.967694]),
array([0.077713,0.069852,0.050379]),
array([21.707727,18.026662]),
array([15.490781,17.169448,17.791565,17.38266,16.633555,17.645442,19.265121,19.173944,16.054159,14.177981,15.05309,14.792197,13.723752,13.89073]),
array([19.785442,20.061049,19.830936,19.434746]),
array([33.544902,31.997986]),
array([19.20703,16.167991,18.858685]),
array([30.839002,32.762423,29.564156]),
array([27.215569]),
array([21.449831,28.649327,30.197169,29.936637,28.327975,28.090364]),
array([33.562289,33.618463]),
array([1.247548,0.271495,2.729819,0.255055,1.210508]),
array([0.00653,0.008313,0.298651,1.856724,0.795862,2.182295,0.099869]),
array([31.018313,31.365201]),
array([31.708157,32.286308,31.5832,33.143916]),
array([17.737831,17.175235,22.681507,16.74495,19.016348,7.254503,19.696836,17.670777,19.593548,16.805245,15.951681,14.006346,6.072497,19.661282,14.235948,14.795015,15.81807,15.656178]),
array([16.034734,18.486559,18.556647,14.726419,17.302499]),
array([24.1124,28.454153,26.775533,20.448249,29.126049,28.19195,20.702679,24.906493,22.762203,20.706598,22.805979,24.861077]),
array([24.610886,22.938442]),
array([20.866665,23.156593,24.227988,21.927677,22.537519,21.999738,23.229663,22.279854]),
array([11.791129,12.702137,11.565084,4.940507,11.653218,13.075423,11.358565,11.215245,13.396119,12.561083,11.286439,12.963459,13.375444,11.710245,11.063395,11.413181,10.554692,15.835882,10.883357,12.094193,14.769458,10.478212,10.915075,11.24042,11.360634,11.318097]),
array([14.878536,14.23811,14.758243,13.767509,14.582121,15.115178,15.322018,15.038133,14.774763,13.99285,14.166634,14.853092,13.979447,14.586589,13.808614,6.384816,15.096695,15.064753,13.938987,15.12402,14.347958,13.984018,15.092519,15.798544,13.95193,16.934093,14.075838,15.334475,15.397636,15.769413,14.721025,15.884299,15.862367,15.023471,14.738573,8.016621,10.605681,15.284738,14.491354,15.134404,15.811164,15.525522,15.906236,13.87901]),
array([28.369938,27.045267,27.259162,27.594447,26.789386,28.876111,28.729275,21.86749]),
array([21.689704,23.295443,17.13751,17.754196,23.339942,17.127179,17.385236,18.790845,27.456123]),
array([24.199634]),
array([22.038457,21.76608,24.423727,21.601173,21.05192,20.893809,21.677171,24.555004]),
array([32.880734,27.070866,24.697014]),
array([21.653649,23.085047,16.451709,20.414192,18.764918,19.863194,18.400945,15.989097,18.181187]),
array([18.73854]),
array([18.476801,16.908294,18.463031,19.127698,19.8933]),
array([27.770782,25.73938,24.367397,22.898867,23.145096,21.211788,20.8438,23.552384,23.326048,20.54772,20.839952,17.930447]),
array([23.703988]),
array([25.516825,25.879633,24.372108,21.204804]),
array([19.597395]),
array([33.710481]),
array([15.256505,15.211295,14.435583,15.341027,13.708203]),
array([2.008478,2.404773,2.478823,0.202883,1.038218,0.119678,0.071838]),
array([0.470252]),
array([1.10558]),
array([0.555063,0.07725,0.078945,0.066263,2.059727,0.583302,0.048485,0.016643]),
array([18.625136,19.947757,19.038238,19.419758,17.474881,19.772949,18.791075,16.016121,17.996071,18.995687,17.650568,17.311253,17.133312,17.724471,17.896223,17.970256,19.782343,17.390538,16.611876,19.855143,14.753932,18.929995,18.145156,15.722765,15.472442,14.270204,15.79846]),
array([13.658505,16.217887,17.680399,14.618427]),
array([0.005789,1.547211,0.266751,0.286805,0]),
array([21.581854,23.146737,30.456191]),
array([2.072006]),
array([0.005767]),
array([26.93123,24.905799,30.34811,28.472553,27.579229]),
array([15.200829,15.493209,6.740345]),
array([0.045424,2.280111,0.084288]),
array([3.571326,2.25376]),
array([15.403313,15.955596,6.9162,13.804454,13.31389]),
array([18.712316,19.542763,18.203093,17.394736,13.717299,17.586773,17.824645,19.260763,20.006213,17.860449,17.813771,13.875262,10.826747,13.507019,14.883759,15.447851,14.160239,19.906998,17.598226,13.701458]),
array([19.144767,18.738391,16.739659,15.276119,19.248845,16.949703,17.679655,19.79097,16.781496,17.654692,19.835069,15.024701,19.096379,19.688125,18.314085,17.166082,14.505376,15.195741,14.718455,14.525066,15.549574,13.601334,15.722409,15.132073,13.797931,13.759633,15.474342,13.751185,14.432376,15.509801,13.980974,15.454508,15.708854,16.169642,14.846852]),
array([2.134357,1.371167,1.410759,0.714002,0.109988,0.021885,0.107405,0.043617,0.266635,12.809642]),
array([4.702935,1.640009,1.000358,1.587021,1.254424,0.434821,0.774621,0.032057,1.586027,0.081106,0.097901,0.10654,0.094359,0.094264,0.42209,0.038864,1.700596,0.07667,0.017894,0.071707,0.107199,0.966418,0.027725,0.045717,2.267648,0.041741,0.011034,0.033868,0.052317,0.0636,0.025151,0.087037,0.10277,0.098925]),
array([4.058302]),
array([2.218613,3.843724,2.738618,4.390501,2.029618]),
array([0.643161,1.482365]),
array([3.905376]),
array([9.584452]),
array([5.370165,8.899827,9.318356,8.916745,3.659827,0.42023,1.481138,0.8994,0.895577,0.897316,1.024833,0.853816,0.616339,1.306754,0.032625,0.016808,4.373164,4.417739,2.480638,1.329476,2.29591,3.472909,2.351661,4.756911,2.805575,4.105394,2.864166,1.881087,1.52763,1.578854,0.233623,1.757825,5.195636,2.637053,2.904052,3.033022,1.642831,0.847873,1.571598,1.779396,1.12757,0.224286,3.774136,1.006059,2.099358,1.319836,2.889754,2.435178,2.883035,2.753667,2.885756,2.962943,2.761836,0.242061,2.052309,1.796167,1.250902,1.8621,0.225406,0.246062,0.840436,0.127581,0.649363,0.453739,0.650048,4.262176,0.023413,1.477081,0.824416,2.4213,0.831442,2.108159,0.127356,8.563747,5.255998,2.375126,1.825308,0.41659,3.88013,0.051842,0.02163,0.064041,0.721343,0.686542,1.046908,0.068476,0.258346,1.08044,4.795819,2.701351,2.585237,1.711574,0.721704,0.615429,0.14209,2.509808,0.660246,3.743482,3.23529,2.516388,1.825185,0.05979,0.019027,0.022706,3.927137,1.723715,3.151587,0.115965,0.090876,0.124779,1.905655,4.603808,0.922754,0.55662,0.084813,0.006933]),
array([0.033852]),
array([0.00762,0.436152,0.002427,2.318996,0.008375,0.006063,0.008618,0.090101,0.005374,0.002756,0.00687,2.200311,1.294016,0.577061,0.46303,0.096186,0.017267,2.374947,1.919427,2.318359]),
array([11.19929]),
array([4.042678]),
array([7.010951,5.030777,5.941871,9.424836,4.944116,4.98783,7.333302,5.417574,8.882066,6.778606,8.04247,0.581856,4.947345,8.935981,7.777874,8.355633,10.023924,9.936602,7.6377,8.939155,13.773959]),
array([1.960227,0.732451,0.352804,0.39725,1.108922,1.672659,1.471356,1.432696,1.203728,0.117476,0.025588,0.122058,0.112317,0.067817,0.093999]),
array([0.585213,0.749462,1.012865,1.585509,0.033415,0.033643,0.076869,2.363414,1.933943,2.55596,0.37635,0.647787,0.678349,0.064336,0.09183,0.485253,1.956121,0.30008,0.2919,2.591385,2.476142,0.082868,0.700149,0.318843,0.037914,0.716462,2.302197,0.332138,0.01994,0.769892,0.233265,0.627485,2.323115,2.356588,0.911734,0.034649,1.203279,0.291404,0.241741,0.288152,1.171946,0.747594,0.08763,0.067348,0.777668,0.064284,0.108391,0.125538,0.102344,0.11026,0.099763,0.106579,0.100084,0.113001,0.122874,0.083897,0.026854,0.096242,0.067768,2.511186,0.096434,0.004261,0.001946,0.00489,0.085855,2.220522,0.076777]),
array([0.035529]),
array([0.06194]),
array([0.614529,2.126836,0.70257]),
array([1.447182,2.388881,0.617189,2.428014,0.758759,2.524211,0.314032,2.310185,0.425857]),
array([1.434457])
]

d=[data_1]
names=[ 'canid_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Aelurodon','Aelurodon_asthenostylus','Aelurodon_ferox','Aelurodon_mcgrewi','Aelurodon_montanensis','Aelurodon_stirtoni','Aelurodon_taxoides','Aelurodon_wheelerianus','Alopex','Alopex_lagopus','Archaeocyon_falkenbachi','Archaeocyon_leptodus','Archaeocyon_pavidus','Borophaginae','Borophagus','Borophagus_diversidens','Borophagus_dudleyi','Borophagus_hilli','Borophagus_littoralis','Borophagus_orc','Borophagus_parvus','Borophagus_pugnator','Borophagus_secundus','Caedocyon_tedfordi','Canidae','Caninae','Canini','Canis','Canis_(Pseudalopex)','Canis_adustus','Canis_anthus','Canis_apolloniensis','Canis_armbrusteri','Canis_aureus','Canis_cedazoensis','Canis_dirus','Canis_edwardii','Canis_familiaris','Canis_ferox','Canis_latrans','Canis_lepophagus','Canis_lupus','Canis_mesomelas','Canis_proplatensis','Canis_rufus','Canis_thooides','Carpocyon','Carpocyon_compressus','Carpocyon_limosus','Carpocyon_robustus','Carpocyon_webbi','Cerdocyon_avius','Cerdocyon_texanus','Cerdocyon_thous','Chailicyon_crassidens','Chrysocyon','Chrysocyon_brachyurus','Chrysocyon_nearcticus','Cormocyon','Cormocyon_copei','Cormocyon_haydeni','Cubacyon_transversidens','Cuon','Cuon_alpinus','Cynarctoides_acridens','Cynarctoides_emryi','Cynarctoides_gawnae','Cynarctoides_harlowi','Cynarctoides_lemur','Cynarctoides_luskensis','Cynarctoides_roii','Cynarctoides_whistleri','Cynarctus','Cynarctus_crucidens','Cynarctus_galushai','Cynarctus_marylandica','Cynarctus_saxatilis','Cynarctus_voorhiesi','Cynarctus_wangi','Cynodesmus_martini','Cynodesmus_thooides','Cynodictis','Cynodictis_lacustris','Cynotherium','Cynotherium_sardous','Desmocyon','Desmocyon_matthewi','Desmocyon_thomsoni','Dusicyon','Dusicyon_avus','Dusicyon_culpaeus','Dusicyon_sechurae','Ectopocynus_antiquus','Ectopocynus_intermedius','Ectopocynus_simplicidens','Enhydrocyon','Enhydrocyon_basilatus','Enhydrocyon_crassidens','Enhydrocyon_pahinsintewakpa','Enhydrocyon_stenocephalus','Epicyon','Epicyon_aelurodontoides','Epicyon_haydeni','Epicyon_saevus','Eucyon','Eucyon_davisi','Eucyon_skinneri','Euoplocyon_brachygnathus','Euoplocyon_spissidens','Gobicyon','Hesperocyon','Hesperocyon_coloradensis','Hesperocyon_gregarius','Hesperocyoninae','Leptocyon','Leptocyon_delicatus','Leptocyon_douglassi','Leptocyon_gregorii','Leptocyon_leidyi','Leptocyon_matthewi','Leptocyon_mollis','Leptocyon_tejonensis','Leptocyon_vafer','Leptocyon_vulpinus','Lycaon','Lycaon_pictus','Mesocyon','Mesocyon_brachyops','Mesocyon_coryphaeus','Mesocyon_temnodon','Metalopex_bakeri','Metalopex_macconnelli','Metalopex_merriami','Metatomarctus','Metatomarctus_canavus','Microtomarctus_conferta','Neovulpavus_washakius','Nyctereutes','Nyctereutes_abdeslami','Nyctereutes_procyonoides','Osbornodon_brachypus','Osbornodon_fricki','Osbornodon_iamonensis','Osbornodon_renjiei','Osbornodon_scitulus','Osbornodon_sesnoni','Osbornodon_wangi','Otarocyon_cooki','Otarocyon_macdonaldi','Otocyon','Otocyon_megalotis','Oxetocyon','Oxetocyon_cuspidatus','Paracynarctus_kelloggi','Paracynarctus_sinclairi','Paraenhydrocyon_josephi','Paraenhydrocyon_robustus','Paraenhydrocyon_wallovianus','Paratomarctus_euthos','Paratomarctus_temerarius','Philotrox_condoni','Phlaocyon','Phlaocyon_achoros','Phlaocyon_annectens','Phlaocyon_latidens','Phlaocyon_leucosteus','Phlaocyon_mariae','Phlaocyon_marslandensis','Phlaocyon_minor','Phlaocyon_multicuspus','Phlaocyon_taylori','Phlaocyon_yatkolai','Protemnocyon_inflatus','Protepicyon_raki','Protocyon','Protocyon_orcesi','Protocyon_tarijensis','Protocyon_troglodytes','Protomarctus_optatus','Psalidocyon_marianae','Pseudalopex_gymnocercus','Rhizocyon_oregonensis','Speothos','Speothos_venaticus','Sunkahetanka_geringensis','Tephrocyon_rurestris','Theriodictis','Theriodictis_floridanus','Tomarctus','Tomarctus_brevirostris','Tomarctus_hippophaga','Urocyon','Urocyon_cinereoargenteus','Urocyon_citrinus','Urocyon_galushai','Urocyon_minicephalus','Urocyon_progressus','Urocyon_webbi','Vulpes','Vulpes_cascadensis','Vulpes_chama','Vulpes_kernensis','Vulpes_mathisoni','Vulpes_stenognathus','Vulpes_velox','Vulpes_vulpes','Vulpes_vulpes_macroura','Vulpini','Xenocyon','Xenocyon_lycaonoides','Xenocyon_texanus']
def get_taxa_names(): return taxa_names
