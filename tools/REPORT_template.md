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

{{TABLE_A}}

## 2. Change over five years (SOH differential total, DOR)

Sorted by change from 2022 to 2026. 2022 to 2025 are final rolls (latest DOR revision); 2026 is the preliminary roll.

{{TABLE_B}}

Statewide sum of county SOH differentials: 2022 $679.6 billion; 2023 $893.2 billion; 2024 $929.1 billion; 2025 $890.9 billion; 2026 (preliminary) $815.1 billion. Each county's peak year: 2025 for 25 counties, 2024 for 24, 2023 for 14, 2026 for 3 (Suwannee, Liberty, Lafayette) and 2022 for 1 (Union). The 2026 total is below the 2022 total in 14 counties, led by Sarasota (down 36.8%), Charlotte (down 35.0%), Lee (down 21.2%) and Flagler (down 20.4%).

Per-homestead averages cannot be compared across the five years. DOR does not publish homestead parcel counts by county before 2026 (see Gaps).

## 3. Where a move without portability costs the most

An owner who sells and buys again in Florida **without** portability (for example, they missed the 3-year window, never filed the transfer form, or moved in from a non-homestead) is reassessed at full just value. In year one, they lose roughly the differential times the millage. The loss grows in later years because the lost differential would have kept widening under the cap. Estimated year-one cost for the average and the median homestead (2026 differential, 2025 mills):

| County | Year-one cost, average homestead | Year-one cost, median homestead |
|---|---|---|
{{TABLE_MOVE}}

Owners who **do** port keep up to $500,000 of differential, so for most owners the cost of moving within Florida is small. The exception is the top tier: for them, the differential above $500,000 is lost even with portability. Estimated annual tax on that above-cap differential:

{{TABLE_CAP}}

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
