# Findings: Florida Save Our Homes Benefit by County

Compiled by Kevin D. Klagge, Esq. (Klagge Law, PLLC, StepUpLaw). Built 2026-09-23 from Florida Department of Revenue (DOR) primary files. Method, definitions and legal rules are in `README.md`; the data are in `data/counties.csv` (67 counties x 2022 to 2026).

## Headline

- On the 2026 preliminary roll, Florida's 5,251,737 homestead parcels carry a Save Our Homes differential of **$815.1 billion** (DOR county total; the county figures sum to exactly the $815,135,591,712 on DOR's 2026 statewide DR-489V recapitulation, line 12). The average homestead's differential is **$153,489** (NAL).
- For the average homestead in the top counties, the cap is worth an **estimated $5,436 a year in Miami-Dade, $5,026 in Palm Beach and $4,586 in Broward** (average differential x 2025 total millage). In the lowest county, Union, it is worth $216.
- **The benefit is shrinking.** The statewide differential peaked at $929.1 billion in 2024. It fell to $890.9 billion in 2025 and to $815.1 billion on the 2026 preliminary roll. It fell in 63 of 67 counties from 2025 to 2026.
- **Portability now covers most owners but not the top tier.** 187,319 homesteads (3.6%) carry a differential above the $500,000 portability cap. Together they hold $122.7 billion that cannot be carried to a new home, worth an estimated $2.06 billion a year in tax at 2025 rates.
- **The portability window is 3 years, not 2.** The current Constitution (Art. VII, s. 4(d)(8)) and s. 193.155(8) both say a new homestead qualifies if the owner had a homestead exemption "as of January 1 of any of the 3 immediately preceding years". A 2-year rule is an older version of the law.

All sources: SOH totals from DOR Data Book `county_overview.xlsx` ("Save Our Homes Value History"); parcel counts, homestead just and assessed values and distributions from DOR's 2026 NAL roll files; millage from DOR Data Book `millage_taxes_levied.xlsx` ("Total Millage Rate"); portability from DOR `amendment_1_impact.xlsx`. Every dollar-of-tax figure is an **estimate**: differential x county Total Millage Rate / 1000, using the 2025 rate because DOR has not yet published 2026 levies.

## 1. Ranked table, latest year (2026 preliminary roll)

Ranked by estimated annual tax saved for the average homestead. "Est. tax saved at median" applies the same millage to the median homestead's differential. It is included because the average is pulled up by a small number of very large differentials. "Homesteads over $500k" counts parcels whose differential exceeds the portability cap. Source columns: homestead parcels, average, median and over-$500k counts from the 2026 NAL; SOH total from the DOR Data Book; mills from the DOR 2025 millage table.

