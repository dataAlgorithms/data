In [26]: import pandas
    ...:
    ...: # Read a CSV file, skipping last line
    ...: rats = pandas.read_csv(r'd:\tmp\rats.csv', skip_footer=1)
    ...: rats
    ...:
D:\Program Files\Anaconda3\Scripts\ipython-script.py:4: ParserWarning: Falling b
ack to the 'python' engine because the 'c' engine does not support skip_footer;
you can avoid this warning by specifying engine='python'.

Out[26]:
       Creation Date           Status Completion Date  Service Request Number  \

0                NaN           STATUS             NaN  SERVICE REQUEST NUMBER

1         01/01/2011        Completed      01/05/2011             11-00000992

2         01/01/2011        Completed      01/05/2011             11-00001321

3         01/01/2011        Completed      01/05/2011             11-00001629

4         01/01/2011        Completed      01/05/2011             11-00002551

5         01/01/2011        Completed      01/05/2011             11-00002697

6         01/01/2011        Completed      01/05/2011             11-00003085

7         01/01/2011        Completed      01/05/2011             11-00003145

8         01/01/2011        Completed      01/05/2011             11-00003368

9         01/01/2011        Completed      01/05/2011             11-00003411

10        01/01/2011        Completed      01/05/2011             11-00003416

11        01/01/2012  Completed - Dup      01/05/2012             12-00001906

12        01/01/2012  Completed - Dup      01/05/2012             12-00001939

13        01/01/2012        Completed      01/05/2012             12-00001680

14        01/01/2012        Completed      01/05/2012             12-00001723

15        01/01/2012        Completed      01/05/2012             12-00001882

16        01/01/2012        Completed      01/05/2012             12-00001885

17        01/01/2012        Completed      01/05/2012             12-00001905

18        01/01/2012        Completed      01/05/2012             12-00002333

19        01/01/2012        Completed      01/05/2012             12-00002659

20        01/01/2012        Completed      01/05/2012             12-00002703

21        01/01/2012        Completed      01/05/2012             12-00002827

22        01/01/2012        Completed      01/05/2012             12-00002855

23        01/01/2012        Completed      01/05/2012             12-00002909

24        01/01/2012        Completed      01/05/2012             12-00002922

25        01/01/2012        Completed      01/05/2012             12-00003025

26        01/01/2012        Completed      01/05/2012             12-00003031

27        01/01/2013        Completed      01/04/2013             13-00000634

28        01/01/2013        Completed      01/04/2013             13-00000654

29        01/01/2013        Completed      01/04/2013             13-00000700

...              ...              ...             ...                     ...

276622    09/15/2015       Open - Dup             NaN             15-04817112

276623    09/15/2015       Open - Dup             NaN             15-04820827

276624    09/16/2015       Open - Dup             NaN             15-04826826

276625    09/16/2015       Open - Dup             NaN             15-04845826

276626    09/17/2015       Open - Dup             NaN             15-04859213

276627    09/18/2015       Open - Dup             NaN             15-04880791

276628    09/19/2015       Open - Dup             NaN             15-04908490

276629    09/21/2015       Open - Dup             NaN             15-04962457

276630    09/22/2015       Open - Dup             NaN             15-04968595

276631    09/23/2015       Open - Dup             NaN             15-04995011

276632    09/25/2015       Open - Dup             NaN             15-05037936

276633    09/25/2015       Open - Dup             NaN             15-05057119

276634    09/25/2017       Open - Dup             NaN             17-06417240

276635    09/27/2016       Open - Dup             NaN             16-06819267

276636    09/28/2015       Open - Dup             NaN             15-05129923

276637    09/29/2015       Open - Dup             NaN             15-05138013

276638    09/30/2015       Open - Dup             NaN             15-05175903

276639    09/30/2016       Open - Dup             NaN             16-06872746

276640    10/01/2015       Open - Dup             NaN             15-05188967

276641    10/01/2015       Open - Dup             NaN             15-05190546

