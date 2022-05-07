I collected data on all players of FIFA2019 on the kaggle website,
including height, weight, and various ability values. As one of the most
popular football games, it introduces many variables to measure the
ability of players. In this article, I found that each player has their
own Preferred Foot, the number of players with the preferred left foot
is less, but the average and median of their multiple ability values are
greater than the players with the Preferred Right Foot.

# Abstract

My question is: Can we predict the preferred foot of a player based on
his various abilities? We used **LASSO**, **Logistics model (based on
AIC and CV)**, **stepwise function**, **RandomForest model** to predict
the binominal variable of preferred foot, and finally we came to a
conclusion based on the ROC curve graph:

# Introduction

Let’s first look at a data comparison of preferred left foot and
preferred right foot players (In this project we analyze the player’s
other ability values):

<table>
<caption>Left preferred foot summary table</caption>
<thead>
<tr class="header">
<th style="text-align: left;">Var1</th>
<th style="text-align: left;">Var2</th>
<th style="text-align: left;">Freq</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">Min. :0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">1st Qu.:0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">Median :0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">Mean :0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">3rd Qu.:0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">Max. :0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">Min. :16.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">1st Qu.:21.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">Median :25.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">Mean :25.08</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">3rd Qu.:28.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">Max. :41.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">Min. :157.5</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">1st Qu.:175.3</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">Median :180.3</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">Mean :180.2</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">3rd Qu.:185.4</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">Max. :203.2</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">Min. :110.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">1st Qu.:154.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">Median :163.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">Mean :163.9</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">3rd Qu.:174.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">Max. :218.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">Min. : 8.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">1st Qu.:49.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">Median :60.50</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">Mean :56.61</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">3rd Qu.:67.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">Max. :91.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">Min. : 5</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">1st Qu.:33</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">Median :50</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">Mean :47</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">3rd Qu.:61</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">Max. :95</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">Min. : 7.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">1st Qu.:46.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">Median :55.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">Mean :53.65</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">3rd Qu.:64.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">Max. :91.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">Min. :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">1st Qu.:57.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">Median :63.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">Mean :61.42</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">3rd Qu.:69.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">Min. : 4.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">1st Qu.:32.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">Median :45.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">Mean :44.58</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">3rd Qu.:57.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">Max. :90.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">Min. : 5.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">1st Qu.:55.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">Median :63.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">Mean :59.9</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">3rd Qu.:70.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">Max. :97.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">Min. : 6.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">1st Qu.:40.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">Median :55.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">Mean :52.55</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">3rd Qu.:66.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">Min. : 3.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">1st Qu.:34.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">Median :47.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">Mean :47.63</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">3rd Qu.:62.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">Min. :10.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">1st Qu.:49.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">Median :58.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">Mean :55.74</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">3rd Qu.:65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">Max. :89.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">Min. : 8.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">1st Qu.:58.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">Median :64.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">Mean :61.89</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">3rd Qu.:70.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">Max. :96.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">Min. :15.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">1st Qu.:62.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">Median :70.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">Mean :67.81</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">3rd Qu.:76.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">Max. :97.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">Min. :15.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">1st Qu.:62.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">Median :70.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">Mean :67.84</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">3rd Qu.:76.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">Max. :96.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">Min. :19.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">1st Qu.:59.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">Median :68.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">Mean :66.41</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">3rd Qu.:76.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">Max. :95.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">Min. :30.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">1st Qu.:57.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">Median :63.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">Mean :62.25</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">3rd Qu.:68.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">Max. :95.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">Min. :16.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">1st Qu.:59.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">Median :68.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">Mean :66.45</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">3rd Qu.:76.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">Max. :96.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">Min. : 9.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">1st Qu.:48.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">Median :61.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">Mean :57.79</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">3rd Qu.:69.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">Min. :27.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">1st Qu.:57.25</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">Median :66.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">Mean :64.69</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">3rd Qu.:73.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">Min. :12.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">1st Qu.:60.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">Median :68.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">Mean :65.87</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">3rd Qu.:75.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">Min. :28.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">1st Qu.:57.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">Median :66.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">Mean :64.43</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">3rd Qu.:73.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">Min. : 5.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">1st Qu.:36.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">Median :53.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">Mean :49.9</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">3rd Qu.:64.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">Max. :94.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">Min. :12.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">1st Qu.:48.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">Median :60.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">Mean :57.72</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">3rd Qu.:69.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">Min. : 6.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">1st Qu.:35.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">Median :56.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">Mean :50.54</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">3rd Qu.:65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">Max. :89.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">Min. : 4.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">1st Qu.:45.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">Median :57.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">Mean :53.24</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">3rd Qu.:65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">Min. :10.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">1st Qu.:46.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">Median :56.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">Mean :55.01</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">3rd Qu.:65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">Min. : 9.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">1st Qu.:41.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">Median :50.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">Mean :50.22</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">3rd Qu.:61.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">Max. :90.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">Min. :13.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">1st Qu.:53.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">Median :60.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">Mean :59.8</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">3rd Qu.:67.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">Max. :96.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">Min. : 5.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">1st Qu.:37.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">Median :56.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">Mean :50.99</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">3rd Qu.:65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">Min. : 7.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">1st Qu.:35.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">Median :60.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">Mean :52.08</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">3rd Qu.:67.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">Min. : 6.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">1st Qu.:33.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">Median :57.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">Mean :50.33</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">3rd Qu.:65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">Max. :90.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">Min. : 1.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">1st Qu.: 8.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">Median :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">Mean :13.32</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">3rd Qu.:13.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">Max. :88.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">Min. : 1.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">1st Qu.: 8.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">Median :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">Mean :13.21</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">3rd Qu.:14.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">Max. :91.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">Min. : 1.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">1st Qu.: 8.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">Median :11.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">Mean :13.1</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">3rd Qu.:13.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">Max. :91.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">Min. : 1.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">1st Qu.: 8.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">Median :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">Mean :13.16</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">3rd Qu.:13.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">Max. :86.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">Min. : 1.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">1st Qu.: 8.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">Median :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">Mean :13.33</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">3rd Qu.:14.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">Max. :92.00</td>
</tr>
</tbody>
</table>