| Rank | County | Homestead parcels | SOH differential total (DOR) | Avg differential per homestead | Median differential | 2025 total mills | Est. avg annual tax saved | Est. tax saved at median | Homesteads over $500k |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Miami-Dade | 451,377 | $134,298,708,315 | $294,035 | $218,511 | 18.4893 | $5,436 | $4,040 | 44,851 (9.9%) |
| 2 | Palm Beach | 366,108 | $106,259,673,147 | $287,327 | $155,335 | 17.4918 | $5,026 | $2,717 | 34,191 (9.3%) |
| 3 | Broward | 419,468 | $97,803,396,020 | $230,895 | $184,130 | 19.8638 | $4,586 | $3,658 | 30,814 (7.3%) |
| 4 | Monroe | 15,702 | $7,553,424,236 | $475,825 | $276,279 | 8.2361 | $3,919 | $2,275 | 4,131 (26.3%) |
| 5 | Martin | 48,966 | $11,615,377,427 | $234,670 | $141,844 | 16.0598 | $3,769 | $2,278 | 3,804 (7.8%) |
| 6 | Pinellas | 250,466 | $41,348,214,354 | $162,443 | $126,552 | 18.4941 | $3,004 | $2,340 | 10,747 (4.3%) |
| 7 | Indian River | 51,024 | $10,384,912,325 | $201,725 | $121,942 | 14.1659 | $2,858 | $1,727 | 3,218 (6.3%) |
| 8 | Nassau | 31,913 | $5,481,013,365 | $171,243 | $117,467 | 16.0559 | $2,749 | $1,886 | 1,647 (5.2%) |
| 9 | Orange | 255,817 | $39,771,268,095 | $153,863 | $145,692 | 17.4100 | $2,679 | $2,536 | 5,214 (2.0%) |
| 10 | Collier | 108,425 | $28,288,327,214 | $260,032 | $129,142 | 9.8185 | $2,553 | $1,268 | 11,986 (11.1%) |
| 11 | Saint Lucie | 106,134 | $11,945,505,200 | $110,665 | $102,238 | 21.5570 | $2,386 | $2,204 | 630 (0.6%) |
| 12 | Hillsborough | 315,709 | $40,355,680,785 | $126,286 | $105,488 | 18.8553 | $2,381 | $1,989 | 5,836 (1.8%) |
| 13 | Saint Johns | 96,532 | $15,608,639,942 | $159,275 | $112,468 | 13.9738 | $2,226 | $1,572 | 4,360 (4.5%) |
| 14 | Seminole | 106,895 | $15,203,762,517 | $140,349 | $141,635 | 15.3480 | $2,154 | $2,174 | 887 (0.8%) |
| 15 | Duval | 212,984 | $23,931,843,746 | $111,565 | $91,091 | 17.8910 | $1,996 | $1,630 | 3,818 (1.8%) |
| 16 | Volusia | 159,518 | $18,219,866,408 | $112,493 | $99,903 | 17.4169 | $1,959 | $1,740 | 1,764 (1.1%) |
| 17 | Alachua | 54,802 | $4,903,509,691 | $88,751 | $81,562 | 20.8894 | $1,854 | $1,704 | 163 (0.3%) |
| 18 | Manatee | 112,560 | $13,709,557,118 | $120,730 | $85,730 | 14.5524 | $1,757 | $1,248 | 2,744 (2.4%) |
| 19 | Pasco | 169,296 | $15,941,695,628 | $92,314 | $83,074 | 17.2168 | $1,589 | $1,430 | 234 (0.1%) |
| 20 | Brevard | 182,211 | $21,053,339,130 | $114,198 | $102,180 | 13.7669 | $1,572 | $1,407 | 1,735 (0.9%) |
| 21 | Gulf | 4,225 | $538,312,453 | $125,964 | $89,217 | 12.2198 | $1,539 | $1,090 | 115 (2.7%) |
| 22 | Clay | 60,166 | $6,039,570,216 | $99,517 | $97,626 | 15.3466 | $1,527 | $1,498 | 240 (0.4%) |
| 23 | DeSoto | 6,415 | $616,648,911 | $95,482 | $86,128 | 15.9319 | $1,521 | $1,372 | 18 (0.3%) |
| 24 | Lake | 114,071 | $11,152,080,457 | $96,713 | $84,392 | 15.6324 | $1,512 | $1,319 | 476 (0.4%) |
| 25 | Lee | 214,474 | $23,054,261,774 | $106,490 | $72,732 | 13.9967 | $1,491 | $1,018 | 3,764 (1.8%) |
| 26 | Hendry | 8,721 | $743,300,670 | $84,232 | $70,514 | 17.1732 | $1,447 | $1,211 | 41 (0.5%) |
| 27 | Leon | 58,098 | $4,721,890,681 | $79,207 | $73,120 | 17.8003 | $1,410 | $1,302 | 52 (0.1%) |
| 28 | Flagler | 43,657 | $3,636,221,310 | $82,007 | $73,674 | 17.1551 | $1,407 | $1,264 | 213 (0.5%) |
| 29 | Sarasota | 139,125 | $15,284,260,634 | $109,011 | $60,522 | 12.7527 | $1,390 | $772 | 4,307 (3.1%) |
| 30 | Franklin | 3,471 | $450,035,512 | $129,372 | $76,355 | 10.6003 | $1,371 | $809 | 140 (4.0%) |
| 31 | Walton | 22,789 | $3,431,421,424 | $149,279 | $51,762 | 9.1512 | $1,366 | $474 | 1,551 (6.8%) |
| 32 | Hernando | 62,191 | $5,931,879,187 | $93,277 | $88,588 | 14.5695 | $1,359 | $1,291 | 157 (0.2%) |
| 33 | Osceola | 87,265 | $8,012,269,512 | $90,730 | $83,810 | 14.9738 | $1,359 | $1,255 | 156 (0.2%) |
| 34 | Hardee | 4,589 | $427,987,651 | $92,216 | $85,839 | 14.1244 | $1,302 | $1,212 | 1 (0.0%) |
| 35 | Marion | 121,437 | $9,986,075,330 | $80,992 | $69,580 | 15.8838 | $1,286 | $1,105 | 660 (0.5%) |
| 36 | Okeechobee | 8,946 | $814,108,302 | $88,772 | $81,048 | 14.4357 | $1,281 | $1,170 | 13 (0.1%) |
| 37 | Levy | 14,224 | $1,103,346,608 | $76,958 | $68,976 | 16.0399 | $1,234 | $1,106 | 8 (0.1%) |
| 38 | Escambia | 76,258 | $6,699,156,679 | $87,268 | $75,536 | 14.1316 | $1,233 | $1,067 | 500 (0.7%) |
| 39 | Citrus | 56,159 | $4,494,783,502 | $79,261 | $74,906 | 15.4758 | $1,227 | $1,159 | 117 (0.2%) |
| 40 | Baker | 6,869 | $567,035,468 | $81,585 | $76,630 | 14.6131 | $1,192 | $1,120 | 2 (0.0%) |
| 41 | Polk | 174,240 | $13,209,922,334 | $74,921 | $63,018 | 15.4378 | $1,157 | $973 | 231 (0.1%) |
| 42 | Putnam | 20,992 | $1,346,230,862 | $63,401 | $47,155 | 17.7142 | $1,123 | $835 | 42 (0.2%) |
| 43 | Okaloosa | 51,326 | $4,644,796,150 | $89,728 | $68,303 | 12.2773 | $1,102 | $839 | 733 (1.4%) |
| 44 | Highlands | 27,044 | $2,026,702,832 | $74,064 | $68,776 | 14.5216 | $1,076 | $999 | 19 (0.1%) |
| 45 | Charlotte | 69,832 | $4,754,127,923 | $67,386 | $46,378 | 15.6763 | $1,056 | $727 | 246 (0.4%) |
| 46 | Bradford | 7,071 | $452,214,971 | $63,341 | $54,846 | 16.5732 | $1,050 | $909 | 3 (0.0%) |
| 47 | Suwannee | 11,313 | $756,794,572 | $66,530 | $55,193 | 15.6611 | $1,042 | $864 | 3 (0.0%) |
| 48 | Gilchrist | 5,668 | $378,584,102 | $65,567 | $57,414 | 15.5297 | $1,018 | $892 | 0 (0.0%) |
| 49 | Glades | 2,759 | $152,629,075 | $54,671 | $42,818 | 18.3732 | $1,004 | $787 | 0 (0.0%) |
| 50 | Columbia | 16,809 | $1,147,927,743 | $67,558 | $62,967 | 14.6841 | $992 | $925 | 5 (0.0%) |
| 51 | Hamilton | 2,903 | $186,109,187 | $63,785 | $51,404 | 15.2115 | $970 | $782 | 2 (0.1%) |
| 52 | Madison | 4,440 | $280,716,391 | $61,854 | $53,474 | 15.1668 | $938 | $811 | 3 (0.1%) |
| 53 | Santa Rosa | 55,270 | $4,221,246,642 | $75,385 | $65,274 | 11.7171 | $883 | $765 | 255 (0.5%) |
| 54 | Jefferson | 3,946 | $252,387,970 | $61,966 | $51,333 | 13.8674 | $859 | $712 | 3 (0.1%) |
| 55 | Washington | 6,409 | $363,492,024 | $56,209 | $50,502 | 14.9640 | $841 | $756 | 0 (0.0%) |
| 56 | Taylor | 5,470 | $295,243,806 | $53,541 | $45,125 | 15.4326 | $826 | $696 | 2 (0.0%) |
| 57 | Lafayette | 1,862 | $93,955,946 | $49,756 | $28,964 | 16.2231 | $807 | $470 | 0 (0.0%) |
| 58 | Sumter | 60,115 | $4,303,906,378 | $71,429 | $54,480 | 11.2052 | $800 | $610 | 176 (0.3%) |
| 59 | Bay | 45,901 | $2,838,229,668 | $61,301 | $34,673 | 12.6966 | $778 | $440 | 276 (0.6%) |
| 60 | Wakulla | 10,536 | $586,286,812 | $54,094 | $43,540 | 13.4421 | $727 | $585 | 9 (0.1%) |
| 61 | Dixie | 4,912 | $175,729,273 | $35,739 | $27,910 | 19.8732 | $710 | $555 | 0 (0.0%) |
| 62 | Gadsden | 10,381 | $452,424,605 | $42,701 | $34,291 | 16.1423 | $689 | $554 | 3 (0.0%) |
| 63 | Jackson | 10,606 | $491,064,632 | $46,107 | $39,594 | 14.2637 | $658 | $565 | 1 (0.0%) |
| 64 | Calhoun | 3,276 | $126,704,990 | $38,240 | $27,438 | 15.3340 | $586 | $421 | 0 (0.0%) |
| 65 | Liberty | 1,686 | $53,807,346 | $31,595 | $18,555 | 15.1744 | $479 | $282 | 1 (0.1%) |
| 66 | Holmes | 4,920 | $123,217,691 | $24,933 | $20,953 | 15.4115 | $384 | $323 | 1 (0.0%) |
| 67 | Union | 2,993 | $38,776,843 | $12,897 | $8,508 | 16.7165 | $216 | $142 | 0 (0.0%) |