276642    02/04/2016       Open - Dup             NaN             16-00714859

276643    03/24/2015       Open - Dup             NaN             15-00892952

276644    03/31/2015       Open - Dup             NaN             15-01055718

276645    04/09/2015       Open - Dup             NaN             15-01216737

276646    04/22/2015       Open - Dup             NaN             15-01499900

276647    04/23/2015       Open - Dup             NaN             15-01525901

276648    05/03/2017       Open - Dup             NaN             17-02715859

276649    07/06/2015       Open - Dup             NaN             15-03228941

276650    07/06/2015       Open - Dup             NaN             15-03231828

276651    07/13/2015       Open - Dup             NaN             15-03383761


             Type of Service Request  Number of Premises Baited  \
0            TYPE OF SERVICE REQUEST                        NaN
1       Rodent Baiting/Rat Complaint                        2.0
2       Rodent Baiting/Rat Complaint                        0.0
3       Rodent Baiting/Rat Complaint                        0.0
4       Rodent Baiting/Rat Complaint                        3.0
5       Rodent Baiting/Rat Complaint                        1.0
6       Rodent Baiting/Rat Complaint                        1.0
7       Rodent Baiting/Rat Complaint                        0.0
8       Rodent Baiting/Rat Complaint                        2.0
9       Rodent Baiting/Rat Complaint                        0.0
10      Rodent Baiting/Rat Complaint                        5.0
11      Rodent Baiting/Rat Complaint                        NaN
12      Rodent Baiting/Rat Complaint                        NaN
13      Rodent Baiting/Rat Complaint                        1.0
14      Rodent Baiting/Rat Complaint                        2.0
15      Rodent Baiting/Rat Complaint                        0.0
16      Rodent Baiting/Rat Complaint                        0.0
17      Rodent Baiting/Rat Complaint                        3.0
18      Rodent Baiting/Rat Complaint                        2.0
19      Rodent Baiting/Rat Complaint                        2.0
20      Rodent Baiting/Rat Complaint                        0.0
21      Rodent Baiting/Rat Complaint                        3.0
22      Rodent Baiting/Rat Complaint                        0.0
23      Rodent Baiting/Rat Complaint                        0.0
24      Rodent Baiting/Rat Complaint                        0.0
25      Rodent Baiting/Rat Complaint                        1.0
26      Rodent Baiting/Rat Complaint                        0.0
27      Rodent Baiting/Rat Complaint                        0.0
28      Rodent Baiting/Rat Complaint                        0.0
29      Rodent Baiting/Rat Complaint                        0.0
...                              ...                        ...
276622  Rodent Baiting/Rat Complaint                        NaN
276623  Rodent Baiting/Rat Complaint                        NaN
276624  Rodent Baiting/Rat Complaint                        NaN
276625  Rodent Baiting/Rat Complaint                        NaN
276626  Rodent Baiting/Rat Complaint                        NaN
276627  Rodent Baiting/Rat Complaint                        NaN
276628  Rodent Baiting/Rat Complaint                        NaN
276629  Rodent Baiting/Rat Complaint                        NaN
276630  Rodent Baiting/Rat Complaint                        NaN
276631  Rodent Baiting/Rat Complaint                        NaN
276632  Rodent Baiting/Rat Complaint                        NaN
276633  Rodent Baiting/Rat Complaint                        NaN
276634  Rodent Baiting/Rat Complaint                        NaN
276635  Rodent Baiting/Rat Complaint                        NaN
276636  Rodent Baiting/Rat Complaint                        NaN
276637  Rodent Baiting/Rat Complaint                        NaN
276638  Rodent Baiting/Rat Complaint                        NaN
276639  Rodent Baiting/Rat Complaint                        NaN
276640  Rodent Baiting/Rat Complaint                        NaN
276641  Rodent Baiting/Rat Complaint                        NaN
276642  Rodent Baiting/Rat Complaint                        NaN
276643  Rodent Baiting/Rat Complaint                        NaN
276644  Rodent Baiting/Rat Complaint                        NaN
276645  Rodent Baiting/Rat Complaint                        NaN
276646  Rodent Baiting/Rat Complaint                        NaN
276647  Rodent Baiting/Rat Complaint                        NaN
276648  Rodent Baiting/Rat Complaint                        NaN
276649  Rodent Baiting/Rat Complaint                        NaN
276650  Rodent Baiting/Rat Complaint                        NaN
276651  Rodent Baiting/Rat Complaint                        NaN

        Number of Premises with Garbage  Number of Premises with Rats  \