Left preferred foot summary table

<table>
<caption>Right preferred foot summary table</caption>
<thead>
<tr class="header">
<th style="text-align: left;">Var1</th>
<th style="text-align: left;">Var2</th>
<th style="text-align: left;">Freq</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">Min. :1</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">1st Qu.:1</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">Median :1</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">Mean :1</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">3rd Qu.:1</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">perfoot_index</td>
<td style="text-align: left;">Max. :1</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">Min. :16.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">1st Qu.:21.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">Median :25.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">Mean :25.11</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">3rd Qu.:28.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Age</td>
<td style="text-align: left;">Max. :45.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">Min. :154.9</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">1st Qu.:177.8</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">Median :182.9</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">Mean :181.6</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">3rd Qu.:185.4</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">height_cm</td>
<td style="text-align: left;">Max. :205.7</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">Min. :110.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">1st Qu.:154.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">Median :165.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">Mean :166.6</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">3rd Qu.:176.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">weight_amount_2</td>
<td style="text-align: left;">Max. :243.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">Min. : 5.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">1st Qu.:35.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">Median :51.50</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">Mean :47.67</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">3rd Qu.:62.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Crossing</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">Min. : 2.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">1st Qu.:29.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">Median :48.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">Mean :45.15</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">3rd Qu.:62.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Finishing</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">Min. : 4.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">1st Qu.:44.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">Median :56.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">Mean :51.88</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">3rd Qu.:65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">HeadingAccuracy</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">Min. : 7.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">1st Qu.:52.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">Median :62.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">Mean :57.89</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">3rd Qu.:68.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShortPassing</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">Min. : 4.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">1st Qu.:29.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">Median :43.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">Mean :42.43</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">3rd Qu.:56.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Volleys</td>
<td style="text-align: left;">Max. :90.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">Min. : 4.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">1st Qu.:46.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">Median :60.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">Mean :54.05</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">3rd Qu.:67.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Dribbling</td>
<td style="text-align: left;">Max. :96.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">Min. : 6.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">1st Qu.:33.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">Median :47.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">Mean :45.6</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">3rd Qu.:60.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Curve</td>
<td style="text-align: left;">Max. :94.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">Min. : 4.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">1st Qu.:30.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">Median :40.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">Mean :41.45</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">3rd Qu.:55.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">FKAccuracy</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">Min. : 9.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">1st Qu.:41.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">Median :55.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">Mean :51.81</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">3rd Qu.:64.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongPassing</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">Min. : 5.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">1st Qu.:53.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">Median :62.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">Mean :57.36</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">3rd Qu.:69.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">BallControl</td>
<td style="text-align: left;">Max. :95.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">Min. :12.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">1st Qu.:55.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">Median :66.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">Mean :63.63</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">3rd Qu.:74.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Acceleration</td>
<td style="text-align: left;">Max. :97.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">Min. :12.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">1st Qu.:55.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">Median :67.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">Mean :63.78</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">3rd Qu.:74.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SprintSpeed</td>
<td style="text-align: left;">Max. :96.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">Min. :14.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">1st Qu.:54.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">Median :65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">Mean :62.65</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">3rd Qu.:73.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Agility</td>
<td style="text-align: left;">Max. :96.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">Min. :21.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">1st Qu.:55.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">Median :62.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">Mean :61.69</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">3rd Qu.:68.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Reactions</td>
<td style="text-align: left;">Max. :96.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">Min. :16.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">1st Qu.:55.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">Median :65.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">Mean :63.21</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">3rd Qu.:73.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Balance</td>
<td style="text-align: left;">Max. :96.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">Min. : 2.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">1st Qu.:45.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">Median :59.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">Mean :54.8</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">3rd Qu.:68.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">ShotPower</td>
<td style="text-align: left;">Max. :95.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">Min. :15.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">1st Qu.:58.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">Median :66.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">Mean :65.25</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">3rd Qu.:73.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Jumping</td>
<td style="text-align: left;">Max. :95.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">Min. :13.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">1st Qu.:55.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">Median :66.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">Mean :62.4</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">3rd Qu.:74.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Stamina</td>
<td style="text-align: left;">Max. :96.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">Min. :17.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">1st Qu.:58.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">Median :67.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">Mean :65.59</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">3rd Qu.:74.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Strength</td>
<td style="text-align: left;">Max. :97.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">Min. : 3.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">1st Qu.:31.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">Median :51.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">Mean :46.29</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">3rd Qu.:62.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">LongShots</td>
<td style="text-align: left;">Max. :93.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">Min. :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">1st Qu.:42.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">Median :58.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">Mean :55.32</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">3rd Qu.:69.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Aggression</td>
<td style="text-align: left;">Max. :95.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">Min. : 3.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">1st Qu.:24.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">Median :50.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">Mean :45.53</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">3rd Qu.:64.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Interceptions</td>
<td style="text-align: left;">Max. :92.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">Min. : 2.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">1st Qu.:35.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">Median :55.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">Mean :49.02</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">3rd Qu.:64.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Positioning</td>
<td style="text-align: left;">Max. :95.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">Min. :10.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">1st Qu.:43.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">Median :55.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">Mean :52.98</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">3rd Qu.:64.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Vision</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">Min. : 5.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">1st Qu.:38.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">Median :49.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">Mean :48.04</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">3rd Qu.:60.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Penalties</td>
<td style="text-align: left;">Max. :92.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">Min. : 3.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">1st Qu.:51.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">Median :59.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">Mean :58.31</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">3rd Qu.:67.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Composure</td>
<td style="text-align: left;">Max. :95.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">Min. : 3.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">1st Qu.:28.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">Median :51.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">Mean :46.14</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">3rd Qu.:63.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">Marking</td>
<td style="text-align: left;">Max. :94.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">Min. : 2.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">1st Qu.:24.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">Median :53.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">Mean :46.35</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">3rd Qu.:66.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">StandingTackle</td>
<td style="text-align: left;">Max. :92.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">Min. : 3.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">1st Qu.:22.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">Median :49.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">Mean :44.22</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">3rd Qu.:63.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">SlidingTackle</td>
<td style="text-align: left;">Max. :91.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">Min. : 1.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">1st Qu.: 8.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">Median :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">Mean :17.58</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">3rd Qu.:14.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKDiving</td>
<td style="text-align: left;">Max. :90.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">Min. : 1.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">1st Qu.: 8.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">Median :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">Mean :17.32</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">3rd Qu.:14.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKHandling</td>
<td style="text-align: left;">Max. :92.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">Min. : 1.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">1st Qu.: 8.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">Median :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">Mean :17.14</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">3rd Qu.:14.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKKicking</td>
<td style="text-align: left;">Max. :91.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">Min. : 1.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">1st Qu.: 8.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">Median :11.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">Mean :17.33</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">3rd Qu.:14.00</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKPositioning</td>
<td style="text-align: left;">Max. :90.00</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">Min. : 1.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">1st Qu.: 8.0</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">Median :11.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">Mean :17.7</td>
</tr>
<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">3rd Qu.:14.0</td>
</tr>
<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;">GKReflexes</td>
<td style="text-align: left;">Max. :94.0</td>
</tr>
</tbody>
</table>