## 2. Change over five years (SOH differential total, DOR)

Sorted by change from 2022 to 2026. 2022 to 2025 are final rolls (latest DOR revision); 2026 is the preliminary roll.

| County | 2022 | 2023 | 2024 | 2025 | 2026 prelim | Change 2022 to 2026 | Change 2025 to 2026 |
|---|---|---|---|---|---|---|---|
| Holmes | $26,264,967 | $31,048,976 | $49,067,464 | $137,302,339 | $123,217,691 | +369.1% | -10.3% |
| Suwannee | $223,179,146 | $501,416,259 | $620,873,846 | $713,130,786 | $756,794,572 | +239.1% | +6.1% |
| Liberty | $22,650,717 | $23,259,660 | $32,481,744 | $40,395,372 | $53,807,346 | +137.6% | +33.2% |
| Bradford | $191,316,545 | $327,653,706 | $400,955,502 | $456,119,136 | $452,214,971 | +136.4% | -0.9% |
| Jackson | $263,733,228 | $470,249,884 | $549,234,288 | $498,384,018 | $491,064,632 | +86.2% | -1.5% |
| Bay | $1,550,229,281 | $2,511,828,476 | $2,754,808,801 | $2,936,369,044 | $2,838,229,668 | +83.1% | -3.3% |
| Nassau | $3,032,713,441 | $4,467,462,071 | $4,939,661,483 | $5,537,911,450 | $5,481,013,365 | +80.7% | -1.0% |
| Lafayette | $52,340,753 | $84,137,739 | $83,853,913 | $91,430,185 | $93,955,946 | +79.5% | +2.8% |
| Washington | $204,388,649 | $271,865,983 | $348,849,387 | $383,701,109 | $363,492,024 | +77.8% | -5.3% |
| Gilchrist | $213,478,116 | $297,234,169 | $351,791,053 | $395,266,683 | $378,584,102 | +77.3% | -4.2% |
| Columbia | $652,943,414 | $936,217,634 | $1,084,822,082 | $1,202,190,929 | $1,147,927,743 | +75.8% | -4.5% |
| Franklin | $258,013,629 | $398,505,337 | $520,889,885 | $468,600,977 | $450,035,512 | +74.4% | -4.0% |
| Calhoun | $72,781,847 | $65,071,270 | $117,628,561 | $129,229,080 | $126,704,990 | +74.1% | -2.0% |
| Hardee | $252,393,837 | $336,788,847 | $412,431,684 | $448,177,967 | $427,987,651 | +69.6% | -4.5% |
| Hamilton | $115,701,199 | $140,735,308 | $150,655,956 | $203,118,444 | $186,109,187 | +60.9% | -8.4% |
| Miami-Dade | $86,094,538,592 | $118,647,689,139 | $139,323,199,761 | $139,762,710,490 | $134,298,708,315 | +56.0% | -3.9% |
| Jefferson | $162,162,617 | $258,246,893 | $258,959,377 | $264,982,490 | $252,387,970 | +55.6% | -4.8% |
| Dixie | $116,915,797 | $148,788,443 | $183,871,405 | $186,013,814 | $175,729,273 | +50.3% | -5.5% |
| Indian River | $7,003,331,076 | $10,698,566,522 | $11,107,427,633 | $10,891,352,276 | $10,384,912,325 | +48.3% | -4.6% |
| Broward | $66,151,090,480 | $91,054,322,690 | $100,318,292,250 | $103,740,324,710 | $97,803,396,020 | +47.8% | -5.7% |
| Wakulla | $399,586,971 | $490,075,444 | $599,303,320 | $681,412,149 | $586,286,812 | +46.7% | -14.0% |
| Orange | $27,742,061,344 | $39,289,967,972 | $42,830,471,644 | $43,898,321,774 | $39,771,268,095 | +43.4% | -9.4% |
| Madison | $202,112,903 | $311,136,831 | $300,144,737 | $284,693,388 | $280,716,391 | +38.9% | -1.4% |
| Palm Beach | $76,690,889,315 | $111,477,206,740 | $112,773,714,016 | $107,523,513,032 | $106,259,673,147 | +38.6% | -1.2% |
| Alachua | $3,547,712,823 | $4,348,272,813 | $5,301,528,966 | $5,975,742,685 | $4,903,509,691 | +38.2% | -17.9% |
| Lake | $8,086,862,508 | $10,666,907,455 | $11,617,260,742 | $11,570,924,570 | $11,152,080,457 | +37.9% | -3.6% |
| Okeechobee | $599,736,979 | $853,401,997 | $843,491,682 | $865,498,942 | $814,108,302 | +35.7% | -5.9% |
| Martin | $8,578,268,346 | $12,343,994,955 | $12,618,923,557 | $12,652,904,163 | $11,615,377,427 | +35.4% | -8.2% |
| Gadsden | $334,701,497 | $435,859,803 | $518,171,586 | $477,301,681 | $452,424,605 | +35.2% | -5.2% |
| Levy | $819,077,626 | $1,111,072,096 | $1,168,604,350 | $1,145,948,276 | $1,103,346,608 | +34.7% | -3.7% |
| Leon | $3,523,408,344 | $4,394,587,537 | $4,638,557,695 | $4,842,335,507 | $4,721,890,681 | +34.0% | -2.5% |
| Gulf | $402,356,472 | $521,426,035 | $539,175,665 | $569,381,601 | $538,312,453 | +33.8% | -5.5% |
| Seminole | $11,886,743,522 | $15,366,616,751 | $16,491,165,372 | $16,226,183,600 | $15,203,762,517 | +27.9% | -6.3% |
| Monroe | $5,921,739,710 | $8,730,966,279 | $9,061,060,615 | $8,407,747,167 | $7,553,424,236 | +27.6% | -10.2% |
| Clay | $4,866,427,316 | $6,518,167,006 | $6,555,641,821 | $6,510,585,131 | $6,039,570,216 | +24.1% | -7.2% |
| Taylor | $242,454,453 | $355,880,602 | $370,678,688 | $331,481,071 | $295,243,806 | +21.8% | -10.9% |
| Marion | $8,269,242,436 | $10,816,154,413 | $10,980,140,006 | $10,478,596,543 | $9,986,075,330 | +20.8% | -4.7% |
| Hendry | $619,227,685 | $817,483,638 | $800,009,494 | $785,875,129 | $743,300,670 | +20.0% | -5.4% |
| Pasco | $13,284,191,924 | $19,149,202,522 | $19,571,739,145 | $17,949,785,827 | $15,941,695,628 | +20.0% | -11.2% |
| Baker | $472,696,842 | $533,245,063 | $565,817,062 | $611,281,134 | $567,035,468 | +20.0% | -7.2% |
| Osceola | $6,706,043,614 | $9,555,655,357 | $9,614,475,998 | $9,097,563,384 | $8,012,269,512 | +19.5% | -11.9% |
| Duval | $20,089,477,523 | $24,576,037,179 | $24,442,197,252 | $25,071,786,893 | $23,931,843,746 | +19.1% | -4.5% |
| Escambia | $5,647,418,568 | $7,105,868,313 | $7,326,512,973 | $6,979,512,313 | $6,699,156,679 | +18.6% | -4.0% |
| Highlands | $1,753,968,894 | $2,352,059,507 | $2,449,315,660 | $2,285,616,565 | $2,026,702,832 | +15.5% | -11.3% |
| Saint Johns | $13,612,578,167 | $16,841,720,658 | $16,842,031,072 | $16,821,748,529 | $15,608,639,942 | +14.7% | -7.2% |
| Citrus | $4,039,416,763 | $5,318,079,125 | $5,366,922,218 | $4,881,762,196 | $4,494,783,502 | +11.3% | -7.9% |
| Saint Lucie | $10,794,906,519 | $14,229,582,050 | $14,086,459,209 | $13,210,545,459 | $11,945,505,200 | +10.7% | -9.6% |
| Putnam | $1,218,399,846 | $1,667,999,337 | $1,797,602,529 | $1,478,440,776 | $1,346,230,862 | +10.5% | -8.9% |
| Volusia | $16,647,888,451 | $20,937,776,274 | $21,254,589,858 | $20,330,062,441 | $18,219,866,408 | +9.4% | -10.4% |
| Glades | $140,011,039 | $180,873,729 | $180,278,775 | $165,108,088 | $152,629,075 | +9.0% | -7.6% |
| Pinellas | $39,104,839,644 | $50,803,993,845 | $54,055,252,049 | $49,480,276,570 | $41,348,214,354 | +5.7% | -16.4% |
| Santa Rosa | $4,062,616,682 | $4,438,305,783 | $4,403,891,916 | $4,570,575,418 | $4,221,246,642 | +3.9% | -7.6% |
| DeSoto | $609,662,310 | $602,939,404 | $647,366,686 | $653,943,531 | $616,648,911 | +1.1% | -5.7% |
| Walton | $3,445,151,216 | $4,247,209,130 | $4,120,632,446 | $4,009,219,106 | $3,431,421,424 | -0.4% | -14.4% |
| Polk | $13,641,236,326 | $16,861,540,903 | $16,204,642,059 | $14,486,379,025 | $13,209,922,334 | -3.2% | -8.8% |
| Manatee | $14,526,367,735 | $20,201,875,720 | $19,420,001,795 | $15,393,485,242 | $13,709,557,118 | -5.6% | -10.9% |
| Hernando | $6,305,898,657 | $7,275,518,640 | $7,327,072,272 | $6,881,672,029 | $5,931,879,187 | -5.9% | -13.8% |
| Brevard | $22,667,812,740 | $25,812,854,870 | $25,438,832,630 | $22,925,060,980 | $21,053,339,130 | -7.1% | -8.2% |
| Union | $42,253,517 | $35,119,116 | $35,194,010 | $35,274,645 | $38,776,843 | -8.2% | +9.9% |
| Hillsborough | $44,034,548,647 | $45,311,403,658 | $48,814,889,116 | $45,058,177,583 | $40,355,680,785 | -8.4% | -10.4% |
| Collier | $31,736,898,889 | $44,030,120,542 | $37,711,735,865 | $35,361,076,354 | $28,288,327,214 | -10.9% | -20.0% |
| Okaloosa | $5,353,327,150 | $6,181,505,395 | $5,711,230,976 | $5,534,192,013 | $4,644,796,150 | -13.2% | -16.1% |
| Sumter | $4,988,767,526 | $5,696,408,766 | $5,217,551,536 | $5,014,643,595 | $4,303,906,378 | -13.7% | -14.2% |
| Flagler | $4,565,877,013 | $4,767,946,539 | $4,903,800,711 | $4,599,038,439 | $3,636,221,310 | -20.4% | -20.9% |
| Lee | $29,246,870,068 | $36,332,157,099 | $36,058,762,947 | $29,296,685,229 | $23,054,261,774 | -21.2% | -21.3% |
| Charlotte | $7,315,482,010 | $9,890,252,220 | $9,369,180,643 | $7,029,413,331 | $4,754,127,923 | -35.0% | -32.4% |
| Sarasota | $24,180,941,680 | $27,784,735,869 | $24,543,419,508 | $19,926,441,499 | $15,284,260,634 | -36.8% | -23.3% |