0                                   NaN                           NaN
1                                   1.0                           2.0
2                                   0.0                           0.0
3                                   0.0                           0.0
4                                   6.0                           3.0
5                                   3.0                           1.0
6                                   3.0                           1.0
7                                   0.0                           0.0
8                                   9.0                           2.0
9                                   5.0                           0.0
10                                  6.0                           5.0
11                                  NaN                           NaN
12                                  NaN                           NaN
13                                  4.0                           1.0
14                                  4.0                           2.0
15                                  2.0                           0.0
16                                 11.0                           0.0
17                                  7.0                           3.0
18                                  6.0                           4.0
19                                  6.0                           2.0
20                                  3.0                           0.0
21                                  1.0                           3.0
22                                  4.0                           0.0
23                                  6.0                           0.0
24                                  2.0                           0.0
25                                  2.0                           1.0
26                                  4.0                           0.0
27                                  2.0                           0.0
28                                  5.0                           0.0
29                                  0.0                           0.0
...                                 ...                           ...
276622                              NaN                           NaN
276623                              NaN                           NaN
276624                              NaN                           NaN
276625                              NaN                           NaN
276626                              NaN                           NaN
276627                              NaN                           NaN
276628                              NaN                           NaN
276629                              NaN                           NaN
276630                              NaN                           NaN
276631                              NaN                           NaN
276632                              NaN                           NaN
276633                              NaN                           NaN
276634                              NaN                           NaN
276635                              NaN                           NaN
276636                              NaN                           NaN
276637                              NaN                           NaN
276638                              NaN                           NaN
276639                              NaN                           NaN
276640                              NaN                           NaN
276641                              NaN                           NaN
276642                              NaN                           NaN
276643                              NaN                           NaN
276644                              NaN                           NaN
276645                              NaN                           NaN
276646                              NaN                           NaN
276647                              NaN                           NaN
276648                              NaN                           NaN
276649                              NaN                           NaN
276650                              NaN                           NaN
276651                              NaN                           NaN

        Current Activity                       Most Recent Action  \
0       CURRENT ACTIVITY                       MOST RECENT ACTION
1          Dispatch Crew                     Inspected and baited
2          Dispatch Crew  Area inspected, no cause and no baiting
3          Dispatch Crew  Area inspected, no cause and no baiting
4          Dispatch Crew                     Inspected and baited
5          Dispatch Crew                     Inspected and baited
6          Dispatch Crew                     Inspected and baited
7          Dispatch Crew  Area inspected, no cause and no baiting
8          Dispatch Crew                     Inspected and baited
9          Dispatch Crew             No contact, left door hanger
10         Dispatch Crew                     Inspected and baited
11                   NaN                                      NaN
12                   NaN                                      NaN
13         Dispatch Crew                     Inspected and baited
14         Dispatch Crew                     Inspected and baited
15         Dispatch Crew                     Inspected and baited
16         Dispatch Crew                     Inspected and baited
17         Dispatch Crew                     Inspected and baited
18         Dispatch Crew                     Inspected and baited
19         Dispatch Crew                     Inspected and baited
20         Dispatch Crew                     Inspected and baited
21         Dispatch Crew                     Inspected and baited
22         Dispatch Crew                     Inspected and baited
23         Dispatch Crew                     Inspected and baited
24         Dispatch Crew                     Inspected and baited
25         Dispatch Crew                     Inspected and baited
26         Dispatch Crew                     Inspected and baited
27         Dispatch Crew                                Completed
28         Dispatch Crew                                Completed
29         Dispatch Crew                                Completed
...                  ...                                      ...
276622               NaN                                      NaN
276623               NaN                                      NaN
276624               NaN                                      NaN
276625               NaN                                      NaN
276626               NaN                                      NaN
276627               NaN                                      NaN
276628               NaN                                      NaN
276629               NaN                                      NaN
276630               NaN                                      NaN
276631               NaN                                      NaN
276632               NaN                                      NaN
276633               NaN                                      NaN
276634               NaN                                      NaN
276635               NaN                                      NaN
276636               NaN                                      NaN
276637               NaN                                      NaN
276638               NaN                                      NaN
276639               NaN                                      NaN
276640               NaN                                      NaN
276641               NaN                                      NaN
276642               NaN                                      NaN
276643               NaN                                      NaN
276644               NaN                                      NaN
276645               NaN                                      NaN
276646               NaN                                      NaN
276647               NaN                                      NaN
276648               NaN                                      NaN
276649               NaN                                      NaN
276650               NaN                                      NaN
276651               NaN                                      NaN

                            Street Address  ZIP Code  X Coordinate  \
