# CryptoPiReader


![alt text](https://github.com/antoninpa/CryptoPiReader/blob/master/static/screen.png " ")

## English

**An ASCII cryptocurrency chart on raspberry screen**

In itself the code is pretty straightforward: 	
 * Data is pulled from the [cryptocompare API](https://www.cryptocompare.com/api/#introduction)
 * Plotting is built using the [gnuplotlib](https://github.com/dkogan/gnuplotlib) library

The terminal resolution is optimized for the official RPi touch screen but can be modified without any other modification.

**Preventing the screen from entering sleep mode**

If you wish to let the raspberry displaying the chart you may want to prevent the terminal and the screen from turning black. I recommend you follow the instructions at [bitpi.co](https://www.bitpi.co/2015/02/14/prevent-raspberry-pi-from-sleeping/).

***
## Français

**Graphique des cryptomonnaies en ASCII sur Raspberry Pi**

Rien particulier de sorcier:
 * Les données sont extraites de l'API de [cryptocompare](https://www.cryptocompare.com/api/#introduction)
 * Les graphique est dessiné à l'aide de [gnuplotlib](https://github.com/dkogan/gnuplotlib)

La résolution du terminal est optimisée pour l'écran officiel Raspberry Pi mais elle peut être modifiée aisément.
 
**Empêcher l'écran et le terminal d'entrer en veille**

Si vous voulez que les informations restent affichées en permanence il est nécessaire d'empêcher l'écran et le terminal de rentrer en mode veille. Pour ce faire il suffit de suivre les instructions mentionnées sur la page de [bitpi.co](https://www.bitpi.co/2015/02/14/prevent-raspberry-pi-from-sleeping/).

Licence:
CC:BY-NC-SA // Antonin Paillet