Statewide sum of county SOH differentials: 2022 $679.6 billion; 2023 $893.2 billion; 2024 $929.1 billion; 2025 $890.9 billion; 2026 (preliminary) $815.1 billion. Each county's peak year: 2025 for 25 counties, 2024 for 24, 2023 for 14, 2026 for 3 (Suwannee, Liberty, Lafayette) and 2022 for 1 (Union). The 2026 total is below the 2022 total in 14 counties, led by Sarasota (down 36.8%), Charlotte (down 35.0%), Lee (down 21.2%) and Flagler (down 20.4%).

Per-homestead averages cannot be compared across the five years. DOR does not publish homestead parcel counts by county before 2026 (see Gaps).

## 3. Where a move without portability costs the most

An owner who sells and buys again in Florida **without** portability (for example, they missed the 3-year window, never filed the transfer form, or moved in from a non-homestead) is reassessed at full just value. In year one, they lose roughly the differential times the millage. The loss grows in later years because the lost differential would have kept widening under the cap. Estimated year-one cost for the average and the median homestead (2026 differential, 2025 mills):

| County | Year-one cost, average homestead | Year-one cost, median homestead |
|---|---|---|
| Miami-Dade | $5,436 | $4,040 |
| Palm Beach | $5,026 | $2,717 |
| Broward | $4,586 | $3,658 |
| Monroe | $3,919 | $2,275 |
| Martin | $3,769 | $2,278 |
| Pinellas | $3,004 | $2,340 |
| Indian River | $2,858 | $1,727 |
| Nassau | $2,749 | $1,886 |
| Orange | $2,679 | $2,536 |
| Collier | $2,553 | $1,268 |