0                           STREET ADDRESS       NaN           NaN
1                            437 W ROOT ST   60609.0  1.174071e+06
2                        5545 W MADISON ST   60644.0  1.139306e+06
3                         2540 W ESTES AVE   60645.0  1.158079e+06
4                       7039 S NORMAL BLVD   60621.0  1.174168e+06
5                           1111 E 93RD ST   60619.0  1.185292e+06
6                           7756 S TROY ST   60652.0  1.156724e+06
7                      2511 W AUGUSTA BLVD   60622.0  1.159482e+06
8                     6700 S HERMITAGE AVE   60636.0  1.165830e+06
9                      1241 N LOCKWOOD AVE   60651.0  1.140796e+06
10                      3144 W WARREN BLVD   60612.0  1.155415e+06
11                  2925 N NEW ENGLAND AVE   60634.0  1.129916e+06
12                  2925 N NEW ENGLAND AVE   60634.0  1.129916e+06
13                          3417 W 73RD PL   60629.0  1.154877e+06
14                     4322 W CULLERTON ST   60623.0  1.147883e+06
15                        4253 W FIFTH AVE   60624.0  1.148085e+06
16                           520 E 80TH ST   60619.0  1.181176e+06
17                  2925 N NEW ENGLAND AVE   60634.0  1.129916e+06
18                      1128 W ARDMORE AVE   60660.0  1.167658e+06
19                    5452 N SPAULDING AVE   60625.0  1.153399e+06
20                     2341 W ROOSEVELT RD   60608.0  1.160951e+06
21                          339 W 109TH PL   60628.0  1.176007e+06
22                       2815 N TALMAN AVE   60618.0  1.158234e+06
23                        1314 W GEORGE ST   60657.0  1.167040e+06
24                         4301 W ADAMS ST   60624.0  1.147752e+06
25                     8144 S WOODLAWN AVE   60619.0  1.185630e+06
26                     8147 S WOODLAWN AVE   60619.0  1.185631e+06
27                    6225 N WASHTENAW AVE   60659.0  1.157203e+06
28                        2303 S KOLIN AVE   60623.0  1.148011e+06
29                      4120 N ASHLAND AVE   60613.0  1.164918e+06
...                                    ...       ...           ...
276622                  6232 W NEWPORT AVE   60634.0  1.134231e+06
276623               3144 W IRVING PARK RD   60618.0  1.154607e+06
276624                   3675 N ELSTON AVE   60618.0  1.153564e+06
276625               4434 N SACRAMENTO AVE   60625.0  1.155583e+06
276626                3512 W ARTHINGTON ST   60624.0  1.153101e+06
276627                  6036 S KEATING AVE   60629.0  1.145744e+06
276628                    4824 S THROOP ST   60609.0  1.168474e+06
276629                   3054 N RACINE AVE   60657.0  1.167754e+06
276630                      19 S HOYNE AVE   60612.0  1.162416e+06
276631                    7727 S HOYNE AVE   60620.0  1.163707e+06
276632                   1139 N KARLOV AVE   60651.0  1.148842e+06
276633                    4824 S THROOP ST   60609.0  1.168474e+06
276634                 1560 N SANDBURG TER   60610.0  1.175026e+06
276635                   3054 N RACINE AVE   60657.0  1.167754e+06
276636               2510 S CHRISTIANA AVE   60623.0  1.154431e+06
276637                  7516 S SANGAMON ST   60620.0  1.171278e+06
276638                      19 S HOYNE AVE   60612.0  1.162416e+06
276639                   3054 N RACINE AVE       NaN  1.167754e+06
276640             5810 S NARRAGANSETT AVE   60638.0  1.134719e+06
276641                  4243 N LINCOLN AVE   60618.0  1.161402e+06
276642                3421 S CLAREMONT AVE   60608.0  1.161279e+06
276643                    1445 W TAYLOR ST   60607.0  1.166794e+06
276644                  3101 W CORTLAND ST   60647.0  1.155200e+06
276645                    1445 W TAYLOR ST   60607.0  1.166794e+06
276646                    1600 N TRIPP AVE   60639.0  1.147813e+06
276647                 5400 W HENDERSON ST   60641.0  1.139774e+06
276648  5900 S DR MARTIN LUTHER KING JR DR   60637.0  1.179932e+06
276649                  4556 S EMERALD AVE   60609.0  1.172069e+06
276650                      6523 N TROY ST   60645.0  1.154157e+06
276651                    6121 N MOZART ST   60659.0  1.156233e+06

        Y Coordinate  Ward  Police District  Community Area   Latitude  \
