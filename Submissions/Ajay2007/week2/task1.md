

### *Find the useragent and print the whole line if it is not a Chrome browser*

#### awk {'print  $10 $11 $12 $13 $14 $15 $16 $17 $18 $19 $20 $21 $22  '} access.log | sed '/Chrome/d'