Owners who **do** port keep up to $500,000 of differential, so for most owners the cost of moving within Florida is small. The exception is the top tier: for them, the differential above $500,000 is lost even with portability. Estimated annual tax on that above-cap differential:

| County | Homesteads over $500k | Differential above cap | Est. annual tax on it (2025 mills) | Per affected homestead |
|---|---|---|---|---|
| Palm Beach | 34,191 | $37,971,462,000 | $664,189,219 | $19,426 |
| Miami-Dade | 44,851 | $32,803,014,767 | $606,504,781 | $13,523 |
| Broward | 30,814 | $12,226,393,020 | $242,862,626 | $7,882 |
| Collier | 11,986 | $9,445,924,749 | $92,744,812 | $7,738 |
| Pinellas | 10,747 | $3,800,812,824 | $70,292,612 | $6,541 |
| Martin | 3,804 | $3,235,868,247 | $51,967,397 | $13,661 |
| Hillsborough | 5,836 | $2,504,178,779 | $47,217,042 | $8,091 |
| Indian River | 3,218 | $2,916,465,646 | $41,314,361 | $12,839 |
| Saint Johns | 4,360 | $2,144,517,418 | $29,967,057 | $6,873 |
| Orange | 5,214 | $1,709,063,708 | $29,754,799 | $5,707 |
| Lee | 3,764 | $2,111,295,036 | $29,551,163 | $7,851 |
| Sarasota | 4,307 | $2,156,190,518 | $27,497,251 | $6,384 |