0                NaN   NaN              NaN             NaN        NaN
1       1.877418e+06   3.0              9.0            37.0  41.819041
2       1.899470e+06  29.0             15.0            25.0  41.880258
3       1.947026e+06  50.0             24.0             2.0  42.010392
4       1.858241e+06   6.0              7.0            68.0  41.766415
5       1.843540e+06   8.0              4.0            47.0  41.725819
6       1.852989e+06  18.0              8.0            70.0  41.752374
7       1.906571e+06  26.0             13.0            24.0  41.899352
8       1.860264e+06  15.0              7.0            67.0  41.772147
9       1.907859e+06  37.0             25.0            25.0  41.903250
10      1.900182e+06  28.0             13.0            27.0  41.881901
11      1.918678e+06  36.0             25.0            18.0  41.933131
12      1.918678e+06  36.0             25.0            18.0  41.933131
13      1.855663e+06  18.0              8.0            66.0  41.759746
14      1.890070e+06  24.0             10.0            29.0  41.854301
15      1.896236e+06  24.0             11.0            26.0  41.871219
16      1.852079e+06   6.0              6.0            44.0  41.749346
17      1.918678e+06  36.0             25.0            18.0  41.933131
18      1.938683e+06  48.0             20.0            77.0  41.987297
19      1.936045e+06  40.0             17.0            13.0  41.980354
20      1.894659e+06  25.0             12.0            28.0  41.866633
21      1.832312e+06  34.0              5.0            49.0  41.695221
22      1.918604e+06   1.0             14.0            21.0  41.932397
23      1.919376e+06  32.0             19.0             6.0  41.934331
24      1.898664e+06  28.0             11.0            26.0  41.877888
25      1.851131e+06   8.0              4.0            45.0  41.746643
26      1.851117e+06   8.0              4.0            45.0  41.746602
27      1.941214e+06  50.0             24.0             2.0  41.994461
28      1.888305e+06  22.0             10.0            29.0  41.849455
29      1.927437e+06  47.0             19.0             6.0  41.956496
...              ...   ...              ...             ...        ...
276622  1.922283e+06  36.0             16.0            17.0  41.942950
276623  1.926423e+06  33.0             17.0            16.0  41.953927
276624  1.924276e+06  33.0             17.0            16.0  41.948056
276625  1.929316e+06  33.0             17.0            14.0  41.961846
276626  1.895817e+06  24.0             11.0            27.0  41.869970
276627  1.864162e+06  13.0              8.0            64.0  41.783247
276628  1.872780e+06  20.0              9.0            61.0  41.806437
276629  1.920508e+06  32.0             19.0             6.0  41.937422
276630  1.899920e+06  27.0             12.0            28.0  41.881040
276631  1.853376e+06  18.0              6.0            71.0  41.753290
276632  1.907286e+06  37.0             11.0            23.0  41.901526
276633  1.872780e+06  20.0              9.0            61.0  41.806437
276634  1.910831e+06   2.0             18.0             8.0  41.910706
276635  1.920508e+06  32.0             19.0             6.0  41.937422
276636  1.887126e+06  12.0             10.0            30.0  41.846095
276637  1.854937e+06  17.0              6.0            71.0  41.757412
276638  1.899920e+06  27.0             12.0            28.0  41.881040
276639  1.920508e+06  32.0             19.0             6.0  41.937422
276640  1.865332e+06  13.0              8.0            56.0  41.786658
276641  1.928249e+06  47.0             19.0             5.0  41.958797
276642  1.881941e+06  12.0              9.0            59.0  41.831726
276643  1.895681e+06  28.0             12.0            28.0  41.869316
276644  1.912457e+06   1.0             14.0            22.0  41.915589
276645  1.895681e+06  28.0             12.0            28.0  41.869316
276646  1.910295e+06  26.0             25.0            23.0  41.909804
276647  1.921746e+06  30.0             16.0            15.0  41.941377
276648  1.865980e+06  20.0              2.0            40.0  41.787523
276649  1.874649e+06  11.0              9.0            61.0  41.811487
276650  1.943083e+06  50.0             24.0             2.0  41.999650
276651  1.940513e+06  50.0             24.0             2.0  41.992557

        Longitude                                  Location