Right preferred foot summary table

<table>
<caption>Number of preferred</caption>
<thead>
<tr class="header">
<th style="text-align: left;">Analyzed_data$Preferred.Foot</th>
<th style="text-align: right;">n</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">Left</td>
<td style="text-align: right;">4162</td>
</tr>
<tr class="even">
<td style="text-align: left;">Right</td>
<td style="text-align: right;">13756</td>
</tr>
</tbody>
</table>

Number of preferred

We can see that in all abilities, left-footed players are better, as
evidenced by both the median and the average. Of course, we have to
mention one important thing, there are far fewer left-footed players
than right-footed players. But based on this difference, I tried to use
machine learning to predict the player’s dominant foot by calculating
various ability values of a player.

Potential Significance: Since left-footed players have higher stats than
right-footed players, if we predict based on a player’s stats that his
dominant foot is the left foot but his dominant foot is actually the
right foot, it means that under the same circumstances, He probably
surpasses someone of the same ability but is left footed, in other
words, at his own level, he is better in terms of perferred foot. This
can be used as a form of self-encouragement

# Methods

The data we mainly use in this project include:

*Dependent variable:* **perfoot\_index**, preferred left foot is 0,
preferred right foot is 1.

*Independent variable:* **Age, height\_cm, weight\_amount\_2, Crossing,
Finishing, HeadingAccuracy** and other ability values.

