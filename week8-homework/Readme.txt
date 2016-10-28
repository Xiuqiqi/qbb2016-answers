10.28.2016
Xiuqi
Week8


hifive 5c-complete express -P Nora_E14 -C Nora_ESC_male_E14.counts Nora_Primers.bed

hifive 5c-heatmap Nora_E14.fcp Out.heat -i Out.png -d fragment

hifive 5c-heatmap Nora_E14.fcp Out2.heat -i Out2.png -d enrichment

./CTCFinter.py

out.png is for "fragment"
out2.png is for "enrichment"