0             NaN                                       NaN
1      -87.636954   (41.81904110375691, -87.63695396416237)
2      -87.763950    (41.88025817420532, -87.7639495188141)
3      -87.693713   (42.01039236610359, -87.69371292873835)
4      -87.637166   (41.76641494684121, -87.63716556232575)
5      -87.596855   (41.72581895961811, -87.59685549830274)
6      -87.701248  (41.752373627738436, -87.70124765768429)
7      -87.689670   (41.89935190229656, -87.68967006324442)
8      -87.667671   (41.77214745780087, -87.66767067184314)
9      -87.758273   (41.90325020713387, -87.75827322161487)
10     -87.704781   (41.88190137275809, -87.70478052590498)
11     -87.797989    (41.93313125807079, -87.7979892523638)
12     -87.797989    (41.93313125807079, -87.7979892523638)
13     -87.707945   (41.75974610599034, -87.70794517774965)
14     -87.732695   (41.85430062789185, -87.73269541832288)
15     -87.731797    (41.8712194446494, -87.73179732176091)
16     -87.611671   (41.74934635397685, -87.61167106182282)
17     -87.797989    (41.93313125807079, -87.7979892523638)
18     -87.658710   (41.98729677283302, -87.65870965896644)
19     -87.711228   (41.98035442330003, -87.71122781699026)
20     -87.684604   (41.86663264206997, -87.68460371311866)
21     -87.631202   (41.69522065143191, -87.63120210727071)
22     -87.693925    (41.9323973004704, -87.69392464481953)
23     -87.661541   (41.93433140216767, -87.66154129786436)
24     -87.732955  (41.877888331577275, -87.73295534268999)
25     -87.595377   (41.74664277994884, -87.59537684969652)
26     -87.595376   (41.74660243223972, -87.59537584596985)
27     -87.697096    (41.9944609997409, -87.69709576089141)
28     -87.732272   (41.84945488068342, -87.73227249526849)
29     -87.669110  (41.956496264125555, -87.66911006992231)
...           ...                                       ...
276622 -87.782047   (41.942949955692754, -87.7820472364623)
276623 -87.707042    (41.95392660071533, -87.7070422427468)
276624 -87.710935  (41.948055998981694, -87.71093542952525)
276625 -87.703376   (41.96184612318967, -87.70337597201659)
276626 -87.713393   (41.86997029813066, -87.71339266194195)
276627 -87.741202   (41.78324671348921, -87.74120208821508)
276628 -87.657617   (41.80643747571596, -87.65761673280419)
276629 -87.658882    (41.93742220307765, -87.6588818174058)
276630 -87.679079  (41.881040002164504, -87.67907947155189)
276631 -87.675648   (41.75329013589339, -87.67564794533163)
276632 -87.728730    (41.90152573869621, -87.7287298178832)
276633 -87.657617   (41.80643747571596, -87.65761673280419)
276634 -87.632447  (41.910705895622435, -87.63244696989126)
276635 -87.658882    (41.93742220307765, -87.6588818174058)
276636 -87.708740   (41.846094691105286, -87.7087402817187)
276637 -87.647854   (41.75741244251146, -87.64785435408605)
276638 -87.679079  (41.881040002164504, -87.67907947155189)
276639 -87.658882    (41.93742220307765, -87.6588818174058)
276640 -87.781598  (41.786658469266534, -87.78159824534002)
276641 -87.682013   (41.95879709193433, -87.68201344869898)
276642 -87.683752   (41.83172610169727, -87.68375248641249)
276643 -87.663123   (41.869316134106626, -87.6631233110701)
276644 -87.705240   (41.91558920348518, -87.70523981533253)
276645 -87.663123   (41.869316134106626, -87.6631233110701)
276646 -87.732433   (41.90980399896635, -87.73243329561515)
276647 -87.761687  (41.941376717744284, -87.76168726395535)
276648 -87.615802   (41.787522714000744, -87.6158022110909)
276649 -87.644377    (41.8114866852777, -87.64437669576763)
276650 -87.708248   (41.99965044554477, -87.70824808024489)
276651 -87.700684    (41.99255722559823, -87.7006835932538)