I mainly use 3 methods, LASSO method (based on AIC and based on
cross-validation), logistic model, and random forest model. First, I
split dataset into training set and test set. Second, I use these
methods and do regression. Third, I use the estimated regression model
and test their accuracy based on test set. Finally, I create a ROC curve
and f1 score for each model, judge which is the best model to complete
my goal.

### LASSO model

I first use `gamlr` package to do the regression, and I choose the
coefficient based on the AIC measurement. In this part, I show the plots
of regression result, and the plot of AIC depends on different lambda.

    ## 载入需要的程辑包：Matrix

    ## 
    ## 载入程辑包：'Matrix'

    ## The following objects are masked from 'package:tidyr':
    ## 
    ##     expand, pack, unpack

    ## Loaded glmnet 4.1-4

![](final_project_files/figure-markdown_strict/lasso%20based%20on%20AIC-1.png)![](final_project_files/figure-markdown_strict/lasso%20based%20on%20AIC-2.png)![](final_project_files/figure-markdown_strict/lasso%20based%20on%20AIC-3.png)

Then I use Lasso do some prediction and set
`ifelse(lasso_predict > 0.5, 1, 0)`, and it shows the result like:

<table>
<caption>LASSO result when choose min lambda</caption>
<thead>
<tr class="header">
<th style="text-align: left;"></th>
<th style="text-align: right;">0</th>
<th style="text-align: right;">1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">0</td>
<td style="text-align: right;">850</td>
<td style="text-align: right;">7</td>
</tr>
<tr class="even">
<td style="text-align: left;">1</td>
<td style="text-align: right;">2660</td>
<td style="text-align: right;">67</td>
</tr>
</tbody>
</table>

LASSO result when choose min lambda

Now I try LASSO regression without AIC approximation, but with cross
validation. Then I plot the comparison plot between AICc and Cross
Validation.

    ## fold 1,2,3,4,5,6,7,8,9,10,done.

![](final_project_files/figure-markdown_strict/withou%20AIC-1.png) I use
Lasso do some prediction and set `ifelse(lasso_predict > 0.5, 1, 0)`,
and it shows the result like:

    ##    yhat
    ## y      0    1
    ##   0  787   70
    ##   1 2136  591

