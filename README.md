# RGB LED on Arduino

Playing around with a cheap RGB led string that uses the LED driver [WS2801](https://cdn-shop.adafruit.com/datasheets/WS2801.pdf)

The led string was bought from a generic Aliexpress store called greenglow. Link [here](https://www.aliexpress.com/item/1005007473460609.html?gps-id=pcStoreJustForYou&scm=1007.23125.137358.0&scm_id=1007.23125.137358.0&scm-url=1007.23125.137358.0&pvid=8d091f30-c0d4-4e21-8bc6-c2e6d7aba2bd&_t=gps-id:pcStoreJustForYou,scm-url:1007.23125.137358.0,pvid:8d091f30-c0d4-4e21-8bc6-c2e6d7aba2bd,tpp_buckets:668%232846%238113%231998&pdp_ext_f=%7B%22order%22%3A%223%22%2C%22eval%22%3A%221%22%2C%22sceneId%22%3A%2213125%22%7D&pdp_npi=4%40dis%21EUR%2126.82%2121.19%21%21%2127.80%2121.96%21%40211b629217412094133015055e9878%2112000040897707445%21rec%21ES%212509307440%21X&spm=a2g0o.store_pc_home.smartJustForYou_1257168121.1005007473460609#nav-specification).

## LED Specs

These leds can be daisy-chained, and each one will communicate with the next.

from the aliexpress page

- IC chip: ~WS2811~ WS2801 (it has 1 data, one clock signal... the 2811 has only one data signal)
- Power Consumption :0.3W
- Work Voltage :DC 5V
- Beam Angle: 120
- LED Quantity:1 PCS F8 strawhat lamp
- Color: Full color  
- Dimension:12mm
- Waterproof Grade: IP67
- Life-span:50,000H
- Warranty:3 years
- Module quantity: 50pcs/ string

## Microcontroller

Old Arduino Duemilanuove I have laying around