[276652 rows x 20 columns]

In [27]:

In [27]: # Investigate range of values for a certain field
    ...: rats['Current Activity'].unique()
Out[27]:
array(['CURRENT ACTIVITY', 'Dispatch Crew', nan,
       'Request Sanitation Inspector', 'Inspect for Violation',
       'FVI - Outcome'], dtype=object)

In [28]: # Filter the data
    ...: crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
    ...: len(crew_dispatched)
    ...:
Out[28]: 256386

In [29]: print(type(crew_dispatched['ZIP Code'].value_counts()))
<class 'pandas.core.series.Series'>

In [30]: # Find 10 most rat-infested ZIP codes in Chicago
    ...: crew_dispatched['ZIP Code'].value_counts()[:10]
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\base.py in get_slice
_bound(self, label, side, kind)
   2909             try:
-> 2910                 return self._searchsorted_monotonic(label, side)
   2911             except ValueError:

D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\base.py in _searchso
rted_monotonic(self, label, side)
   2875
-> 2876         raise ValueError('index must be monotonic increasing or decreasi
ng')
   2877

ValueError: index must be monotonic increasing or decreasing

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-30-37293585ad28> in <module>()
      1 # Find 10 most rat-infested ZIP codes in Chicago
----> 2 crew_dispatched['ZIP Code'].value_counts()[:10]

D:\Program Files\Anaconda3\lib\site-packages\pandas\core\series.py in __getitem_
_(self, key)
    622             key = check_bool_indexer(self.index, key)
    623
--> 624         return self._get_with(key)
    625
    626     def _get_with(self, key):

D:\Program Files\Anaconda3\lib\site-packages\pandas\core\series.py in _get_with(
self, key)
    627         # other: fancy integer or otherwise
    628         if isinstance(key, slice):
--> 629             indexer = self.index._convert_slice_indexer(key, kind='getit
em')
    630             return self._get_values(indexer)
    631         elif isinstance(key, ABCDataFrame):

D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\numeric.py in _conve
rt_slice_indexer(self, key, kind)
    288
    289         # translate to locations
--> 290         return self.slice_indexer(key.start, key.stop, key.step, kind=ki
nd)
    291
    292     def _format_native_types(self, na_rep='', float_format=None, decimal
='.',

D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\base.py in slice_ind
exer(self, start, end, step, kind)
   2783         """
   2784         start_slice, end_slice = self.slice_locs(start, end, step=step,
-> 2785                                                  kind=kind)
   2786
   2787         # return a slice

D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\base.py in slice_loc
s(self, start, end, step, kind)
   2968         end_slice = None
   2969         if end is not None:
-> 2970             end_slice = self.get_slice_bound(end, 'right', kind)
   2971         if end_slice is None:
   2972             end_slice = len(self)

D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\base.py in get_slice
_bound(self, label, side, kind)
   2911             except ValueError:
   2912                 # raise the original KeyError
-> 2913                 raise err
   2914
   2915         if isinstance(slc, np.ndarray):

D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\base.py in get_slice
_bound(self, label, side, kind)
   2905         # we need to look up the label
   2906         try:
-> 2907             slc = self.get_loc(label)
   2908         except KeyError as err:
   2909             try:

D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\numeric.py in get_lo
c(self, key, method, tolerance)
    367             pass
    368         return super(Float64Index, self).get_loc(key, method=method,
--> 369                                                  tolerance=tolerance)
    370
    371     @property

D:\Program Files\Anaconda3\lib\site-packages\pandas\indexes\base.py in get_loc(s
elf, key, method, tolerance)
   1945                 return self._engine.get_loc(key)
   1946             except KeyError:
-> 1947                 return self._engine.get_loc(self._maybe_cast_indexer(key
))
   1948
   1949         indexer = self.get_indexer([key], method=method, tolerance=toler
ance)

pandas\index.pyx in pandas.index.IndexEngine.get_loc (pandas\index.c:4154)()

pandas\index.pyx in pandas.index.IndexEngine.get_loc (pandas\index.c:4018)()

pandas\hashtable.pyx in pandas.hashtable.Float64HashTable.get_item (pandas\hasht
able.c:9667)()

pandas\hashtable.pyx in pandas.hashtable.Float64HashTable.get_item (pandas\hasht
able.c:9611)()

KeyError: 10.0


In [32]:
    ...: # Group by completion date
    ...: dates = crew_dispatched.groupby('Completion Date')
    ...: len(dates)
    ...:
Out[32]: 1713

In [33]: # Determine counts on each day
    ...: date_counts = dates.size()
    ...: date_counts[0:10]
    ...:
Out[33]:
Completion Date
01/01/2014      7
01/02/2013     20
01/02/2014     96
01/02/2015      5
01/03/2011      4
01/03/2012    125
01/03/2013     46
01/03/2014     59
01/03/2017    212
01/04/2011     54
dtype: int64

In [34]: # Sort the counts
    ...: date_counts.sort()
    ...: date_counts[-10:]
    ...:
D:\Program Files\Anaconda3\Scripts\ipython-script.py:2: FutureWarning: sort is d
eprecated, use sort_values(inplace=True) for INPLACE sorting
  import sys
Out[34]:
Completion Date
11/28/2014    384
10/14/2011    391
08/17/2017    392
10/11/2017    392
11/12/2013    401
10/14/2016    412
10/07/2011    457
07/06/2016    461
11/01/2013    488
09/09/2016    492
dtype: int64