## logistic regression

In this part, I try logistic model to estimate players’ preferred feet.
And it provides the result like (under
`ifelse(log_prediction > 0.5, 1, 0)`):

    ##    yhat
    ## y      0    1
    ##   0  248  609
    ##   1  210 2517

## stepwise function

I use the stepwise function to estimate players’ preferred feet. Below
it gives part of prediction result, under
`ifelse(stepwise_pred>0.5, 1, 0)`.

    ##    yhat
    ## y      0    1
    ##   0  249  608
    ##   1  206 2521

## Tree model

I use random forest tree model to do the regression, and it also provide
some prediction result(under `ifelse(rf_pred > 0.5, 1, 0)`):

    rf_pred = predict(load.forest, Y_test)
    rf_pred_result = ifelse(rf_pred > 0.5, 1, 0)
    rf_pred_result_table = table(y = Y_test$perfoot_index, yhat = rf_pred_result)
    rf_pred_result_table

    ##    yhat
    ## y      0    1
    ##   0   85  772
    ##   1   48 2679

![](final_project_files/figure-markdown_strict/show%20result-1.png)![](final_project_files/figure-markdown_strict/show%20result-2.png)

    ##                   %IncMSE
    ## Age             19.670058
    ## height_cm       19.310194
    ## weight_amount_2 21.223866
    ## Crossing        42.981661
    ## Finishing       36.526868
    ## HeadingAccuracy 28.468521
    ## ShortPassing    40.688275
    ## Volleys         35.880054
    ## Dribbling       23.535156
    ## Curve           33.136651
    ## FKAccuracy      23.656101
    ## LongPassing     29.087800
    ## BallControl     25.750806
    ## Acceleration    22.421775
    ## SprintSpeed     20.567126
    ## Agility         31.306838
    ## Reactions       30.283359
    ## Balance         23.046646
    ## ShotPower       38.261372
    ## Jumping         16.951204
    ## Stamina         19.315870
    ## Strength        23.118044
    ## LongShots       31.049864
    ## Aggression      32.319835
    ## Interceptions   20.702001
    ## Positioning     24.419470
    ## Vision          36.227275
    ## Penalties       36.296523
    ## Composure       34.687209
    ## Marking         24.030605
    ## StandingTackle  20.385181
    ## SlidingTackle   24.174700
    ## GKDiving         9.196987
    ## GKHandling      12.611430
    ## GKKicking       16.021474
    ## GKPositioning    6.752236
    ## GKReflexes      13.132788

## ROC curve

Since we cannot judge any model’s accuracy based on single threshold in
terms of the binominal variable (left or right), so I create a ROC curve
and see their performance. In this case, I set a series of thresholds
for the final binomial variable determination, which is a series of data
`thresh_grid = seq(0.94, 0.45, by=-0.05)`.
<img src="final_project_files/figure-markdown_strict/ROC curves combination-1.png" style="display: block; margin: auto;" />

It looks like the stepwise function has better performance, since the
blue line is always above other lines. To confirm our guess, we
introduce **f1 score**.

## f1 score

    ## 
    ## 载入程辑包：'ModelMetrics'

    ## The following object is masked from 'package:base':
    ## 
    ##     kappa

<table>
<caption>f1 score summary for different models</caption>
<thead>
<tr class="header">
<th style="text-align: left;">modelname</th>
<th style="text-align: right;">f1SCore</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">LASSO_AIC</td>
<td style="text-align: right;">0.0478401</td>
</tr>
<tr class="even">
<td style="text-align: left;">LASSO_CV</td>
<td style="text-align: right;">0.3488784</td>
</tr>
<tr class="odd">
<td style="text-align: left;">Logistic</td>
<td style="text-align: right;">0.8671509</td>
</tr>
<tr class="even">
<td style="text-align: left;">stepwise</td>
<td style="text-align: right;">0.8673338</td>
</tr>
<tr class="odd">
<td style="text-align: left;">randomforest</td>
<td style="text-align: right;">0.8672710</td>
</tr>
</tbody>
</table>

f1 score summary for different models

According to the result, we can see that random forest has the largest
f1 score, which means random forest has better performance than other
models.

# can cluster model distinguish players’s position based on their ability indexes?