Statewide, an estimated $2.06 billion a year of tax benefit sits above the portability cap. It would be lost on a move even with timely filing. This group is where estate planning matters most: a lady bird deed or other transfer that s. 193.155(3)(a) excludes from "change of ownership" keeps the cap in place for a surviving spouse or a continuing homestead owner. A sale and repurchase cannot keep more than $500,000.

Owners moving **out of state** lose everything: the full average differential, $5,436 a year in Miami-Dade at 2025 rates.

## 4. Ten surprising findings

1. **The benefit fell 12.3% in two years.** The statewide differential dropped from $929.1 billion (2024) to $815.1 billion (2026 preliminary). The differential only widens when market value rises faster than the cap (3% or CPI), so a flat or falling market narrows it from the top. Sixty-three of 67 counties shrank from 2025 to 2026.
2. **Southwest Florida's cushion is disappearing fastest.** From 2022 to 2026 the differential fell 36.8% in Sarasota, 35.0% in Charlotte, 21.2% in Lee and 10.9% in Collier. From 2025 to 2026 alone it fell 32.4% in Charlotte.
3. **About one homestead in five gets nothing from the cap.** 959,454 homestead parcels statewide (18.3%) have a differential of zero or less: their assessed value equals just value. The share is 33.5% in Charlotte, 29.9% in Manatee, 29.7% in Flagler and 29.0% in Sarasota (NAL 2026).
4. **Monroe has the largest average differential but ranks only 4th in dollars.** The average Monroe homestead is sheltered on $475,825 of value, 62% more than Miami-Dade's $294,035. But Monroe's total millage of 8.2361 is the lowest in the state (2025), so the tax value is $3,919 against Miami-Dade's $5,436.
5. **A quarter of Keys homesteads are over the portability cap.** 26.3% of Monroe homestead parcels (4,131) have a differential above $500,000. The next highest shares are Collier (11.1%), Miami-Dade (9.9%) and Palm Beach (9.3%).
6. **The average misleads badly in resort counties.** Walton's average differential ($149,279) is 2.9 times its median ($51,762). Collier's is 2.0 times ($260,032 against $129,142) and Palm Beach's 1.8 times. In Seminole the median ($141,635) is actually above the average ($140,349).
7. **Miami-Dade homesteads are assessed at 56% of market value.** Statewide, homestead assessed value is 65.9% of just value (NAL 2026). Miami-Dade is lowest at 56.1%, then Broward 58.9% and Hardee 59.1%. Union is highest at 89.0%.
8. **Movers are fewer but carry far more.** Portability transfers fell from 106,353 (2022) to 83,352 (2025). Meanwhile the average value ported per transfer roughly doubled, from $64,652 to $134,489 (DOR `amendment_1_impact.xlsx`; the average is computed as value divided by count). In 51 of 67 counties, the average ported amount in 2026 exceeds the county's average homestead differential. That pattern is consistent with movers being mostly long-time owners, though the data cannot show it directly.
9. **Rural Panhandle counties quietly surged.** Holmes County's differential rose 369% from 2022 to 2026, including a 2.8-fold jump in 2025 (from $49.1 million to $137.3 million). Suwannee's rose 239% and Liberty's 138%. The Holmes jump is in DOR's table as published. It is unexplained here and worth a call to the Holmes County Property Appraiser before quoting.
10. **Single-parcel extremes.** The largest single homestead differential on the 2026 NAL is $131.6 million, in Palm Beach, followed by $128.7 million in Miami-Dade and $70.5 million in Lee. At Palm Beach's 2025 average millage, the Palm Beach parcel's cap is worth more than $2 million a year in tax. These are roll values as recorded and have not been verified parcel by parcel.

Also notable: Saint Lucie has the highest 2025 total millage in the state (21.557). That lifts a modest $110,665 average differential to 11th place in tax value.

## 5. Gaps and data issues (complete list)

1. **Homestead parcel counts and homestead just and assessed totals, 2022 to 2025: blank for all 67 counties (268 county-years).** The DOR Data Book does not break these out. The NAL files that do are hosted only for the current year (2026). Older years are not on the DOR portal, and the Wayback Machine holds just one 2026 file. As a result, `avg_soh_differential_per_homestead` and `est_avg_annual_tax_saved` are also blank for 2022 to 2025. The SOH totals and millage for those years are complete. **To fill:** request the 2022 to 2025 final NAL files from DOR Property Tax Oversight (PTOResearchAnalysis@floridarevenue.com, the contact listed in the Data Book), then rerun `tools/nal_summarize.py` on them.
2. **2026 millage not published.** DOR's current Data Book (retrieved 2026-09-23) still carries the 2025 millage table. `avg_total_millage` is blank for 2026, and the 2026 tax estimate uses 2025 rates.
3. **2026 is a preliminary roll.** Values will move with Value Adjustment Board changes and final certification.
4. **Citrus 2026:** the preliminary NAL file is not on the DOR portal. The 2026 final NAL file (posted 2026-09-23) was used instead, so Citrus's homestead figures are one roll stage later than the other 66 counties'.
5. **NAL versus Data Book gap.** In every county, the NAL sum of homestead just minus assessed value is 0.10% to 3.12% below the Data Book SOH figure (largest gaps: Jefferson 3.1%, Wakulla 2.8%, Leon 2.5%, Okeechobee 2.5%). Statewide, the NAL homestead just value ($2,363.7 billion) is 1.0% below DR-489V line 8 ($2,387.6 billion). The likely cause is different extract dates. Each row's `note` gives the county's gap.
6. **Manatee 2026 portability count looks incomplete.** DOR reports 245 transfers in 2026 against 2,299 to 2,662 in each of 2022 to 2025. Treat Manatee's 2026 portability figures as provisional.
7. **Holmes 2025 SOH jump** (2.8-fold in one year) is as published by DOR and is unexplained.
8. **Footnote markers.** DOR's millage tables label Orange and Osceola "Orange1" and "Osceola1". The footnote text is not in the workbook. Rates were used as shown.
9. **Within-county millage.** The Total Millage Rate is a county average. Municipal and MSTU millage varies by location, and a city resident's actual rate can differ by several mills.
10. **Exempt owners.** Owners whose taxable value is already zero or near zero (for example, totally and permanently disabled veterans) save little from the cap. The average-based estimate overstates their benefit. The NAL could separate them, but that was not done here.
11. **The portability window.** Descriptions of a "2-year window" for portability are out of date. Current law is 3 years. Chapter 2026-239 changes "immediate prior homestead" to "prior homestead" in s. 193.155(8)(a) and (b) starting with the 2027 roll. It does not change the $500,000 cap or the window.
12. **Not verified parcel by parcel.** The extreme single-parcel differentials (finding 10) are as recorded on the roll.

## Validation performed

- The county SOH figures for 2026 sum to $815,135,591,712, equal to DOR's 2026 preliminary statewide DR-489V line 12 ("Homestead Assessment Differential"), `statewide_recap.xlsx`.
- For 2021 to 2025, the SOH figure as first published in each year's Data Book and as revised in the 2026 Data Book differ by less than 1% for every county.
- Each millage table's stated year was checked against its roll year.
- Every county has 5 rows; every 2026 row has a NAL-based homestead count; nothing was imputed.
